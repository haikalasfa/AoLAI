Langkah 1: Install Python
Berikut adalah petunjuk menyeluruh dalam bahasa Indonesia untuk mengoperasikan program di laptop baru:
1. Unduh Python:
Kunjungi: [python.org](https://www.python.org).
Klik menu Download dan pilih versi terbaru sesuai sistem operasi Anda (Windows/macOS).
2. Install Python:
Jalankan file installer yang telah diunduh.
Saat instalasi, centang kotak bertuliskan”Add Python to PATH” (ini sangat penting).
Pilih opsi untuk menginstal Python dengan pip.
3. Verifikasi Instalasi Python:
Buka terminal atau command prompt: Windows: Tekan `Win + R, ketik `cmd, lalu tekan Enter.
macOS: Buka aplikasi Terminal.
Ketik:
bash
Python –version
Jika instalasi berhasil, akan muncul versi Python (contoh: `Python 3.x.x).

Langkah 2: Install Editor Kode
1. Unduh Visual Studio Code (VS Code):
Kunjungi [code.visualstudio.com](https://code.visualstudio.com) dan unduh versi terbaru.
2. Install Visual Studio Code dan buka aplikasinya setelah selesai.
   
Langkah 3: Install Library yang Dibutuhkan
1. Buka terminal atau command prompt.
2. Install library Python dengan mengetikkan:
bash
Pip install numpy matplotlib scikit-learn opencv-python-headless
Jika Anda menggunakan macOS dan mengalami masalah dengan Tkinter, instal dengan:
Bash
Brew install python-tk

Langkah 4: Simpan Kode Program
1. Buka Visual Studio Code.
2. Buat file baru:
Pilih File > New File.
 Salin dan tempel kode yang disediakan ke file tersebut.
3. Simpan file:
Tekan Ctrl + S (Windows) atau Cmd + S (macOS). Simpan file dengan nama market_chart_analyzer.py.

Langkah 5: Jalankan Program
1. Buka terminal di Visual Studio Code:
Pilih View > Terminal atau tekanCtrl + (tanda backtick).
2. Arahkan ke folder tempat file disimpan:
bash
Cd path/to/your/script
3. Jalankan skrip:
bash
Python market_chart_analyzer.py

Langkah 6: Gunakan Aplikasi
1. Jendela Market Chart Analyzer akan muncul.
2. Pilih File Gambar:
Klik tombol “Select File” untuk membuka dialog pemilihan file.
Pilih gambar grafik pasar (format: .png, .jpg, .bmp).
3. Proses Gambar:
Setelah memilih file, klik “Submit” untuk memproses gambar.
Jendela baru akan menampilkan gambar dengan zona support dan resistance yang ditandai.
4. Keluar:
Klik tombol “Back” atau tutup jendela untuk keluar dari aplikasi.

Masalah Umum pada Sistem Baru
1. Python Tidak Dikenali di Terminal:
Pastikan Python ditambahkan ke PATH selama instalasi.
Jika terlewat, instal ulang Python dan pastikan untuk mencentang kotak Add to PATH.
2. Library Tidak Lengkap:
Periksa kembali apakah Anda sudah menjalankan perintah:
bash
Pip install numpy matplotlib scikit-learn opencv-python-headless
3. Error Tkinter pada macOS: Instal Tkinter dengan:
bash
Brew install python-tk
Setelah Berhasil
Kini sistem Anda sudah siap untuk pengembangan Python! Anda bisa menggunakan setup ini untuk menjalankan skrip lain atau membuat proyek Anda sendiri.
