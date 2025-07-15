import streamlit as st
from generate import StableDiffusionGenerator
import os

# Sayfa yapılandırması
st.set_page_config(
    page_title="Metinden Görsel Üret", 
    page_icon="🖼️",
    layout="centered"
)

# Başlık
st.title("🖼️ Metinden Görsel Üretici")
st.write("Türkçe veya İngilizce metin girin, yapay zeka sizin için görsel üretsin!")

# Session state'de generator'ı sakla
if 'generator' not in st.session_state:
    st.session_state.generator = None

# Sidebar - Ayarlar
with st.sidebar:
    st.header("⚙️ Ayarlar")
    
    # Temel ayarlar
    quality = st.select_slider(
        "Kalite",
        options=["Hızlı", "Orta", "Yüksek"],
        value="Orta"
    )
    
    # Kalite ayarlarını map et
    quality_map = {
        "Hızlı": {"steps": 15, "scale": 6.0},
        "Orta": {"steps": 20, "scale": 7.5},
        "Yüksek": {"steps": 30, "scale": 9.0}
    }
    
    # Görsel sayısı
    image_count = st.selectbox("Görsel Sayısı", [1, 2, 3, 4], index=0)
    
    # Negatif prompt
    with st.expander("Gelişmiş Ayarlar"):
        negative_prompt = st.text_area(
            "İstenmeyen Özellikler",
            "blurry, low quality, distorted, ugly"
        )

# Ana alan
col1, col2 = st.columns([3, 1])

with col1:
    prompt = st.text_input(
        "🎯 Metin Açıklaması:", 
        placeholder="Örn: gün batımında sahil, mavi gökyüzünde uçan kedi"
    )

with col2:
    st.write("")
    st.write("")
    generate_btn = st.button("🚀 Üret", type="primary", use_container_width=True)

# Görsel üretme
if generate_btn and prompt:
    # Generator'ı başlat
    if st.session_state.generator is None:
        with st.spinner("Model yükleniyor... (İlk kullanımda biraz zaman alabilir)"):
            st.session_state.generator = StableDiffusionGenerator()
    
    # Ayarları al
    settings = quality_map[quality]
    
    # Görsel üret
    with st.spinner(f"Görsel{'ler' if image_count > 1 else ''} üretiliyor..."):
        try:
            if image_count == 1:
                # Tek görsel
                image_path = st.session_state.generator.generate_image(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    num_inference_steps=settings["steps"],
                    guidance_scale=settings["scale"]
                )
                
                if image_path:
                    st.success("✅ Görsel başarıyla üretildi!")
                    st.image(image_path, caption=f"Prompt: {prompt}", use_container_width=True)
                    
                    # İndir butonu
                    with open(image_path, "rb") as file:
                        st.download_button(
                            label="📥 İndir",
                            data=file.read(),
                            file_name=os.path.basename(image_path),
                            mime="image/png"
                        )
                else:
                    st.error("❌ Görsel üretilirken hata oluştu!")
            
            else:
                # Çoklu görsel
                image_paths = st.session_state.generator.generate_multiple_images(
                    prompt=prompt,
                    count=image_count,
                    negative_prompt=negative_prompt,
                    num_inference_steps=settings["steps"],
                    guidance_scale=settings["scale"]
                )
                
                if image_paths:
                    st.success(f"✅ {len(image_paths)} görsel başarıyla üretildi!")
                    
                    # Grid layout
                    cols = st.columns(2)
                    for i, image_path in enumerate(image_paths):
                        with cols[i % 2]:
                            st.image(image_path, caption=f"Varyasyon {i+1}", use_container_width=True)
                            
                            # Her görsel için indir butonu
                            with open(image_path, "rb") as file:
                                st.download_button(
                                    label=f"📥 İndir {i+1}",
                                    data=file.read(),
                                    file_name=os.path.basename(image_path),
                                    mime="image/png",
                                    key=f"download_{i}"
                                )
                else:
                    st.error("❌ Görseller üretilirken hata oluştu!")
                    
        except Exception as e:
            st.error(f"❌ Hata: {str(e)}")

elif generate_btn and not prompt:
    st.warning("⚠️ Lütfen bir metin açıklaması girin!")

# Alt bilgi
st.divider()
st.caption("💡 İpucu: Daha detaylı açıklamalar daha iyi sonuçlar verir. Örnek: 'kedi' yerine 'fluffy orange cat sitting on a windowsill'")

# Örnek promptlar
with st.expander("🎨 Örnek Promptlar"):
    example_prompts = [
        "gün batımında sahil manzarası",
        "kar yağan dağda ahşap kulübe",
        "uzayda yüzen renkli kediler",
        "cyberpunk tarzı neon şehir",
        "fantastik orman ile peri ışıkları",
        "Van Gogh tarzında ayçiçeği tarlası"
    ]
    
    for example in example_prompts:
        if st.button(example, key=f"example_{example}"):
            st.rerun()