import math

r = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx * dx + dy * dy
b = 2 * (x1 * dx + y1 * dy)
c = x1 * x1 + y1 * y1 - r * r

D = b * b - 4 * a * c

if D < 0:
    if x1*x1 + y1*y1 <= r*r and x2*x2 + y2*y2 <= r*r:
        length = math.sqrt(a)
    else:
        length = 0.0
else:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2 * a)
    t2 = (-b + sqrtD) / (2 * a)

    t_low = max(0.0, min(t1, t2))
    t_high = min(1.0, max(t1, t2))

    if t_low > t_high:
        if x1*x1 + y1*y1 <= r*r and x2*x2 + y2*y2 <= r*r:
            length = math.sqrt(a)
        else:
            length = 0.0
    else:
        length = math.sqrt(a) * (t_high - t_low)

print(f"{length:.10f}")