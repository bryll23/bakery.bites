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
# STYLE / BACKGROUND
# ==========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#fff5f5,
#fff8f0,
#fff0f5
);
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

h1{
text-align:center;
color:#d63384;
font-size:55px;
}

div[data-testid="column"]{
background:white;
padding:20px;
border-radius:25px;
box-shadow:0px 8px 20px rgba(0,0,0,0.06);
border: 1px solid #ffe4e1;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# JUDUL
# ==========================
st.title("🍰 bakery.bites")
st.markdown(
    "<p style='text-align:center;font-size:18px;color:#6c757d;'>"
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

df = pd.read_csv(file_data)

kategori_list = df["kategori"].unique()

# ==========================
# PRODUK
# ==========================
for kat in kategori_list:

    st.header(f"🍓 Menu Kategori: {kat.title()}")

    data_kat = df[df["kategori"] == kat]
    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():

        with cols[index % 3]:

            # ==========================
            # FOTO
            # ==========================
            nama_foto = os.path.join(
                os.path.dirname(__file__),
                str(row["foto"]).strip()
            )

            if os.path.exists(nama_foto):
                st.image(nama_foto, use_container_width=True)
            else:
                st.caption(f"📸 Foto tidak ditemukan: {row['foto']}")

            # ==========================
            # NAMA PRODUK
            # ==========================
            st.subheader(str(row["nama"]).title())

            # ==========================
            # HARGA
            # ==========================
            st.markdown(f"### 💸 Rp {row['harga']:,}")

            # ==========================
            # STATUS
            # ==========================
            st.success(f"Status: {row['status']}")

            # ==========================
            # BUTTON
            # ==========================
            if st.button(
                f"🛒 Order {row['nama']}",
                key=f"order_{kat}_{index}"
            ):
                st.success(f"🧁 {row['nama']} berhasil ditambahkan ke keranjang!")

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
    no_hp = "62895400551222"
    pesan = "Halo bakery.bites! Saya mau pesan menu strawberry-nya dong 🍓"
    link = f"https://wa.me/{no_hp}?text={pesan.replace(' ','%20')}"

    st.link_button("📱 Pesan WhatsApp", link)

st.caption("© 2026 bakery.bites — Freshly Baked with Love 🍓✨")
