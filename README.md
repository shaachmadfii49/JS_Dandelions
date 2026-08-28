# Python Lyric - Dandelions

Repositori ini berisi program Python untuk menampilkan lirik lagu "Dandelions". Proyek ini dibuat untuk memenuhi tugas mahasiswa baru di Program Studi Teknologi Informasi.

## Tentang Proyek Ini
Program ini bekerja dengan cara mencetak teks lirik ke layar terminal secara bertahap. Kami menggunakan modul bawaan Python (`sys` dan `time`) untuk membaca baris lirik dan mengatur jeda waktu antar kalimatnya. Tujuannya supaya teks yang muncul bisa pas dengan ritme dan tempo lagu aslinya.

## Penjelasan Kode
* **Struktur Data:** Menggunakan struktur data `list` yang berisi `tuple` untuk menyimpan baris lirik beserta durasi jeda (delay) spesifiknya.
* **Logika Program:** Menggunakan perulangan `for` di dalam sebuah fungsi utama (`def`) untuk menampilkan teks lirik baris demi baris dan huruf demi huruf.
* **Typing Effect:** Huruf muncul satu per satu menggunakan perintah `sys.stdout.write` dengan jeda 0.09 detik.
* **Custom Delay:** Menggunakan perintah `time.sleep()` untuk mengatur jeda waktu setelah baris lirik selesai diketik (berkisar antara 0.5 sampai 3.0 detik).
* **Tanpa Library Tambahan:** Skrip ini murni menggunakan modul bawaan Python, sehingga bisa langsung dieksekusi tanpa perlu *install package* eksternal.

## Kelompok 3 Javascript
Proyek ini dikerjakan bersama-sama oleh:
* Naurah Luthfitah Firdausi
* Achmad Abimanyu Al Mufty
* Dio Ihsan Adi Wijaya
* Manuel Vincent Andanu
* Vera Eva Aprillia
* Keisha Achmad Fiandika Putera
* Diny Agata Rahmawati
