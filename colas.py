def mm1(lam, miu, m, K, cs, cw):

    if m > 1:
        miu *= m

    l = lam / (miu - lam)
    w = 1 / (miu - lam)
    lq = lam ** 2 / (miu * (miu - lam))
    wq = lam / (miu * (miu - lam))
    ro = (lam / miu)
    p0 = 1 - ro
    P = []
    ct = m * cs + lam * w * cw

    for k in K:
        prob = (lam / miu) ** (k + 1)
        P.append({'k': k, 'probabilidad': prob})

    for p in P:
        print(p)

    print("Promedio de unidades en el sistema L = " + str(l))
    print("Promedio de tiempo en el sistema W = " + str(w))
    print("Promedio de unidades en la cola Lq = " + str(lq))
    print("Promedio de tiempo de esepera en la cola Wq = " + str(wq))
    print("Factor de uso para el sistema ro = " + str(ro))
    print("Factor de osio P0 = " + str(p0))
    print("Costo total CT = " + str(ct))

def mmm(lam, miu, m, K, cs, cw):

    sumatoria = 0

    for i in range(m):
        sumatoria += (1 / factorial(i)) * (lam / miu) ** i

    p0 = 1 / (sumatoria + ((1 / factorial(m)) * (lam / miu) ** m) * ((m * miu) / ((m * miu) - lam)))
    l = ((lam * miu * (lam / miu) ** m) / (factorial(m - 1) * (m * miu - lam) ** 2) ) * p0 + (lam / miu)
    w = l / lam
    lq = l - lam / miu
    wq = lq / lam
    ro = lam / (m * miu)
    ct = m * cs + lam * w * cw
    print("Promedio de unidades en el sistema L = " + str(l))
    print("Promedio de tiempo en el sistema W = " + str(w))
    print("Promedio de unidades en la cola Lq = " + str(lq))
    print("Promedio de tiempo de esepera en la cola Wq = " + str(wq))
    print("Factor de uso para el sistema ro = " + str(ro))
    print("Factor de osio P0 = " + str(p0))
    print("Costo total CT = " + str(ct))


def md1(lam, miu, cs, cw):

    lq = lam ** 2 / (2 *(miu * (miu - lam)))
    wq = lam / (2 * (miu * (miu - lam)))
    l = lq + lam / miu
    w = wq + 1 / miu
    ct = 1 * cs + lam * w * cw

    print("Promedio de unidades en el sistema L = " + str(l))
    print("Promedio de tiempo en el sistema W = " + str(w))
    print("Promedio de unidades en la cola Lq = " + str(lq))
    print("Promedio de tiempo de esepera en la cola Wq = " + str(wq))
    print("Costo total CT = " + str(ct))


def finitemm1(lam, miu, N, K, cs, cw):

    sum = 0

    for i in range(N):
        sum += (factorial(N) / factorial(N - i)) * (lam / miu) ** i

    p0 = 1 / sum
    lq = N - ((lam + miu) / lam) * (1 - p0)
    l = lq + (1 - p0)
    wq = lq / ((N - l) * lam)
    w = wq + 1 / miu
    P = []
    ct = 1 * cs + lam * w * cw

    for k in K:
        prob = (factorial(N) / factorial(N - k))(lam / miu) ** k
        P.append({'k': k, 'probabilidad': prob})

    for p in P:
        print(p)

    print("Promedio de unidades en el sistema L = " + str(l))
    print("Promedio de tiempo en el sistema W = " + str(w))
    print("Promedio de unidades en la cola Lq = " + str(lq))
    print("Promedio de tiempo de esepera en la cola Wq = " + str(wq))
    #print("Factor de uso para el sistema ro = " + str(ro))
    print("Factor de osio P0 = " + str(p0))
    print("Costo total CT = " + str(ct))

def factorial(num):

    if num < 2:
        return 1

    res = 1
    for i in range(2, num + 1):
        res *= i

    return res