
def tiempo_maximo(n, consultas):
    cache = []
    t_act = 0 
    t_max = 0
    for c in consultas:
        if c in cache:
            t_act = t_act + 1
        else:
            if t_act > t_max:
                t_max = t_act
            t_act = 0
            if len(cache) == n:
                cache.pop(0)
            cache.append(c)
    return t_max

con = [1,2,3,2,4,2,3,3,4,2,1,2]
print(tiempo_maximo(3, con))