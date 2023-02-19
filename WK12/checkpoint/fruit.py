def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    print()

    fruit_list.reverse()
    print(f"reverse: {fruit_list}")
    print()
    
    fruit_list.append("orange") #add to the end orange, by default append will place it there
    print(f"append orange: {fruit_list}")
    print()

    index_apple = fruit_list.index("apple")
    fruit_list.insert(index_apple,"cherry")
    print(f"Insert cherry: {fruit_list}")
    print()

    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")
    print()

    last_index = len(fruit_list) - 1
    fruit_pop = fruit_list[last_index] #fruit_pop = fruit_list.pop() by default takes out the last one
    fruit_list.pop(last_index)
    print(f"pop {fruit_pop}: {fruit_list}")
    print()

    fruit_list.sort()
    print(f"sort: {fruit_list}")
    print()

    fruit_list.clear()
    print(f"clear: {fruit_list}")
    print()
    

def print_backwards(list):
    print("a")

# Call main to start this program.
if __name__ == "__main__":
    main()