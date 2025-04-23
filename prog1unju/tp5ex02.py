#serie_par_a
x=int(input('valor a superar:'))
s = 0
i = 0
while s <= x:
    i += 1
    s += 2 * i
print(f"serie={s} terminos={i-1}")