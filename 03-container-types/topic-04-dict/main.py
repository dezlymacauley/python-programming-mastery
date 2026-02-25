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
    print(f"Renji's score is {player_scores["Renji"]}")
    # Renji's score is 1170

    # _________________________________________________________________________
   
    # Removing a key-value pair

    player_scores.pop("Gojo")
    print(f"player_scores: {player_scores}")
    # player_scores: {'Dezly': 3782, 'Tsunade': 7282, 'Renji': 1170}
    

    # _________________________________________________________________________

if __name__ == "__main__":
    main()
