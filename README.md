# P2_Komnum_E13
Praktikum 2 komputasi numerik kelas E kelompok 13

kelompok 13:
1. Muhammad Hafidh Rosyadi – 5025211013 
2. Heru Dwi Kurniawan – 5025211055 
3. Mohammad Ahnaf Fauzan – 5025211170

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

**CODE**
misalkan fungsi yang digunakan adalah exp(x):
```python
def f(x):
    return np.exp(x)
```
untuk setiap nilai A dibutuhkan metode trapezoid dengan pias n sebagai berikut
```python
def metode_trapezoid(a, b, n):
    h = (b - a) / n
    x = a
    ans = f(a)
    for i in range(1, n):
        x = x + h
        ans += 2*f(x)
    return (ans + f(b))*h*0.5
```

untuk metode romberg dengan pias n serta perbandingan metode dengan metode trapezoid dinyatakan sebagai berikut
```python
def metode_romberg(a, b, n):
    i = 1
    arrTable = []
    temp = []
    print("\nTABEL METODE TRAPEZOID PADA SETIAP PIAS")
    idx = 0
    while i <= n:
        print(f"{i}  {metode_trapezoid(a, b, i)}")
        sementara = metode_trapezoid(a, b, i)
        temp.append(metode_trapezoid(a, b, i))
        i = i*2
        idx = idx + 1
    arrTable.append(temp)
    h = 1
    while h != idx:
        j = h
        temp = []
        for p in range(j):
            temp.append(" ")
        while j < idx:  # persamaan extrapolasi richardson
            temp.append(arrTable[h-1][j]+(arrTable[h-1]
                        [j]-arrTable[h-1][j-1])/(pow(2, 2*h)-1))
            j += 1
        arrTable.append(temp)
        h = h + 1
    h = 1
    TabelUtama = pd.DataFrame()
    for i in arrTable:
        s = "O(h^" + str(2*h) + ")"
        h = h + 1
        TabelUtama[s] = i
    print("\nTABEL METODE ROMBERG PADA SETIAP PIAS\n")
    print(TabelUtama)
    sementara2 = arrTable[len(arrTable)-1][len(arrTable[len(arrTable)-1])-1]

    print(f"\nMETODE TRAPEZOID : {sementara}")
    print(f"\nMETODE ROMBERG : {sementara2}")
    nilaiAsli = float(
        input("\nmasukkan nilai asli untuk membandingkan error : "))
    TError = abs(sementara-nilaiAsli)/nilaiAsli*100
    RError = abs(sementara2-nilaiAsli)/nilaiAsli*100
    print(f"Error yang dihasilkan metode trapezoid : {TError}%")
    print(f"Error yang dihasilkan metode romberg : {RError}%")
```
**I/O**
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
sehingga dari output tersebut dapat diperoleh error yang dihasilkan metode romberg dengan pias/interval yang sama dengan metode trapezoid
menghasilkan perbedaan error yang cukup signifikan.(romberg jauh lebih akurat)
