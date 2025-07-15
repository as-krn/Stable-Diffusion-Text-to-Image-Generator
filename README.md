# 🖼️ Stable Diffusion Text-to-Image Generator
# EN
A user-friendly Streamlit application that generates images from text descriptions using Stable Diffusion AI. The application supports both Turkish and English prompts with automatic translation capabilities.

## ✨ Features

- **Text-to-Image Generation**: Create stunning images from text descriptions
- **Multi-language Support**: Works with Turkish and English prompts
- **Automatic Translation**: Converts Turkish prompts to English for better results
- **Multiple Image Generation**: Generate up to 4 variations of the same prompt
- **Quality Settings**: Choose between Fast, Medium, and High quality modes
- **User-friendly Interface**: Clean Streamlit web interface
- **Download Support**: Download generated images directly
- **Advanced Settings**: Customize negative prompts and generation parameters

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/stable-diffusion-generator.git
cd stable-diffusion-generator
```

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
diffusers>=0.21.0
torch>=2.0.0
torchvision>=0.15.0
transformers>=4.33.0
accelerate>=0.20.0
googletrans==4.0.0rc1
Pillow>=9.0.0
```

## 🚀 Usage

1. **Start the Streamlit application**:
```bash
streamlit run app.py
```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Enter your text description** in Turkish or English

4. **Adjust settings** (optional):
   - Choose quality level (Fast/Medium/High)
   - Select number of images to generate
   - Modify negative prompts in advanced settings

5. **Click "Generate"** and wait for your images to be created

## 🎯 Example Prompts

- "sunset over ocean waves"
- "cyberpunk neon city at night"
- "fantasy forest with fairy lights"
- "fluffy orange cat sitting on windowsill"
- "Van Gogh style sunflower field"
- "sunset beach landscape" (Turkish: gün batımında sahil manzarası)
- "wooden cabin in snowy mountain" (Turkish: kar yağan dağda ahşap kulübe)

## 🔧 Configuration

The application uses the following default settings:
- Model: `runwayml/stable-diffusion-v1-5`
- Image size: 512x512 pixels
- Device: CUDA (if available) or CPU
- Output directory: `outputs/`

## 📁 Project Structure

```
stable-diffusion-generator/
├── app.py                 # Streamlit web interface
├── generate.py           # Core image generation logic
├── requirements.txt      # Python dependencies
├── outputs/             # Generated images directory
├── README.md            # This file
```

## ⚙️ Advanced Configuration

### Quality Settings Mapping:
- **Fast**: 15 steps, guidance scale 6.0
- **Medium**: 20 steps, guidance scale 7.5
- **High**: 30 steps, guidance scale 9.0

### Supported Languages:
- English (native)
- Turkish (with automatic translation)

### Image Output Format:
- Format: PNG
- Naming: `YYYYMMDD_HHMMSS_prompt_description.png`
- Location: `outputs/` directory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## ⚠️ System Requirements

- Python 3.8+
- CUDA-compatible GPU (recommended for faster generation)
- At least 8GB RAM
- 10GB free disk space

## 🐛 Troubleshooting

### Common Issues:

1. **Model loading takes too long**
   - First-time usage requires downloading the model (~4GB)
   - Subsequent runs will be faster

2. **Out of memory errors**
   - Reduce image size or use CPU instead of GPU
   - Close other applications to free up memory

3. **Translation errors**
   - Check internet connection (required for Google Translate)
   - Very long prompts may cause translation issues

4. **Slow generation on CPU**
   - Consider using a GPU for faster processing
   - Reduce quality settings for quicker results

## 📊 Performance Tips

- Use GPU for significantly faster generation
- Lower inference steps for quicker results
- Batch multiple images for efficiency
- Enable attention slicing for memory optimization

## 🔄 Version History

- **v1.0.0**: Initial release
  - Basic text-to-image generation
  - Turkish language support
  - Streamlit interface

## 🌟 Acknowledgments

