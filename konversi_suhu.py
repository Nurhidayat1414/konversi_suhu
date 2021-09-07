"""
RUMUS KONVERSI SUHU

@author --> Nurhidayat

celsius -> fahrenheit =( celsius * 9/5 )+ 32
celsius -> kelvin = celsius + 273.15
celsius -> Reamur = 4/5 * celsius

fahrenheit -> celsius = ( f - 32 ) * 5/9
fahrenheit -> kelvin = (f - 32) * 5/9 + 273.15
fahrenheit -> reamur = 4/9 * ( f - 32 )

kelvin -> Celsius = k - 273.15
kelvin -> fahrrenheit = (k - 273.15 ) * 9/5 + 32
kelvin -> reumur = 4/5 * ( K-273 )

reamur -> celsius = ( 5/4 ) * r
reamur -> fahrenheit = ( 9/4 * r ) + 32
reamur -> kelvi  = c + 273
"""


# membuat fungsi untuk koversi dari selsius ke fahrenheit
def c_f(cel):
    return (cel * 9 / 5) + 32  # mengembalikan nilai hasil konversi


# membuat fungsi untuk konversi dari selisius ke kelvin
def c_k(cel):
    return cel + 273.15  # mengembalikan nilai hasil konversi


# membuat fungsi untuk konversi dari celsius ke reamur
def c_r(cel):
    return 4 / 5 * cel  # mengembalikan nilai hasil konversi


def main():
    # menampung input dari user dan di simpan ke variabel nilai_selsius
    nilai_selsius = int(input("masukan nilai selsius: "))

    print("-" * 20)
    print(f"komversi dari {nilai_selsius} selsius ke fanherhit :", c_f(nilai_selsius), "F")
    print(f"komversi dari {nilai_selsius} selsius ke kelvin :", c_k(nilai_selsius), "k")
    print(f"komversi dari {nilai_selsius} selsius ke reamur :", c_r(nilai_selsius), "r")


main()
