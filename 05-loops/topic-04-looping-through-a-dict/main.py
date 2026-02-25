# ABOUT: dict

# This stands for `dictionary`
# This is a data structure that is a collection of key-value pairs
# In other programming languages the equivalent is a hashmap

# Each key in the dictionary must be unique 

# A dictionary is an iterable object but it does not have indexes
# You get the information you want by using the key

# ______________________________________________________________________________


def main():

    player_scores: dict[str, int] = {
        "Dezly": 3782,
        "Tsunade": 7282,
        "Gojo": 2710,
    }

    print("List of players in player_scores:")
    print()

    # _________________________________________________________________________

    # SECTION: Printing out only the key

    for key in player_scores:
        print(f"{key}")
    # Dezly
    # Tsunade
    # Gojo


    print()

    # _________________________________________________________________________
  
    # SECTION: Printing out only the value
    
    # method 1
    for key in player_scores:
        print(f"{player_scores[key]}")
    # 3782
    # 7282
    # 2710
    
    print()
    
    # method 2
    for value in player_scores.values():
        print(f"{value}")
    # 3782
    # 7282
    # 2710

    # _________________________________________________________________________
   
    # SECTION: Printing out both the key and the value

    for key in player_scores:
        print(f"{key}: {player_scores[key]}")
    # Dezly: 3782
    # Tsunade: 7282
    # Gojo: 2710
    
    print()

    # _________________________________________________________________________
   
   # SECTION: Sorting a dictionary based on the highest value



    # _________________________________________________________________________

if __name__ == "__main__":
    main()
