def euclidian_distance(q, r):
    return pow(pow(float(q[0]) - float(r[0]), 2) + pow(float(q[1]) - float(r[1]), 2)
               + pow(float(q[2]) - float(r[2]), 2) + pow(float(q[3]) - float(r[3]), 2), 1 / 2)
