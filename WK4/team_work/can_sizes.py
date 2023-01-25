import math

def compute_volume(radius, height):
    """Compute and return a can's volume.
    Parameters
        radius (float): a can's radius in centimeters.
        height (float): a can's height in centimeters.
    Return: a can's volume.
    """
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    """Compute and return a can's surface area.
    Parameters
        radius (float): a can's radius in centimeters.
        height (float): a can's height in centimeters.
    Return: a can's surface area.
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    """Compute and return a can's storage efficiency.
    Parameters
        radius (float): a can's radius in centimeters.
        height (float): a can's height in centimeters.
    Return: a can's storage efficiency.
    """
    storage_efficiency = compute_volume(radius, height) / compute_surface_area (radius, height)
    return storage_efficiency

def compute_cost_efficiency(price, radius, height):
    """Compute and return a can's cost efficiency.
    Parameters
        radius (float): a can's radius in centimeters.
        height (float): a can's height in centimeters.
        price (float): a can's price in USD
    Return: a can's cost efficiency.
    """
    cost_efficiency = compute_volume(radius, height) / price
    return cost_efficiency

def main():
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    prices = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    max_storage_efficiency = 0
    max_storage_efficiency_index = -1
    size_lists = len(names)

    for numberCan in range(size_lists):
        print("For the can "+names[numberCan])
        print(f"Compute volume is {compute_volume(radiuses[numberCan],heights[numberCan]):.2f}")
        print(f"Compute surface area is {compute_surface_area(radiuses[numberCan],heights[numberCan]):.2f}")
        print(f"Compute storage efficiency is {compute_storage_efficiency(radiuses[numberCan], heights[numberCan]):.2f}")
        print(f"Compute cost efficiency is {compute_cost_efficiency(prices[numberCan], radiuses[numberCan], heights[numberCan]):.2f}\n")
        if max_storage_efficiency < compute_storage_efficiency(radiuses[numberCan], heights[numberCan]):
            max_storage_efficiency = compute_storage_efficiency(radiuses[numberCan], heights[numberCan])
            max_storage_efficiency_index = numberCan
    
    print(f"The can design named '{names[max_storage_efficiency_index]}', its storage efficiency is equal to {max_storage_efficiency:.2f}, its price is ${prices[max_storage_efficiency_index]}"  )

# Start this program by
# calling the main function.
main()
