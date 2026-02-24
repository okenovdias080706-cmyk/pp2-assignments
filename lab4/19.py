import math

r = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
d = math.hypot(dx, dy)

dot = x1*dx + y1*dy
seg_len_sq = dx*dx + dy*dy

if seg_len_sq == 0:
    print("0.0000000000")
    exit()

t = -dot / seg_len_sq

if 0 <= t <= 1:
    px = x1 + t*dx
    py = y1 + t*dy
    dist_to_center = math.hypot(px, py)
else:
    dist_to_center = min(math.hypot(x1, y1), math.hypot(x2, y2))

if dist_to_center >= r:
    print(f"{d:.10f}")
else:
    OA = math.hypot(x1, y1)
    OB = math.hypot(x2, y2)

    ta = math.sqrt(OA*OA - r*r)
    tb = math.sqrt(OB*OB - r*r)

    angleA = math.acos(r / OA)
    angleB = math.acos(r / OB)

    cos_theta = (x1*x2 + y1*y2) / (OA * OB)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    theta = math.acos(cos_theta)

    arc_angle = theta - angleA - angleB

    length = ta + tb + r * arc_angle
    print(f"{length:.10f}")