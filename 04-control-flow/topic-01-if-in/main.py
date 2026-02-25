# ABOUT: If in

# You can use this to check if an item is in a list

# ______________________________________________________________________________


def main():
    player_scores: list[int] = [10, 40, 50, 80]

    search_term: int = 40

    if search_term in player_scores:
        print(f"{search_term} is in player_scores")

if __name__ == "__main__":
    main()
