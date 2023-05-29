def expo(values, teta):
    filt = [values[0]]
    for i in range(1, len(values)):
        filt.append(teta * values[i] + (1 - teta) * filt[i - 1])
    return filt


values = list(map(float, input('Введите значения: ').split()))
teta = float(input('Введите коэффициент: '))
print(expo(values, teta))
