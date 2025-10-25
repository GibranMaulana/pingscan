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
## Lisensi

MIT — gunakan sesuai kebutuhan.
