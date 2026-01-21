import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SIM Perpustakaan", layout="wide")

# --- INISIALISASI SESSION STATE (DATABASE SEMENTARA) ---
# Dalam aplikasi nyata, ini diganti dengan koneksi ke Database (MySQL/PostgreSQL)
if 'init' not in st.session_state:
    st.session_state.init = True
    
    # Data Awal
    st.session_state.users = pd.DataFrame([
        {'nama': 'Muhammad Itsna Ali Tiyas Bahari', 'password': 'Ali16052000', 'role': 'Administrator', 'id': 'ADMIN001'}
    ])
    
    st.session_state.books = pd.DataFrame(columns=[
        'ISBN', 'Judul', 'Kategori', 'Penulis', 'Penerbit', 'Tahun', 'Stok', 'Lokasi', 'PDF_File'
    ])
    
    st.session_state.members = pd.DataFrame(columns=[
        'Nama', 'Role', 'Status', 'NIS', 'Kelas', 'No_Telp', 'Email', 'Alamat', 'Foto'
    ])
    
    st.session_state.peminjaman = pd.DataFrame(columns=[
        'ID_Transaksi', 'ID_Anggota', 'ISBN', 'Judul', 'Tgl_Pinjam', 'Tgl_Jatuh_Tempo', 'Status', 'Denda'
    ])
    
    st.session_state.kunjungan = pd.DataFrame(columns=[
        'Tanggal', 'Jam', 'ID_Anggota', 'Nama', 'Tujuan'
    ])
    
    st.session_state.keuangan = pd.DataFrame(columns=[
        'Tanggal', 'Jenis', 'Keterangan', 'Jumlah'
    ])
    
    st.session_state.settings = {
        'sekolah': 'SMK Harapan Bangsa',
        'kepala': 'Drs. H. Ahmad',
        'alamat': 'Jl. Pendidikan No. 1',
        'denda_per_hari': 1000,
        'logo': None,
        'bg_image': None
    }

# --- FUNGSI BANTUAN ---
def get_time():
    now = datetime.now()
    return now.strftime("%A, %d %B %Y - %H:%M:%S")

def hitung_jatuh_tempo(hari_pinjam=3):
    # Logika sederhana menghindari Sabtu/Minggu (Tanggal Merah dinamis butuh API libur nasional)
    tgl = datetime.now()
    count = 0
    while count < hari_pinjam:
        tgl += timedelta(days=1)
        if tgl.weekday() < 5: # 0-4 adalah Senin-Jumat
            count += 1
    return tgl.date()

def set_bg(image_file):
    # Fungsi CSS untuk Background Custom
    if image_file:
        encoded_string = base64.b64encode(image_file.getvalue()).decode()
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
        )

# --- LOGIN SYSTEM (Fitur 1) ---
def login_page():
    st.title("🔐 Login SIM Perpustakaan")
    
    with st.form("login_form"):
        username = st.text_input("Nama Lengkap")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Masuk")
        
        if submitted:
            # Cek Admin Hardcoded
            if username == "Muhammad Itsna Ali Tiyas Bahari" and password == "Ali16052000":
                st.session_state['logged_in'] = True
                st.session_state['user_role'] = 'Administrator'
                st.session_state['username'] = username
                st.rerun()
            
            # Cek Anggota Biasa (Simulasi login sederhana berdasarkan NIS)
            member = st.session_state.members[st.session_state.members['Nama'] == username]
            if not member.empty and password == member.iloc[0]['NIS']: # Password anggota = NIS
                st.session_state['logged_in'] = True
                st.session_state['user_role'] = 'Anggota'
                st.session_state['username'] = username
                st.rerun()
            elif username != "" and password != "":
                st.error("Nama atau Password salah.")

