import streamlit as st
import pandas as pd
import os

# ==========================
# KONFIGURASI WEBSITE
# ==========================
st.set_page_config(
    page_title="Bakery Bites 🍓🥐",
    page_icon="🥐",
    layout="wide"
)

# ==========================
# STYLE / BACKGROUND & CARD DESIGN
# ==========================
st.markdown("""
<style>
/* Background Utama */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fff5f5, #fff8f0, #fff0f5);
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

h1 {
    text-align: center;
    color: #d63384;
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Mengatur container kolom bawaan agar fleksibel */
div[data-testid="column"] {
    background: none !important;
    padding: 0px !important;
    box-shadow: none !important;
    border: none !important;
}

/* Desain Card Produk yang Rapi & Sejajar */
.bakery-card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.05);
    border: 1px solid #ffe4e1;
    text-align: center;
    margin-bottom: 25px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.product-title {
    font-size: 20px;
    font-weight: bold;
    color: #333333;
    margin-top: 15px;
    margin-bottom: 8px;
    min-height: 50px; /* Menjaga tinggi nama produk tetap sejajar */
}

.product-price {
    font-size: 22px;
    color: #d63384;
    font-weight: bold;
    margin-bottom: 12px;
}

.status-badge {
    background-color: #e8f5e9;
    color: #2e7d32;
    padding: 5px 12px;
    border-radius: 15px;
    font-size: 13px;
    font-weight: bold;
    display: inline-block;
    margin-bottom: 15px;
}

.error-badge {
    background-color: #ffebee;
    color: #c62828;
    padding: 8px;
    border-radius: 10px;
    font-size: 12px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# JUDUL
# ==========================
st.title("🍰 bakery.bites")
st.markdown(
    "<p style='text-align:center;font-size:18px;color:#6c757d;margin-bottom:20px;'>"
    "Premium Strawberry Treats Baked Fresh Daily ✨"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ==========================
# FILE DATA
# ==========================
file_data = "data_bakery.bites.csv"

if not os.path.exists(file_data):
    st.error(f"❌ File '{file_data}' tidak ditemukan!")
    st.stop()

# Membaca data dan membersihkan spasi nama kolom
df = pd.read_csv(file_data, sep=None, engine='python')
df.columns = df.columns.str.strip().str.lower()

kategori_list = df["kategori"].unique()

# ==========================
# DISPLAY PRODUK (GRID SYSTEM)
# ==========================
for kat in kategori_list:

    st.markdown(f"### 🍓 Menu Kategori: {kat.title()}")
    
    data_kat = df[df["kategori"] == kat].reset_index(drop=True)
    
    # Membuat grid 3 kolom
    for i in range(0, len(data_kat), 3):
        chunk = data_kat.iloc[i:i+3]
        cols = st.columns(3)
        
        for idx, row in chunk.iterrows():
            col_index = idx % 3
            with cols[col_index]:
                
                # Membuka pembungkus Card Custom
                st.markdown('<div class="bakery-card">', unsafe_allow_html=True)
                
                # 1. Pengecekan & Tampilan Foto
                nama_foto = str(row["foto"]).strip()
                path_foto = os.path.join(os.path.dirname(__file__), nama_foto)
                
                if os.path.exists(path_foto):
                    st.image(path_foto, use_container_width=True)
                else:
                    # Menampilkan pesan error rapi di dalam card jika file gambarnya salah/hilang
                    st.markdown(f'<div class="error-badge">📸 Gambar tidak ditemukan:<br><b>{nama_foto}</b></div>', unsafe_allow_html=True)
                
                # 2. Detail Konten Produk
                st.markdown(f'<div class="product-title">{str(row["nama"]).title()}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-price">Rp {row["harga"]:,}</div>', unsafe_allow_html=True)
                st.markdown(f'<span class="status-badge">● {row["status"]}</span>', unsafe_allow_html=True)
                
                # 3. Tombol Order Streamlit
                if st.button(f"🛒 Order Sekarang", key=f"btn_{row['nama']}_{idx}"):
                    st.success(f"🧁 {row['nama']} masuk keranjang!")
                
                # Menutup pembungkus Card Custom
                st.markdown('</div>', unsafe_allow_html=True)
                
    st.divider()

# ==========================
# FOOTER
# ==========================
st.subheader("📍 Lokasi & Pemesanan")

col1, col2 = st.columns(2)

with col1:
    st.info("""
🏪 **bakery.bites Central Kitchen**

Jl. Strawberry Manis No. 12  
Kota Bakery, Indonesia 🇮🇩
""")

with col2:
    no_hp = "6285869485201"
    pesan = "Halo bakery.bites! Saya mau pesan menu strawberry-nya dong 🍓"
    link = f"https://wa.me/{no_hp}?text={pesan.replace(' ','%20')}"

    st.link_button("📱 Hubungi via WhatsApp", link)

st.caption("© 2026 bakery.bites — Freshly Baked with Love 🍓✨")
