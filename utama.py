# ==========================
# FILE DATA
# ==========================
file_data = "data_bakery.bites.csv"

if not os.path.exists(file_data):
    st.error(f"❌ File '{file_data}' tidak ditemukan!")
    st.stop()

# Membaca CSV (sep=None dan engine='python' otomatis mendeteksi jika pemisahnya koma atau titik koma)
df = pd.read_csv(file_data, sep=None, engine='python')

# Bersihkan spasi gaib di nama kolom dan ubah jadi huruf kecil semua
df.columns = df.columns.str.strip().str.lower()

# Validasi apakah kolom 'kategori' beneran ada setelah dibersihkan
if "kategori" not in df.columns:
    st.error("❌ Kolom 'kategori' tetap tidak ditemukan! Periksa kembali baris pertama file CSV kamu.")
    st.info("Solusi: Pastikan baris pertama di file data_bakery.bites.csv kamu bertuliskan: kategori,nama,harga,status,foto")
    st.stop()

kategori_list = df["kategori"].unique()
