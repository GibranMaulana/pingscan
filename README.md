<!-- PingScan
Simple QR scanning utility using webcam + OpenCV that opens a constructed attendance URL. -->

<!-- Logos: Python, OpenCV, NumPy -->
<p align="center">
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="64" alt="Python" />
	&nbsp;&nbsp;
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" width="64" alt="OpenCV" />
	&nbsp;&nbsp;
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="64" alt="NumPy" />
</p>

# PingScan

PingScan adalah aplikasi ringan untuk memindai (scan) kode QR menggunakan webcam.
Saat kode QR terdeteksi, aplikasi akan membentuk URL absensi dan otomatis membuka
URL tersebut di peramban.

Contoh URL yang dibuka:
`https://pingfest.id/attendance/check/<DATA_QR>`

---

## Ringkasan fitur

- Menggunakan OpenCV (`cv2.QRCodeDetector`) untuk deteksi QR secara real-time.
- Sederhana: satu file utama (`pingscan.py`) dan `requirements.txt` untuk dependensi.
- Dapat dijalankan di Windows, macOS, atau Linux asalkan Python dan webcam tersedia.

## Cara kerja singkat

1. Membuka webcam dengan OpenCV (`cv2.VideoCapture(0)`).
2. Setiap frame dipindai menggunakan `cv2.QRCodeDetector().detectAndDecode()`.
3. Jika ditemukan data, skrip membentuk URL absensi:
	 `https://pingfest.id/attendance/check/{data}`
4. URL dibuka di peramban default (hanya sekali per data QR unik selama sesi berjalan).

## Persyaratan

- Python 3.8+ disarankan
- Webcam (bawaan atau USB)
- Paket Python yang tercantum di `requirements.txt`:

```text
numpy==2.2.6
opencv-python==4.12.0.88
pyzbar==0.1.9
```

Catatan: Implementasi saat ini memakai OpenCV `QRCodeDetector`. `pyzbar` dimasukkan
sebagai opsi alternatif bila dibutuhkan pada beberapa sistem.

## Instalasi (Windows - PowerShell)

Buka PowerShell (pwsh) lalu jalankan:

```powershell
# buat virtual environment (disarankan)
python -m venv .venv
# aktifkan venv (PowerShell)
.\.venv\Scripts\Activate.ps1

# perbarui pip dan instal dependensi
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Pada macOS / Linux, gunakan `python3 -m venv .venv` lalu `source .venv/bin/activate`
kemudian `pip install -r requirements.txt`.

## Menjalankan

Dengan venv aktif, jalankan:

```powershell
python pingscan.py
```

Perilaku saat dijalankan:

- Akan muncul jendela berjudul `scanning...` yang menampilkan feed kamera.
- Saat QR terdeteksi, program akan:
	- Menggambar poligon hijau di sekitar QR
	- Menampilkan URL absensi pada konsol
	- Membuka URL di peramban (hanya sekali per payload QR unik)
- Tutup aplikasi dengan menekan `q`, `Q`, `Esc`, atau Ctrl+C di konsol.

## Catatan & pemecahan masalah

- Kamera tidak dapat diakses / pesan error "Cannot access camera":
	- Pastikan tidak ada aplikasi lain yang menggunakan webcam.
	- Di Windows, izinkan akses kamera untuk aplikasi terminal/PowerShell.
	- Coba ubah indeks kamera: di `pingscan.py` ganti `VideoCapture(0)` menjadi `VideoCapture(1)`.

- Deteksi QR tidak stabil:
	- Pastikan pencahayaan cukup dan kamera fokus.
	- Dekatkan atau jauhkan QR sampai terdeteksi.
	- Jika tetap gagal, pertimbangkan menggunakan `pyzbar` sebagai alternatif.

### Menggunakan pyzbar (opsional)

Jika ingin mencoba `pyzbar`, ubah logika deteksi di `pingscan.py` untuk memakai
`pyzbar.decode(frame)` kemudian proses objek hasil decode. Perhatikan bahwa `pyzbar`
bisa memerlukan dependensi sistem di beberapa OS.

## Kontrak singkat

- Input: frame video dari webcam.
- Output: membuka peramban ke `https://pingfest.id/attendance/check/<QR_DATA>` untuk setiap QR unik.
- Mode error: kamera tidak dapat diakses, tidak ada QR, atau kegagalan membuka peramban.

## Kasus tepi

- Pemindaian ulang QR yang sama: skrip mencegah membuka URL yang sama berkali-kali dengan
	menyimpan `opened_urls` di memori selama sesi berjalan.
- Payload QR sangat panjang/kompleks: detector akan mengembalikan data apa adanya; pastikan payload aman.

## Kontribusi

Ide perbaikan kecil:

- Tambahkan flag CLI (indeks kamera, nonaktifkan auto-open, template URL)
- Simpan QR yang sudah dipindai ke file atau database
- Tambahkan antarmuka GUI untuk menerima/menolak membuka URL

## Lisensi

MIT — gunakan sesuai kebutuhan.

---

Jika Anda mau, saya bisa:

- Menambahkan opsi CLI (argparse) untuk template URL dan indeks kamera
- Menambahkan skrip pengujian kecil atau workflow CI

Saya akan melanjutkan dengan pemeriksaan sintaks untuk `pingscan.py`.
