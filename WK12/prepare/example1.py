# Example 1
#Procedural programming

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")


# Call main to start this program.
if __name__ == "__main__":
    main()