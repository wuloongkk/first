import time

start_time=time.time()
for a in range(1,1001):
    for b in range(1,1001):
        c=1000-b-a
        if a**2+b**2==c**2:
            print(f"a={a},b={b},c={c}")
print(f"Time taken:{time.time()-start_time}seconds")



import time

start = time.time()

target = 500000
solutions = set()

for m in range(1, int(target**0.5) + 1):
    if target % m == 0:
        n = target // m
        for pair in [(m, n), (n, m)]:
            m1, n1 = pair
            if m1 < 1000 and n1 < 1000 and (m1 + n1) > 1000:
                a = 1000 - m1
                b = 1000 - n1
                c = m1 + n1 - 1000
                if a > 0 and b > 0 and c > 0:
                    triplet = tuple(sorted([a, b, c]))
                    solutions.add(triplet)

for sol in solutions:
    print(f"a={sol[0]}, b={sol[1]}, c={sol[2]}")

end = time.time()
print(f"Time: {end - start:.6f} seconds")