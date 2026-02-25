# ABOUT: List methods

# ______________________________________________________________________________


def main():

    #__________________________________________________________________________
  
    # SECTION: `.sort()`

    # This method will modify the original list
    # The elements will be sorted from smallest to largest

    player_scores: list[int] = [56, 10, 3, 7]
   
    player_scores.sort()
    print(f"player_scores sorted from smallest to largest: {player_scores}")
    # player_scores sorted from smallest to largest: [3, 7, 10, 56]

    #__________________________________________________________________________
    
    # SECTION: `.sort(reverse=True)`

    # This method will modify the original list
    # The elements will be sorted from largest to smallest

    player_scores.sort(reverse=True)
    print(f"player_scores sorted from largest to smallest: {player_scores}")
    # player_scores sorted from largest to smallest: [56, 10, 7, 3]

    #__________________________________________________________________________
    
    # SECTION: `.len()`

    # count the number of elements

    print(f"There are {len(player_scores)} elements in player_scores")
    # There are 4 elements in player_scores

    #__________________________________________________________________________

if __name__ == "__main__":
    main()

