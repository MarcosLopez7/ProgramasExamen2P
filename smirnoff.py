def smirnoff(data):

    data = sorted(data)
    d_plus = []
    d_minus = []

    for i in range(1, len(data) + 1):
        d_plus.append((i / len(data)) - data[i - 1])
        d_minus.append( data[i - 1] - ( (i - 1) / len(data) ) )

    max_plus = max(d_plus)
    max_minus = max(d_minus)

    if max_plus > max_minus:
        result = max_plus
    else:
        result = max_minus

    print(d_plus)
    print(d_minus)
    print("La prueba dice que: " + str(result))
    print("La D+ dice que: " + str(max_plus))
    print("La D- dice que: " + str(max_minus))