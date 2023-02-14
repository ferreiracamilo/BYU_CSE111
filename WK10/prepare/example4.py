# Example 4

def main():
    try:
        players = int(input("Enter the number of players: "))
        teams = int(input("Enter the number of teams: "))

        players_per_team = players / teams

        print(f"Each team should have {players_per_team} players")

    except ZeroDivisionError as zero_div_err:
        print(zero_div_err)

if __name__ == "__main__":
    main()