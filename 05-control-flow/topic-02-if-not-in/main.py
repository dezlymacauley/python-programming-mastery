# ABOUT: If not in

# You can use this to check if an item is not in a list

# ______________________________________________________________________________


def main():
    player_scores: list[int] = [10, 20, 50, 80]

    search_term: int = 40

    if search_term not in player_scores:
        print(f"{search_term} is not in player_scores")

if __name__ == "__main__":
    main()
