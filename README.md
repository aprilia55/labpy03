# Praktikum 3 - perulangan

Nama : Alafarizki Aprilia Putri

Kelas : TI.24.A.5

NIM : 312410455

Mata Kuliah : Bahasa Pemograman

## alur kode latihan1

```python
from random import random
```
Kode ini mengimpor fungsi random() dari modul random, yang akan menghasilkan angka acak antara 0 dan 1.

```python
n = int(input("masukkan nilai N: "))
```
Kode ini meminta pengguna untuk memasukkan nilai `N`, yang akan menentukan jumlah data yang ingin dihasilkan yang memenuhi kriteria tertentu.

```python
count = 0
```
Variabel `count` diinisialisasi dengan nilai 0, yang akan digunakan untuk menghitung jumlah data acak yang sudah memenuhi kriteria.

```python
while count < n:
```
Kode ini membuat sebuah while loop yang akan terus berjalan selama nilai `count` kurang dari `n`.

```python
random_number = random()
```
Dalam setiap iterasi while loop, kode ini menghasilkan angka acak `random_number` antara 0 dan 1.

```python
if random_number < 0.05:
```
Setelah menghasilkan angka acak, kode memeriksa apakah angka tersebut kurang dari 0.05. Jika ya, maka angka tersebut dianggap memenuhi kriteria.

```python
print(f"data ke {count} = {random_number}")
count += 1
```
Jika angka acak memenuhi kriteria (`random_number < 0.05`), maka:

- Kode akan menampilkan angka acak tersebut dan indeksnya.
- Nilai count akan ditambah 1 untuk menunjukkan bahwa satu angka yang memenuhi kriteria telah ditemukan.

- ```python
print("SELESAI")
```
akan menampilkan `SELESAI!`
```

## alur kode 2

```python
modal_awal = 100_000_000
```
Kode ini menginisialisasi variabel `modal_awal` dengan nilai 100 juta.

```python
laba_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]
```
- `0` berarti tidak ada laba pada bulan tersebut.
- `0.01` laba 1%.
- `0.05` laba 5%.
- `0.03` laba 3%.

```python
modal = modal_awal
```
Variabel `modal` diinisialisasi dengan nilai `modal_awal`. Variabel ini akan diubah setiap bulan untuk menghitung total modal setelah laba ditambahkan.

```python
for i, persentase_laba in enumerate(laba_bulan):
```

Loop `for` digunakan untuk menghitung laba dan memperbarui modal setiap bulan. `enumerate` memberikan indeks `i` untuk melacak bulan ke berapa, dan `persentase_laba` adalah nilai persentase laba untuk bulan tersebut.

```python
laba_bulan_ini = modal * persentase_laba
```

Di dalam loop, variabel `laba_bulan_ini` digunakan untuk menghitung laba berdasarkan `modal` saat ini dan `persentase_laba` bulan tersebut. Laba ini kemudian akan ditambahkan ke modal.
```python

modal += laba_bulan_ini
```
Laba yang diperoleh pada bulan tersebut (`laba_bulan_ini`) ditambahkan ke `modal`, memperbarui total modal.

```python
print(f"laba bulan ke{i+1}: sebesar {persentase_laba*100}% -> Total modal: Rp{modal:,.0f}")
```

Bulan keberapa (`i+1` untuk menjadikannya mulai dari 1).
Persentase laba untuk bulan tersebut (dikali 100 agar dalam bentuk persen).
Total modal setelah laba bulan tersebut ditambahkan, diformat dalam format rupiah dengan pemisah ribuan.

```python
print(f"\nTotal modal pada akhir bulan ke-8: Rp{modal:,.0f}")
```
Setelah loop selesai, kode ini menampilkan total modal setelah bulan ke-8, diformat dengan pemisah ribuan untuk tampilan yang lebih mudah dibaca.


