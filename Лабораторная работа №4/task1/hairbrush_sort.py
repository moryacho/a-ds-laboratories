def hairbrush_sort(a):
    dist = int(len(a) / 1.217)

    for step in range(dist, 0, -1):
        for i in range(0, len(a) - step):
            if a[i] > a[i + step]:
                a[i], a[i + step] = a[i + step], a[i]
