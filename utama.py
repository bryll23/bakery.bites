import streamlit as st
import pandas as pd
import os

# ==========================
# KONFIGURASI WEBSITE
# ==========================
st.set_page_config(
    page_title="Bakery Bites | Premium Strawberry Treats 🍓",
    page_icon="🍓",
    layout="wide"
)

# ==========================
# STYLE / CSS CUSTOM (AESTHETIC)
# ==========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,400&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

/* Background Utama */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fff6f6 0%, #fffbf7 50%, #f9f0f5 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Judul Utama */
.main-title {
    font-family: 'Playfair Display', serif;
    text-align: center;
    color: #bc4749;
    font-size: 58px;
    font-weight: 600;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #6c757d;
    font-style: italic;
    margin-bottom: 30px;
}

/* Kategori Header */
.category-header {
    font-family: 'Playfair Display', serif;
    color: #3a506b;
    font-size: 28px;
    border-bottom: 2px solid #f3d5d8;
    padding-bottom: 8px;
    margin-top: 40px;
    margin-bottom: 25px;
}

/* Kartu Produk (Card) */
div[data-testid="column"] {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(188, 71, 73, 0.03);
    border: 1px solid rgba(243, 213, 216, 0.6);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

div[data-testid="column"]:hover {
    transform: translateY(-8px);
    box-shadow: 0px 15px 35px rgba(188, 71, 73, 0.08);
    border: 1px solid rgba(188, 71, 73, 0.3);
}

/* Nama & Harga Produk */
.product-name {
    font-family: 'Playfair Display', serif;
    color: #2b2d42;
    font-size: 22px;
    font-weight: 600;
    margin-top: 15px;
    margin-bottom: 8px;
    min-height: 60px; /* Menjaga tinggi card tetap sejajar */
}

.product-price {
    color: #bc4749;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 15px;
}

/* Badge Status */
.status-badge {
    background-color: #e8f5e9;
    color: #2e7d32;
    padding: 4px 12px;
    border-radius: 50px;
    font-size: 12px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 20px;
}

/* Custom Button */
.stButton > button {
    background-color: #bc4749 !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 10px 20px !important;
    width: 100% !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    background-color: #a7383a !important;
    box-shadow: 0px 5px 15px rgba(188, 71, 73, 0.3) !important;
}

/* Footer Info */
.footer-box {
    background: rgba(255, 255, 255, 0.7);
    padding: 25px;
    border-radius: 15px;
    border-left: 5px solid #bc4749;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER / HERO SECTION
# ==========================
st.markdown('<div class="main-title">bakery.bites</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Premium Strawberry Treats Baked Fresh Daily ✨</div>', unsafe_allow_html=True)

st.divider()

# ==========================
# LOAD DATA CSV
# ==========================
file_data = "data_bakery.bites.csv"

if not os.path.exists(file_data):
    st.error(f"❌ File '{file_data}' tidak ditemukan!")
    st.stop()

df = pd.read_csv(file_data)
kategori_list = df["kategori"].unique()

# ==========================
# LOOPING DISPLAY PRODUK
# ==========================
for kat in kategori_list:

    # Header Kategori Estetik
    st.markdown(f'<div class="category-header">🍓 {kat.title()}</div>', unsafe_allow_html=True)

    data_kat = df[df["kategori"] == kat]
    
    # Membuat grid 3 kolom
    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():
        with cols[index % 3]:

            # 1. Foto Produk dengan Sudut Tumpul
            nama_foto = os.path.join(os.path.dirname(__file__), str(row["foto"]).strip())
            if os.path.exists(nama_foto):
                st.image(nama_foto, use_container_width=True)
            else:
                st.caption(f"📸 Foto tidak ditemukan: {row['foto']}")

            # 2. Detail Produk via HTML (Agar font & layout rapi)
            st.markdown(f'<div class="product-name">{str(row["nama"]).title()}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-price">Rp {row["harga"]:,}</div>', unsafe_allow_html=True)
            st.markdown(f'<span class="status-badge">● {row["status"]}</span>', unsafe_allow_html=True)

            # 3. Tombol Order
            if st.button(
                f"🛒 Order Now",
                key=f"order_{kat}_{index}"
            ):
                st.toast(f"🧁 {row['nama'].title()} ditambahkan!", icon="🛒")
                st.success(f"Berhasil menambahkan ke keranjang!")

# ==========================
# FOOTER SECTION
# ==========================
st.markdown('<div class="category-header">📍 Lokasi & Pemesanan</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="footer-box">
        <h4 style="margin-top:0; color:#3a506b;">🏪 bakery.bites Central Kitchen</h4>
        <p style="color:#6c757d; margin-bottom:0;">
            Jl. Strawberry Manis No. 12<br>
            Kota Bakery, Indonesia 🇮🇩
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    no_hp = "62895400551222"
    pesan = "Halo bakery.bites! Saya mau pesan menu strawberry-nya dong 🍓"
    link = f"https://wa.me/{no_hp}?text={pesan.replace(' ','%20')}"
    
    st.write("") # Spacer jalur manual biar seimbang tinggi kotaknya
    st.link_button("📱 Hubungi via WhatsApp", link, use_container_width=True)

st.write("")
st.write("")
st.caption("<center style='color:#a7a7a7;'>© 2026 bakery.bites — Freshly Baked with Love 🍓✨</center>", unsafe_allow_html=True)