# --- MAIN APPLICATION ---
def main_app():
    # Fitur 11 & 12: Waktu & Setting Background
    if st.session_state.settings['bg_image']:
        set_bg(st.session_state.settings['bg_image'])

    # Header Info Sekolah
    col_h1, col_h2 = st.columns([1, 5])
    with col_h1:
        st.info("Logo") # Placeholder Logo
    with col_h2:
        st.title(f"Perpustakaan {st.session_state.settings['sekolah']}")
        st.write(f"{st.session_state.settings['alamat']} | {get_time()}")

    # Sidebar Menu
    st.sidebar.title(f"Hai, {st.session_state['username']}")
    st.sidebar.caption(f"Role: {st.session_state['user_role']}")
    
    if st.session_state['user_role'] == 'Administrator':
        menu = st.sidebar.radio("Menu Utama", 
            ["Dashboard", "Data Buku", "Data Anggota", "Peminjaman", "Pengembalian", 
             "Kunjungan", "Riwayat & Laporan", "Keuangan", "Pengaturan"])
    else:
        menu = st.sidebar.radio("Menu Anggota", ["Dashboard", "Cari & Baca Buku", "Riwayat Saya"])

    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    # --- LOGIKA MENU ADMINISTRATOR ---
    
    # 1. DASHBOARD (Fitur 2)
    if menu == "Dashboard":
        st.header("📊 Dashboard Statistik")
        
        # Statistik Utama
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Buku", len(st.session_state.books))
        col2.metric("Total Anggota", len(st.session_state.members))
        sedang_pinjam = len(st.session_state.peminjaman[st.session_state.peminjaman['Status']=='Dipinjam'])
        col3.metric("Sedang Dipinjam", sedang_pinjam)
        
        # Hitung Kunjungan Hari Ini
        today_str = datetime.now().strftime("%Y-%m-%d")
        kunjungan_hari_ini = len(st.session_state.kunjungan[st.session_state.kunjungan['Tanggal'].astype(str) == today_str])
        col4.metric("Kunjungan Hari Ini", kunjungan_hari_ini)
        
        st.subheader("Buku Terpopuler")
        if not st.session_state.peminjaman.empty:
            populer = st.session_state.peminjaman['Judul'].value_counts().head(5)
            st.bar_chart(populer)
        else:
            st.info("Belum ada data peminjaman.")

    # 2. DATA BUKU (Fitur 3)
    elif menu == "Data Buku":
        st.header("📚 Manajemen Data Buku")
        
        tab1, tab2 = st.tabs(["Tambah Buku", "Daftar Buku & Cetak Barcode"])
        
        with tab1:
            with st.form("tambah_buku"):
                col_a, col_b = st.columns(2)
                isbn = col_a.text_input("ISBN")
                judul = col_b.text_input("Judul Buku")
                kategori = col_a.selectbox("Kategori", ["Umum", "Sains", "Sosial", "Agama", "Fiksi"])
                penulis = col_b.text_input("Penulis")
                penerbit = col_a.text_input("Penerbit")
                tahun = col_b.number_input("Tahun Terbit", 1900, 2099, 2023)
                stok = col_a.number_input("Jumlah Stok", 1, 1000, 10)
                lokasi = col_b.text_input("Lokasi Rak")
                pdf_file = st.file_uploader("Upload PDF (E-Book)", type=['pdf'])
                
                if st.form_submit_button("Simpan Buku"):
                    new_book = {
                        'ISBN': isbn, 'Judul': judul, 'Kategori': kategori, 
                        'Penulis': penulis, 'Penerbit': penerbit, 'Tahun': tahun, 
                        'Stok': stok, 'Lokasi': lokasi, 'PDF_File': pdf_file
                    }
                    st.session_state.books = pd.concat([st.session_state.books, pd.DataFrame([new_book])], ignore_index=True)
                    st.success("Buku berhasil ditambahkan!")
        
        with tab2:
            st.dataframe(st.session_state.books)
            st.info("Fitur Cetak Barcode: Pilih buku di atas (Simulasi: Barcode dihasilkan berdasarkan ISBN)")
            # Simulasi Cetak Barcode
            buku_pilih = st.selectbox("Pilih Buku untuk Barcode", st.session_state.books['Judul'].unique() if not st.session_state.books.empty else [])
            if buku_pilih:
                jml_cetak = st.number_input("Jumlah Barcode", 1, 100)
                if st.button("Generate Barcode"):
                    st.write(f"Mencetak {jml_cetak} barcode untuk: {buku_pilih}")
                    st.code(f"||| {buku_pilih} |||", language="text") # Visualisasi sederhana

    # 3. DATA ANGGOTA (Fitur 4)
    elif menu == "Data Anggota":
        st.header("👥 Manajemen Anggota")
        
        tab1, tab2 = st.tabs(["Tambah Anggota", "Daftar & Cetak Kartu"])
        
        with tab1:
            with st.form("tambah_anggota"):
                nama = st.text_input("Nama Lengkap")
                role = st.selectbox("Role", ["Siswa", "Guru", "Staff"])
                status = st.selectbox("Status", ["Aktif", "Tidak Aktif"])
                nis = st.text_input("NIS/NIP")
                kelas = st.text_input("Kelas/Jabatan")
                no_telp = st.text_input("No Telepon")
                email = st.text_input("Email")
                alamat = st.text_area("Alamat")
                
                if st.form_submit_button("Simpan Anggota"):
                    new_member = {
                        'Nama': nama, 'Role': role, 'Status': status, 'NIS': nis,
                        'Kelas': kelas, 'No_Telp': no_telp, 'Email': email, 'Alamat': alamat, 'Foto': None
                    }
                    st.session_state.members = pd.concat([st.session_state.members, pd.DataFrame([new_member])], ignore_index=True)
                    st.success("Anggota berhasil ditambahkan!")

        with tab2:
            st.dataframe(st.session_state.members)
            
            # Fitur Cetak Kartu
            st.subheader("Cetak Kartu Anggota")
            pilih_anggota = st.selectbox("Pilih Anggota", st.session_state.members['Nama'].unique() if not st.session_state.members.empty else [])
            if st.button("Cetak Kartu") and pilih_anggota:
                data_a = st.session_state.members[st.session_state.members['Nama'] == pilih_anggota].iloc[0]
                # Visualisasi Kartu
                st.markdown(f"""
                <div style="border: 2px solid #333; padding: 20px; width: 400px; border-radius: 10px; background-color: #f9f9f9; color: black;">
                    <h3>KARTU PERPUSTAKAAN</h3>
                    <p><b>Nama:</b> {data_a['Nama']}</p>
                    <p><b>NIS:</b> {data_a['NIS']}</p>
                    <p><b>Kelas:</b> {data_a['Kelas']}</p>
                    <div style="background-color: black; color: white; padding: 5px; text-align: center; margin-top: 10px;">
                    ||||||| {data_a['NIS']} |||||||
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # 4. PEMINJAMAN (Fitur 5)
    elif menu == "Peminjaman":
        st.header("📖 Transaksi Peminjaman")
        
        col1, col2 = st.columns(2)
        with col1:
            id_anggota = st.text_input("Scan/Input NIS Anggota")
        with col2:
            # Cari buku otomatis
            buku_opsi = st.session_state.books['Judul'].tolist() if not st.session_state.books.empty else []
            buku_pinjam = st.selectbox("Cari Buku (Scan Barcode/Judul)", buku_opsi)
        
        jatuh_tempo = hitung_jatuh_tempo(3) # Otomatis hitung hari kerja
        st.write(f"Tanggal Jatuh Tempo: **{jatuh_tempo}** (Otomatis hari kerja)")
        
        if st.button("Proses Peminjaman"):
            if id_anggota and buku_pinjam:
                transaksi = {
                    'ID_Transaksi': f"TRX-{int(time.time())}",
                    'ID_Anggota': id_anggota,
                    'ISBN': 'AUTO', # Simplifikasi
                    'Judul': buku_pinjam,
                    'Tgl_Pinjam': datetime.now().date(),
                    'Tgl_Jatuh_Tempo': jatuh_tempo,
                    'Status': 'Dipinjam',
                    'Denda': 0
                }
                st.session_state.peminjaman = pd.concat([st.session_state.peminjaman, pd.DataFrame([transaksi])], ignore_index=True)
                st.success("Peminjaman Berhasil!")
            else:
                st.error("Data belum lengkap.")
        
        st.subheader("Daftar Peminjaman Aktif")
        active = st.session_state.peminjaman[st.session_state.peminjaman['Status'] == 'Dipinjam']
        st.dataframe(active)

    # 5. PENGEMBALIAN (Fitur 6)
    elif menu == "Pengembalian":
        st.header("↩️ Pengembalian Buku")
        
        cari_kembali = st.text_input("Cari Buku/NIS untuk Pengembalian")
        
        if cari_kembali:
            hasil = st.session_state.peminjaman[
                (st.session_state.peminjaman['Status'] == 'Dipinjam') & 
                (st.session_state.peminjaman['Judul'].str.contains(cari_kembali) | 
                 st.session_state.peminjaman['ID_Anggota'].str.contains(cari_kembali))
            ]
            
            if not hasil.empty:
                trx = hasil.iloc[0]
                st.write(f"Ditemukan: **{trx['Judul']}** dipinjam oleh **{trx['ID_Anggota']}**")
                
                # Cek Keterlambatan
                hari_ini = datetime.now().date()
                tempo = trx['Tgl_Jatuh_Tempo']
                # Konversi tempo jika formatnya string (tergantung pandas)
                if isinstance(tempo, str):
                    tempo = datetime.strptime(tempo, "%Y-%m-%d").date()
                    
                selisih = (hari_ini - tempo).days
                denda = 0
                if selisih > 0:
                    denda = selisih * st.session_state.settings['denda_per_hari']
                    st.warning(f"⚠️ Terlambat {selisih} hari. Denda: Rp {denda}")
                else:
                    st.success("Tepat Waktu.")
                
                if st.button("Proses Pengembalian"):
                    idx = hasil.index[0]
                    st.session_state.peminjaman.at[idx, 'Status'] = 'Kembali'
                    st.session_state.peminjaman.at[idx, 'Denda'] = denda
                    
                    # Catat Pemasukan Denda jika ada
                    if denda > 0:
                        keu = {'Tanggal': hari_ini, 'Jenis': 'Pemasukan', 'Keterangan': 'Denda Keterlambatan', 'Jumlah': denda}
                        st.session_state.keuangan = pd.concat([st.session_state.keuangan, pd.DataFrame([keu])], ignore_index=True)
                        
                    st.success("Buku berhasil dikembalikan!")
            else:
                st.warning("Data peminjaman tidak ditemukan.")

    # 6. KUNJUNGAN (Fitur 7)
    elif menu == "Kunjungan":
        st.header("🏃 Buku Tamu Kunjungan")
        
        with st.form("form_kunjungan"):
            id_pengunjung = st.text_input("Scan Kartu / ID Anggota / Nama")
            tujuan = st.selectbox("Tujuan Kunjungan", ["Membaca", "Meminjam Buku", "Mengembalikan Buku", "Lainnya (Custom)"])
            tujuan_custom = st.text_input("Jika Lainnya, isi disini:")
            
            if st.form_submit_button("Catat Kunjungan"):
                final_tujuan = tujuan_custom if tujuan == "Lainnya (Custom)" else tujuan
                visit = {
                    'Tanggal': datetime.now().date(),
                    'Jam': datetime.now().strftime("%H:%M"),
                    'ID_Anggota': id_pengunjung,
                    'Nama': id_pengunjung, # Sebaiknya lookup nama dari ID
                    'Tujuan': final_tujuan
                }
                st.session_state.kunjungan = pd.concat([st.session_state.kunjungan, pd.DataFrame([visit])], ignore_index=True)
                st.success(f"Selamat datang, {id_pengunjung}!")

        st.subheader("Kunjungan Hari Ini")
        today = datetime.now().date()
        df_visit = st.session_state.kunjungan
        if not df_visit.empty:
            df_today = df_visit[df_visit['Tanggal'].astype(str) == str(today)]
            st.dataframe(df_today)

    # 7. RIWAYAT & LAPORAN (Fitur 8 & 9)
    elif menu == "Riwayat & Laporan":
        st.header("📈 Laporan & Riwayat")
        
        tab_riwayat, tab_laporan = st.tabs(["Riwayat Transaksi", "Laporan & Export"])
        
        with tab_riwayat:
            st.subheader("Riwayat Peminjaman & Pengembalian")
            st.dataframe(st.session_state.peminjaman)
            st.subheader("Riwayat Kunjungan")
            st.dataframe(st.session_state.kunjungan)
            
        with tab_laporan:
            st.write("Pilih Periode Laporan (Simulasi Filter)")
            col_d1, col_d2 = st.columns(2)
            start_date = col_d1.date_input("Dari Tanggal")
            end_date = col_d2.date_input("Sampai Tanggal")
            
            # Export CSV
            if st.button("Export Laporan ke CSV"):
                csv = st.session_state.peminjaman.to_csv(index=False).encode('utf-8')
                st.download_button("Download Data Peminjaman", csv, "laporan_peminjaman.csv", "text/csv")
            
            # Statistik Anggota Aktif
            st.subheader("Anggota Paling Aktif (Top 3)")
            if not st.session_state.kunjungan.empty:
                top_visit = st.session_state.kunjungan['ID_Anggota'].value_counts().head(3)
                st.write("Berdasarkan Kunjungan:", top_visit)

    # 8. KEUANGAN (Fitur 10)
    elif menu == "Keuangan":
        st.header("💰 Manajemen Keuangan")
        
        col_in, col_out = st.columns(2)
        
        with col_in:
            st.subheader("Catat Pemasukan")
            sumber = st.selectbox("Sumber", ["Denda Keterlambatan", "Denda Hilang/Rusak", "Sumbangan", "Lainnya"])
            jml_masuk = st.number_input("Jumlah (Rp)", min_value=0)
            ket_masuk = st.text_input("Keterangan Masuk")
            if st.button("Simpan Pemasukan"):
                trx_uang = {'Tanggal': datetime.now().date(), 'Jenis': 'Pemasukan', 'Keterangan': f"{sumber} - {ket_masuk}", 'Jumlah': jml_masuk}
                st.session_state.keuangan = pd.concat([st.session_state.keuangan, pd.DataFrame([trx_uang])], ignore_index=True)
                st.success("Tersimpan")

        with col_out:
            st.subheader("Catat Pengeluaran")
            jml_keluar = st.number_input("Jumlah Keluar (Rp)", min_value=0)
            ket_keluar = st.text_input("Keterangan Pengeluaran")
            if st.button("Simpan Pengeluaran"):
                trx_uang = {'Tanggal': datetime.now().date(), 'Jenis': 'Pengeluaran', 'Keterangan': ket_keluar, 'Jumlah': jml_keluar}
                st.session_state.keuangan = pd.concat([st.session_state.keuangan, pd.DataFrame([trx_uang])], ignore_index=True)
                st.success("Tersimpan")
        
        st.divider()
        st.subheader("Laporan Keuangan")
        st.dataframe(st.session_state.keuangan)
        
        # Hitung Saldo
        if not st.session_state.keuangan.empty:
            masuk = st.session_state.keuangan[st.session_state.keuangan['Jenis']=='Pemasukan']['Jumlah'].sum()
            keluar = st.session_state.keuangan[st.session_state.keuangan['Jenis']=='Pengeluaran']['Jumlah'].sum()
            st.metric("Total Saldo Kas", f"Rp {masuk - keluar:,.0f}")

    # 9. PENGATURAN (Fitur 12)
    elif menu == "Pengaturan":
        st.header("⚙️ Pengaturan Sistem")
        
        with st.form("settings_form"):
            st.subheader("Identitas Sekolah")
            sekolah = st.text_input("Nama Sekolah", st.session_state.settings['sekolah'])
            kepala = st.text_input("Kepala Sekolah", st.session_state.settings['kepala'])
            alamat = st.text_area("Alamat", st.session_state.settings['alamat'])
            
            st.subheader("Aturan Perpustakaan")
            denda = st.number_input("Denda per Hari (Rp)", value=st.session_state.settings['denda_per_hari'])
            
            st.subheader("Tampilan")
            bg_file = st.file_uploader("Upload Background (JPG)", type=['jpg', 'jpeg', 'png'])
            
            if st.form_submit_button("Simpan Pengaturan"):
                st.session_state.settings['sekolah'] = sekolah
                st.session_state.settings['kepala'] = kepala
                st.session_state.settings['alamat'] = alamat
                st.session_state.settings['denda_per_hari'] = denda
                if bg_file:
                    st.session_state.settings['bg_image'] = bg_file
                st.success("Pengaturan Disimpan!")
                st.rerun()

    # --- LOGIKA MENU ANGGOTA (Akses Terbatas) ---
    elif menu == "Cari & Baca Buku" or menu == "Dashboard": # Dashboard anggota disamakan
        st.header("📚 Katalog Buku Digital")
        
        search = st.text_input("Cari Buku...")
        df_books = st.session_state.books
        
        if search:
            df_books = df_books[df_books['Judul'].str.contains(search, case=False)]
        
        if not df_books.empty:
            for index, row in df_books.iterrows():
                with st.expander(f"{row['Judul']} - {row['Penulis']}"):
                    st.write(f"**Penerbit:** {row['Penerbit']} ({row['Tahun']})")
                    st.write(f"**Rak:** {row['Lokasi']}")
                    st.write(f"**Stok:** {row['Stok']}")
                    
                    # Fitur 13: Akses Baca Buku (E-Book)
                    if row['PDF_File']:
                        st.download_button("📖 Download/Baca PDF", row['PDF_File'], file_name=f"{row['Judul']}.pdf")
                    else:
                        st.caption("Versi digital belum tersedia.")
        else:
            st.info("Buku tidak ditemukan.")

    elif menu == "Riwayat Saya":
        st.header("Riwayat Peminjaman Saya")
        # Filter berdasarkan username yang sedang login
        my_history = st.session_state.peminjaman[st.session_state.peminjaman['Judul'] == 'dummy'] # Placeholder filter
        # Dalam implementasi nyata, filter menggunakan ID Anggota yang login
        st.info("Fitur ini menampilkan riwayat khusus akun yang sedang login.")


# --- ROUTING HALAMAN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login_page()
else:
    main_app()
