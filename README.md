# Time Zone Converter App

Aplikasi **Time Zone Converter** ini dibuat menggunakan **Python** dan **Tkinter** untuk mengkonversi waktu dari satu zona waktu ke zona waktu lainnya. Dengan antarmuka pengguna yang sederhana, pengguna dapat memasukkan waktu, memilih zona waktu asal, serta zona waktu tujuan, dan aplikasi akan menampilkan waktu yang telah dikonversi secara langsung.

## Fitur
- Input waktu dalam format **YYYY-MM-DD HH:MM:SS**.
- Pilihan untuk memilih zona waktu asal dan zona waktu tujuan dari daftar lengkap zona waktu yang didukung oleh **pytz**.
- Tampilkan waktu yang telah dikonversi beserta nama zona waktu.

## Dependencies

- **Tkinter**: Untuk antarmuka grafis pengguna.
- **pytz**: Untuk menangani konversi zona waktu.

## Instalasi
1. Pastikan Anda telah menginstall Python versi 3.x di komputer Anda.
2. Clone repository ini dengan menjalankan perintah berikut:
   ```bash
   git clone https://github.com/Athallah1234/Time-Zone-Converter.git
   ```
4. Install modul yang dibutuhkan dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menggunakan

1. Jalankan skrip Python dengan perintah berikut:
   ```bash
   python run.py
   ```
3. Masukkan waktu yang ingin Anda konversi dalam format YYYY-MM-DD HH:MM
4. Pilih zona waktu asal dari daftar zona waktu.
5. Pilih zona waktu tujuan dari daftar zona waktu.
6. Klik tombol Convert dan waktu yang telah dikonversi akan ditampilkan.

## Contoh Penggunaan

Misalnya, jika Anda memasukkan waktu sebagai 2024-09-25 12:00:00, dan memilih zona waktu asal sebagai Asia/Jakarta serta zona waktu tujuan sebagai America/New_York, aplikasi ini akan menampilkan waktu yang telah dikonversi sesuai dengan zona waktu tujuan.

## Format Waktu

Aplikasi ini memerlukan input waktu dalam format **YYYY-MM-DD HH:MM:SS**. Jika format yang dimasukkan tidak sesuai atau salah, aplikasi akan menampilkan pesan kesalahan yang relevan.

Contoh format yang valid:
- **2024-09-25 14:30:00**

## Daftar Zona Waktu

Aplikasi ini mendukung semua zona waktu yang diakui secara internasional melalui pustaka **pytz**. Beberapa contoh zona waktu yang bisa dipilih:
- **Asia/Jakarta**
- **America/New_York**
- **Europe/London**
- **Australia/Sydney**
- **Africa/Cairo**

Pengguna bisa memilih zona waktu dari dua dropdown menu yang telah disediakan.

## Mengatasi Error

- **Kesalahan format waktu**: Jika format waktu tidak sesuai, aplikasi akan menampilkan pesan seperti **"Error: time data 'input' does not match format '%Y-%m-%d %H:%M:%S'"**. Pastikan format waktu yang dimasukkan sudah benar.
- **Zona waktu tidak valid**: Aplikasi otomatis memvalidasi zona waktu dari daftar **pytz**, jadi tidak akan ada kesalahan terkait zona waktu.

## Cara Berkontribusi
Kami menerima kontribusi dari siapa pun yang tertarik untuk membantu meningkatkan aplikasi ini. Berikut langkah-langkah untuk berkontribusi:

1. **Fork** repository ini.
2. Buat **branch** fitur baru (`git checkout -b feature-nama-fitur`).
3. Lakukan perubahan yang diperlukan dan tambahkan dokumentasi yang sesuai.
4. **Commit** perubahan Anda (`git commit -m 'Menambahkan fitur nama-fitur'`).
5. **Push** ke branch (`git push origin feature-nama-fitur`).
6. Buat **Pull Request** dan jelaskan secara detail perubahan yang telah Anda lakukan.

Kami akan meninjau kontribusi Anda dan memprosesnya sesegera mungkin!

## FAQ

**1. Apakah saya bisa menggunakan format waktu 12 jam (AM/PM)?**

Saat ini aplikasi hanya mendukung format 24 jam. Namun, kami sedang merencanakan penambahan dukungan untuk format 12 jam pada rilis mendatang.

**2. Bagaimana jika zona waktu yang saya pilih tidak ada?**

Aplikasi ini menggunakan pustaka **pytz** yang mencakup semua zona waktu internasional yang dikenal. Jika Anda tidak menemukan zona waktu tertentu, pastikan untuk memeriksa nama zona waktu yang tepat sesuai standar **pytz**.

**3. Apakah saya bisa menggunakan aplikasi ini di sistem operasi selain Windows?**

Ya, aplikasi ini berbasis **Tkinter** yang berjalan di semua sistem operasi utama termasuk **Windows**, **macOS**, dan **Linux**.

**4. Bagaimana jika saya menemukan bug?**

Jika Anda menemukan bug atau masalah dalam aplikasi, silakan buat **issue** di repository ini atau hubungi saya secara langsung melalui kontak yang disediakan.

## Testing
Untuk memastikan aplikasi berjalan dengan baik, berikut adalah beberapa skenario pengujian yang bisa dilakukan:

1. **Skenario Valid**:
   - Input: `2024-09-25 14:00:00`
   - Zona Waktu Asal: **Asia/Jakarta**
   - Zona Waktu Tujuan: **Europe/London**
   - Output: **2024-09-25 08:00:00 BST** (British Summer Time)
   
2. **Skenario Invalid**:
   - Input: `2024-09-25 14:00` (Format salah)
   - Output: **Error: time data '2024-09-25 14:00' does not match format '%Y-%m-%d %H:%M:%S'**

3. **Zona Waktu Sama**:
   - Input: `2024-09-25 14:00:00`
   - Zona Waktu Asal: **Asia/Jakarta**
   - Zona Waktu Tujuan: **Asia/Jakarta**
   - Output: **2024-09-25 14:00:00 WIB**

## Known Issues
- Aplikasi ini hanya mendukung format waktu **24 jam** dan **detik** harus diikutsertakan.
- Tidak ada validasi langsung untuk input yang belum diisi, jadi jika kolom kosong dan pengguna mencoba mengonversi, pesan kesalahan akan muncul.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan lakukan **fork** pada repository ini dan kirimkan **pull request** dengan penjelasan singkat tentang perubahan yang Anda buat.

## Kontak
Jika Anda memiliki pertanyaan atau saran mengenai aplikasi ini, jangan ragu untuk menghubungi saya di:
- **Email**: your-email@example.com
- **LinkedIn**: [Profil LinkedIn](https://linkedin.com/in/yourprofile)
