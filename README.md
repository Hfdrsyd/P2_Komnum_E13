# P2_Komnum_E13
Praktikum 2 komputasi numerik kelas E kelompok 13
integrasi romberg merupakan teknik yang digunakan dalam integrasi numerik untuk menganalisis kasus dimana fungsi yang akan diintegrasikan tersedia.
Sedangkan integrasi numerik sendiri merupakan perhitungan aproksimasi luas daerah di bawah fungsi pada selang tertentu.
Pada dasarnya integrasi romberg merupakan metode trapezoida yang diefisiensikan dengan extrapolasi richardson, sehingga menghasilkan galat yang lebih kecil.
Extrapolasi Richardson merupakan metode untuk mengkombinasikan dua perkiraan integral secara numerik untuk memperoleh nilai ketiga, yang lebih akurat.
Setiap penerapan extrapolasi richardson akan menaikkan order galat pada hasil solusinya sebesar dua.

Untuk melakukan perhitungan diperlukan tabel romberg yang dinyatakan sebagai:
![image](https://user-images.githubusercontent.com/92217730/209085907-1ce2addf-634a-4a95-8920-1c7aa580da45.png)


dimana untuk setiap A_k merupakan perkiraan nilai integrasi dengan kaidah trapesium dengan pias n=2^k.
selanjutnya untuk setiap B_k, C_k, D_k dengan extrapolasi Richardson diperoleh:

![image](https://user-images.githubusercontent.com/92217730/209086732-c62418d7-cf5d-49f5-826a-7feae04b5513.png)


misalkan B merupakan index setelah A, C merupakan index setelah B dan seterusnya maka dapat dituliskan persamaan rekursif untuk mewakili A,B,C,...
sebagai berikut:

![image](https://user-images.githubusercontent.com/92217730/209092419-68b30b37-195d-49f2-8e4b-f143b27ca698.png)

#CODE

#I/O
```python
Masukkan Batas bawah : 0
Masukkan Batas atas : 4
Jumlah Pias : 8

TABEL METODE TRAPEZOID PADA SETIAP PIAS
1  111.19630006628847
2  70.37626223100554
4  57.99194986714948
8  54.71015306379173

TABEL METODE ROMBERG PADA SETIAP PIAS

       O(h^2)     O(h^4)     O(h^6)     O(h^8)
0  111.196300
1   70.376262  56.769583
2   57.991950  53.863846   53.67013
3   54.710153  53.616221  53.599712  53.598595

METODE TRAPEZOID : 54.71015306379173

METODE ROMBERG : 53.59859472845862

masukkan nilai asli untuk membandingkan error : 53.59815
Error yang dihasilkan metode trapezoid : 2.074704189961281%
Error yang dihasilkan metode romberg : 0.0008297459121720912%
```
