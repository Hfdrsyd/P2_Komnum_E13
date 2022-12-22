import math
import numpy as np
import pandas as pd

# fungsi yang akan di integrasi


def f(x):
    return np.exp(x)


# metode trapezoida
def metode_trapezoid(a, b, n):
    h = (b - a) / n
    x = a
    ans = f(a)
    for i in range(1, n):
        x = x + h
        ans += 2*f(x)
    return (ans + f(b))*h*0.5


def metode_romberg(a, b, p):
    i = 1
    arrTable = []
    temp = []
    print("\nTABEL METODE TRAPEZOID PADA SETIAP PIAS")
    idx = 0
    while i <= p:
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


a = int(input("Masukkan Batas bawah : "))
b = int(input("Masukkan Batas atas : "))
n = int(input("Jumlah Pias : "))

metode_romberg(a, b, n)
