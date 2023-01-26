import math
from tabulate import tabulate

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


def print_table_cans (names, radiuses, heights, prices):
    """Given 4 list of can's data which all have same size print its data in table format
    Parameters
        names[] (String): a list of cans' names
        radiuses[] (Float): a list of cans' radiuses
        heights[] (Float): a list of cans' heights
        prices[] (Float): a list of cans' prices
    Return: none
    """
    data_one = []
    size_lists = len(names)
    for numberCan in range(size_lists):
        can_price = prices[numberCan]
        can_radius = radiuses[numberCan]
        can_height = heights[numberCan]
        can_name = names[numberCan]
        can_volume = compute_volume(can_radius,can_height)
        can_surface_area = compute_surface_area(can_radius,can_height)
        can_storage_efficiency = compute_storage_efficiency(can_radius, can_height)
        can_cost_efficiency = compute_cost_efficiency(can_price, can_radius, can_height)

        data_line_one = [can_name, can_radius, can_height, can_price, can_volume, can_surface_area, can_storage_efficiency, can_cost_efficiency]
        data_one.append(data_line_one)
    print("CANS' TABLE DATA")
    print (tabulate(data_one, headers=["Name", "Radius(cm)", " Height(cm)", "Unit Cost(USD)","Volume", "Surface Area", "Storage Efficiency", "Cost Efficiency"]))


def print_all_cans (names, radiuses, heights, prices):
    """Given 4 list of can's data which all have same size print its data
    Parameters
        names[] (String): a list of cans' names
        radiuses[] (Float): a list of cans' radiuses
        heights[] (Float): a list of cans' heights
        prices[] (Float): a list of cans' prices
    Return: none
    """
    size_lists = len(names)
    for numberCan in range(size_lists):
        can_price = prices[numberCan]
        can_radius = radiuses[numberCan]
        can_height = heights[numberCan]
        can_name = names[numberCan]
        can_volume = compute_volume(can_radius,can_height)
        can_surface_area = compute_surface_area(can_radius,can_height)
        can_storage_efficiency = compute_storage_efficiency(can_radius, can_height)
        can_cost_efficiency = compute_cost_efficiency(can_price, can_radius, can_height)

        print(f"The can named {can_name} with radius of {can_radius}, height of {can_height} and price ${can_price}")
        print("Its computed values are")
        #print(f"Volume: {can_volume:.2f}, Surface area: {can_surface_area:.2f}, Storage efficiency: {can_storage_efficiency:.2f}, Cost efficiency: {can_cost_efficiency:.2f}\n")


def can_with_max_storage (names, radiuses, heights, prices):
    """Given 4 list of can's data which all have same size
    Parameters
        names[] (String): a list of cans' names
        radiuses[] (Float): a list of cans' radiuses
        heights[] (Float): a list of cans' heights
        prices[] (Float): a list of cans' prices
    Return: Index list to locate max sample
    """
    max_storage_efficiency = 0
    max_storage_efficiency_index = -1
    
    size_lists = len(names)

    for numberCan in range(size_lists):
        can_radius = radiuses[numberCan]
        can_height = heights[numberCan]
        can_storage_efficiency = compute_storage_efficiency(can_radius, can_height)

        if max_storage_efficiency < can_storage_efficiency:
            max_storage_efficiency = can_storage_efficiency
            max_storage_efficiency_index = numberCan
    
    return max_storage_efficiency_index


def can_with_max_effiency (names, radiuses, heights, prices):
    """Given 4 list of can's data which all have same size
    Parameters
        names[] (String): a list of cans' names
        radiuses[] (Float): a list of cans' radiuses
        heights[] (Float): a list of cans' heights
        prices[] (Float): a list of cans' prices
    Return: Index list to locate max sample
    """
    max_cost_efficiency = 0
    max_cost_efficiency_index = -1
    
    size_lists = len(names)

    for numberCan in range(size_lists):
        can_price = prices[numberCan]
        can_radius = radiuses[numberCan]
        can_height = heights[numberCan]
        can_cost_efficiency = compute_cost_efficiency(can_price, can_radius, can_height)
        if max_cost_efficiency < can_cost_efficiency:
            max_cost_efficiency = can_cost_efficiency
            max_cost_efficiency_index = numberCan

    return max_cost_efficiency_index


def main():
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    prices = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    #print_all_cans(names, radiuses, heights, prices)
    print_table_cans(names, radiuses, heights, prices)
    #can_with_max_storage(names, radiuses, heights, prices)
    #can_with_max_effiency(names, radiuses, heights, prices)

    
# Start this program by
# calling the main function.
main()
