import math

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    storage_efficiency = compute_volume(radius, height) / compute_surface_area (radius, height)
    return storage_efficiency

def compute_cost_efficiency(price, radius, height):
    cost_efficiency = compute_volume(radius, height) / price
    return cost_efficiency

def main():
    # compute_cost_efficiency(storage_efficiency, price, radius, height)
    print(compute_cost_efficiency(price = 0.43, radius = 7.78, height = 11.91))

# Start this program by
# calling the main function.
main()
