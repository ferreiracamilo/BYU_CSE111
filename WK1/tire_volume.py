import math

pai = math.pi
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = pai * w**2 * a * (w * a + 2540 * d) / 10000000000
print(f"Volume is {v:.2f}")