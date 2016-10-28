import scipy.stats, math

def correalo(alfa, data, l, i):

    m = 0

    for k in range(len(data), 0, -1):
        if len(data) >= (i + (k + 1) * l):
            m = k
            break

    sumatoria_ril = 0

    for k in range(m + 1):
        sumatoria_ril += data[(i + k * l) - 1] * data[(i + (k + 1) * l) - 1]

    ril = 1 / (m + 1) * sumatoria_ril - 0.25
    sigril =  math.sqrt(13 * m + 7) / (12 * (m + 1))
    z0 = ril / sigril
    zalfa = scipy.stats.norm.ppf(alfa / 2)

    if abs(z0) > abs(zalfa):
        print("Esto se tiene que rechazar")
    else:
        print("Esto NO se tiene que rechazar")


    print("M = " + str(m))
    print("N = " + str(len(data)))
    print("Z0 = " + str(z0))
    print("Zalfa = " + str(zalfa))
