# Example 7

def main():
    # Create a list that contains data about countries.
    countries = [
        # [country_name, land_area, population, gdp_per_capita]
        ["Mexico", 1972550, 126014024, 21362],
        ["France",  640679,  67399000, 45454],
        ["Ghana",   239567,  31072940,  7343],
        ["Brazil", 8515767, 210147125, 14563],
        ["Japan",   377975, 125480000, 41634]
    ]

    # Print the unsorted list.
    print("Original unsorted list of countries")
    for country in countries:
        print(country)
    print()

    # Define a lambda function that will be used as the
    # key function by the sorted function. The lambda
    # function extracts the population data from a
    # country so that the population will be used for
    # sorting the list of countries.
    POPULATION_INDEX = 2
    popul_func = lambda country: country[POPULATION_INDEX]

    # Sort the list of countries by the population.
    sorted_list = sorted(countries, key=popul_func)

    # Print the sorted list.
    print("List of countries sorted by population")
    for country in sorted_list:
        print(country)
    print()

    # Define a lambda function that will be used as the
    # key function by the sorted function. The lambda
    # function extracts the population data from a
    # country so that the population will be used for
    # sorting the list of countries.
    NAME_INDEX = 0
    name_func = lambda country: country[NAME_INDEX]

    # Sort the list of countries by the population.
    sorted_list = sorted(countries, key=name_func)

    # Print the sorted list.
    print("List of countries sorted by population")
    for country in sorted_list:
        print(country)


# Call main to start this program.
if __name__ == "__main__":
    main()