- [Stability AI](https://stability.ai/) for Stable Diffusion
- [Hugging Face](https://huggingface.co/) for the Diffusers library
- [Streamlit](https://streamlit.io/) for the web framework

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the documentation

---

⭐ **If you found this project helpful, please give it a star!**

## 👉 Example of Use
![WhatsApp Görsel 2025-07-13 saat 18 20 53_05fc7b63](https://github.com/user-attachments/assets/42f1d482-21bb-4f90-99f8-b6bf0bc11818)

# TR
# 🖼️ Stable Diffusion Metinden Görsel Üretici

Stable Diffusion yapay zekası kullanarak metin açıklamalarından görsel üreten kullanıcı dostu bir Streamlit uygulaması. Uygulama hem Türkçe hem de İngilizce promptları destekler ve otomatik çeviri özelliği sunar.

## ✨ Özellikler

- **Metinden Görsel Üretimi**: Metin açıklamalarından etkileyici görseller oluşturun
- **Çoklu Dil Desteği**: Türkçe ve İngilizce promptlarla çalışır
- **Otomatik Çeviri**: Daha iyi sonuçlar için Türkçe promptları İngilizce'ye çevirir
- **Çoklu Görsel Üretimi**: Aynı prompt için 4'e kadar varyasyon üretin
- **Kalite Ayarları**: Hızlı, Orta ve Yüksek kalite modları arasında seçim yapın
- **Kullanıcı Dostu Arayüz**: Temiz Streamlit web arayüzü
- **İndirme Desteği**: Üretilen görselleri doğrudan indirin
- **Gelişmiş Ayarlar**: Negatif promptları ve üretim parametrelerini özelleştirin

## 🛠️ Kurulum

1. **Depoyu klonlayın**:
```bash
git clone https://github.com/yourusername/stable-diffusion-generator.git
cd stable-diffusion-generator
```

2. **Sanal ortam oluşturun**:
```bash
python -m venv venv
source venv/bin/activate  # Windows'ta: venv\Scripts\activate
```

3. **Bağımlılıkları yükleyin**:
```bash
pip install -r requirements.txt
```

## 📋 Gereksinimler

Aşağıdaki bağımlılıkları içeren bir `requirements.txt` dosyası oluşturun:

```
streamlit>=1.28.0
diffusers>=0.21.0
torch>=2.0.0
torchvision>=0.15.0
transformers>=4.33.0
accelerate>=0.20.0
googletrans==4.0.0rc1
Pillow>=9.0.0
```

## 🚀 Kullanım

1. **Streamlit uygulamasını başlatın**:
```bash
streamlit run app.py
```

2. **Tarayıcınızı açın** ve `http://localhost:8501` adresine gidin

3. **Metin açıklamanızı girin** (Türkçe veya İngilizce)

4. **Ayarları düzenleyin** (isteğe bağlı):
   - Kalite seviyesini seçin (Hızlı/Orta/Yüksek)
   - Üretilecek görsel sayısını belirleyin
   - Gelişmiş ayarlarda negatif promptları değiştirin

5. **"Üret" butonuna tıklayın** ve görsellerinizin oluşturulmasını bekleyin

## 🎯 Örnek Promptlar

- "gün batımında sahil manzarası"
- "kar yağan dağda ahşap kulübe"
- "uzayda yüzen renkli kediler"
- "cyberpunk tarzı neon şehir"
- "fantastik orman ile peri ışıkları"
- "Van Gogh tarzında ayçiçeği tarlası"
- "okyanus dalgaları üzerinde gün batımı" (İngilizce: sunset over ocean waves)
- "pencere pervazında oturan tüylü turuncu kedi" (İngilizce: fluffy orange cat sitting on windowsill)

## 🔧 Yapılandırma

Uygulama aşağıdaki varsayılan ayarları kullanır:
- Model: `runwayml/stable-diffusion-v1-5`
- Görsel boyutu: 512x512 piksel
- Cihaz: CUDA (varsa) veya CPU
- Çıktı dizini: `outputs/`

## 📁 Proje Yapısı

```
stable-diffusion-generator/
├── app.py                 # Streamlit web arayüzü
├── generate.py           # Ana görsel üretim mantığı
├── requirements.txt      # Python bağımlılıkları
├── outputs/             # Üretilen görseller dizini
├── README.md            # Bu dosya
```

## ⚙️ Gelişmiş Yapılandırma

### Kalite Ayarları Haritası:
- **Hızlı**: 15 adım, kılavuz ölçeği 6.0
- **Orta**: 20 adım, kılavuz ölçeği 7.5
- **Yüksek**: 30 adım, kılavuz ölçeği 9.0

### Desteklenen Diller:
- İngilizce (ana dil)
- Türkçe (otomatik çeviri ile)

### Görsel Çıktı Formatı:
- Format: PNG
- Adlandırma: `YYYYAAGG_SSDDSS_prompt_aciklamasi.png`
- Konum: `outputs/` dizini

## 🤝 Katkıda Bulunma

1. Depoyu fork edin
2. Bir özellik dalı oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Dalı push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request açın


## ⚠️ Sistem Gereksinimleri

- Python 3.8+
- CUDA uyumlu GPU (daha hızlı üretim için önerilen)
- En az 8GB RAM
- 10GB boş disk alanı

## 🐛 Sorun Giderme

### Yaygın Sorunlar:

1. **Model yükleme çok uzun sürüyor**
   - İlk kullanımda modelin indirilmesi gerekir (~4GB)
   - Sonraki çalıştırmalar daha hızlı olacak

2. **Bellek yetersizliği hataları**
   - Görsel boyutunu küçültün veya GPU yerine CPU kullanın
   - Belleği boşaltmak için diğer uygulamaları kapatın

3. **Çeviri hataları**
   - İnternet bağlantısını kontrol edin (Google Translate için gerekli)
   - Çok uzun promptlar çeviri sorunlarına neden olabilir

4. **CPU'da yavaş üretim**
   - Daha hızlı işleme için GPU kullanmayı düşünün
   - Daha hızlı sonuçlar için kalite ayarlarını düşürün

## 📊 Performans İpuçları

- Önemli ölçüde daha hızlı üretim için GPU kullanın
- Daha hızlı sonuçlar için çıkarım adımlarını azaltın
- Verimlilik için birden fazla görseli toplu olarak işleyin
- Bellek optimizasyonu için dikkat dilimlemeyi etkinleştirin

## 🔄 Sürüm Geçmişi

- **v1.0.0**: İlk sürüm
  - Temel metin-görsel üretimi
  - Türkçe dil desteği
  - Streamlit arayüzü

## 🌟 Teşekkürler

- [Stability AI](https://stability.ai/) - Stable Diffusion için
- [Hugging Face](https://huggingface.co/) - Diffusers kütüphanesi için
- [Streamlit](https://streamlit.io/) - Web çerçevesi için

## 📞 Destek

Herhangi bir sorunla karşılaşırsanız veya sorularınız varsa:
- GitHub'da bir issue açın
- Yukarıdaki sorun giderme bölümünü kontrol edin
- Dokümantasyonu inceleyin

---

⭐ **Bu projeyi faydalı bulduysanız, lütfen yıldız vermeyi unutmayın!**
## 👉 Örnek Kullanım
![WhatsApp Görsel 2025-07-13 saat 18 20 53_05fc7b63](https://github.com/user-attachments/assets/4ccd11bd-faae-4cfb-a0d7-e49c2aea6322)
