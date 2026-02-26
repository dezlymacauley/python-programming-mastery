# ABOUT: dict

# This stands for `dictionary`
# This is a data structure that is a collection of key-value pairs
# In other programming languages the equivalent is a hashmap

# Each key in the dictionary must be unique

# A dictionary is an iterable object but it does not have indexes
# You get the information you want by using the key

# ______________________________________________________________________________


def main():

    # _________________________________________________________________________

    player_scores: dict[str, int] = {
        "Dezly": 3782,
        "Tsunade": 7282,
        "Gojo": 2710,
    }

    print(f"Dezly's score is {player_scores['Dezly']}")
    print(f"Tsunade's score is {player_scores['Tsunade']}")
    print(f"Gojo's score is {player_scores['Gojo']}")
    # Dezly's score is 3782
    # Tsunade's score is 7282
    # Gojo's score is 2710

    # _________________________________________________________________________

    # Adding a new key-value pair
    player_scores["Renji"] = 1170
    print(f"Renji's score is {player_scores['Renji']}")
    # Renji's score is 1170

    # _________________________________________________________________________

    # Removing a key-value pair

    player_scores.pop("Gojo")
    print(f"player_scores: {player_scores}")
    # player_scores: {'Dezly': 3782, 'Tsunade': 7282, 'Renji': 1170}

    # _________________________________________________________________________

    # TIP: Always check if a search_term exists in the dictionary
    # before trying to remove it

    search_term = "Dezly"

    if search_term in player_scores:
        print(f"{search_term} exists")
    else:
        print(f"{search_term} does not exist")

    # _________________________________________________________________________

    # TIP: Never remove a key-value pair from a dictionary during a for loop

    # _________________________________________________________________________

    # SECTION: How to create a sorted list of keys from a dict,

    stock_yearly_growth: dict[str, int] = {
        "GOOGL": 3782,
        "META": 4032,
        "AMZN": 1824,
        "NFLX": 6822,
        "AAPL": 2304,
    }

    # Sort the dictionary by values in descending order (Largest value first)
    sorted_keys = sorted(
        stock_yearly_growth, key=lambda k: stock_yearly_growth[k], reverse=True
    )

    print(f"sorted_keys: {sorted_keys}")
    # sorted_keys: ['NFLX', 'META', 'GOOGL', 'AAPL', 'AMZN']


# _________________________________________________________________________


if __name__ == "__main__":
    main()
