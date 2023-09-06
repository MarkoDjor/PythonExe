nizka = [10, 20, 30, 40, 50, 60]

nizka_p = nizka[:1] + nizka[1::2]

nizka_n = nizka[2:2] + nizka[2::2]

suma_nizka = sum(nizka_p) - sum(nizka_n)

print(nizka_p)

print(nizka_n)

print( suma_nizka )