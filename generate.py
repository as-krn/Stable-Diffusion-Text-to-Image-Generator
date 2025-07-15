from diffusers import StableDiffusionPipeline
import torch
import os
from datetime import datetime
from googletrans import Translator
import logging
from typing import Optional, Tuple
import re

# Logging ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StableDiffusionGenerator:
    def __init__(self, model_id: str = "runwayml/stable-diffusion-v1-5"):
        """
        Stable Diffusion görsel üretici sınıfı
        
        Args:
            model_id: Kullanılacak Stable Diffusion model ID'si
        """
        self.model_id = model_id
        self.pipe = None
        self.translator = Translator()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Türkçe karakter düzeltme sözlüğü
        self.turkish_chars = {
            'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
            'Ç': 'C', 'Ğ': 'G', 'I': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
        }
        
        logger.info(f"Cihaz: {self.device}")
        
    def load_model(self):
        """Modeli yükle"""
        try:
            logger.info("Model yükleniyor...")
            self.pipe = StableDiffusionPipeline.from_pretrained(
                self.model_id,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                safety_checker=None,
                requires_safety_checker=False
            )
            self.pipe = self.pipe.to(self.device)
            
            # Bellek optimizasyonu
            if self.device == "cuda":
                self.pipe.enable_attention_slicing()
                self.pipe.enable_model_cpu_offload()
            
            logger.info("Model başarıyla yüklendi!")
            
        except Exception as e:
            logger.error(f"Model yüklenirken hata: {e}")
            raise
    
    def detect_language(self, text: str) -> str:
        """Metin dilini algıla"""
        try:
            detected = self.translator.detect(text)
            return detected.lang
        except:
            return "tr"  # Varsayılan olarak Türkçe
    
    def translate_to_english(self, text: str) -> str:
        """Türkçe metni İngilizce'ye çevir"""
        try:
            if self.detect_language(text) == "tr":
                # Türkçe karakterleri düzelt
                for tr_char, en_char in self.turkish_chars.items():
                    text = text.replace(tr_char, en_char)
                
                # Çeviri yap
                translated = self.translator.translate(text, src='tr', dest='en')
                logger.info(f"Çeviri: '{text}' -> '{translated.text}'")
                return translated.text
            else:
                return text
        except Exception as e:
            logger.warning(f"Çeviri hatası: {e}, orijinal metin kullanılacak")
            return text
    
    def clean_filename(self, text: str) -> str:
        """Dosya adı için güvenli string oluştur"""
        # Türkçe karakterleri değiştir
        for tr_char, en_char in self.turkish_chars.items():
            text = text.replace(tr_char, en_char)
        
        # Özel karakterleri kaldır
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '_', text)
        
        return text[:50]  # Maksimum 50 karakter
    
    def generate_image(self, 
                      prompt: str, 
                      negative_prompt: str = "blurry, low quality, distorted, ugly",
                      width: int = 512,
                      height: int = 512,
                      num_inference_steps: int = 20,
                      guidance_scale: float = 7.5,
                      output_dir: str = "outputs",
                      auto_translate: bool = True) -> Optional[str]:
        """
        Görsel üret
        
        Args:
            prompt: Görsel açıklaması
            negative_prompt: İstenmeyen özellikler
            width: Görsel genişliği
            height: Görsel yüksekliği
            num_inference_steps: İterasyon sayısı (daha yüksek = daha kaliteli)
            guidance_scale: Prompt'a ne kadar bağlı kalınacağı
            output_dir: Çıktı dizini
            auto_translate: Otomatik çeviri yapılsın mı
        
        Returns:
            Kaydedilen dosyanın yolu
        """
        if self.pipe is None:
            self.load_model()
        
        try:
            # Otomatik çeviri
            original_prompt = prompt
            if auto_translate:
                prompt = self.translate_to_english(prompt)
            
            logger.info(f"Görsel üretiliyor: '{prompt}'")
            
            # Görsel üret
            image = self.pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale
            ).images[0]
            
            # Dosya kaydetme
            os.makedirs(output_dir, exist_ok=True)
            
            # Dosya adı oluştur
            clean_prompt = self.clean_filename(original_prompt)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{clean_prompt}.png"
            filepath = os.path.join(output_dir, filename)
            
            # Kaydet
            image.save(filepath)
            logger.info(f"Görsel kaydedildi: {filepath}")
            
            return filepath
            
        except Exception as e:
            logger.error(f"Görsel üretilirken hata: {e}")
            return None
    
    def generate_multiple_images(self, 
                               prompt: str, 
                               count: int = 4,
                               **kwargs) -> list:
        """
        Aynı prompt için birden fazla görsel üret
        
        Args:
            prompt: Görsel açıklaması
            count: Üretilecek görsel sayısı
            **kwargs: generate_image metoduna geçirilecek diğer parametreler
        
        Returns:
            Üretilen dosya yollarının listesi
        """
        results = []
        for i in range(count):
            logger.info(f"Görsel {i+1}/{count} üretiliyor...")
            filepath = self.generate_image(prompt, **kwargs)
            if filepath:
                results.append(filepath)
        
        return results

# Kullanım örneği
if __name__ == "__main__":
    # Generator oluştur
    generator = StableDiffusionGenerator()
    
    # Tek görsel üret
    prompt = "mavi gökyüzünde uçan renkli bir kedi"
    filepath = generator.generate_image(
        prompt=prompt,
        num_inference_steps=25,
        guidance_scale=8.0
    )
    
    if filepath:
        print(f"Görsel başarıyla üretildi: {filepath}")
    
    # Çoklu görsel üret
    print("\nÇoklu görsel üretimi...")
    filepaths = generator.generate_multiple_images(
        prompt="fantastik bir orman manzarası",
        count=3,
        num_inference_steps=20
    )
    
    print(f"{len(filepaths)} görsel üretildi:")
    for path in filepaths:
        print(f"  - {path}")