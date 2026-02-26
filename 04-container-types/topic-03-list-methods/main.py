# ABOUT: List methods

# _____________________________________________________________________________


def main():

    # _________________________________________________________________________

    # SECTION: `.sort()`

    # This method will modify the original list
    # The elements will be sorted from smallest to largest

    player_scores: list[int] = [56, 10, 3, 7]

    player_scores.sort()
    print(f"player_scores sorted from smallest to largest: {player_scores}")
    # player_scores sorted from smallest to largest: [3, 7, 10, 56]

    # _________________________________________________________________________

    # SECTION: `.sort(reverse=True)`

    # This method will modify the original list
    # The elements will be sorted from largest to smallest

    player_scores.sort(reverse=True)
    print(f"player_scores sorted from largest to smallest: {player_scores}")
    # player_scores sorted from largest to smallest: [56, 10, 7, 3]

    # _________________________________________________________________________

    # SECTION: `.len()`

    # count the number of elements

    print(f"There are {len(player_scores)} elements in player_scores")
    # There are 4 elements in player_scores

    # _________________________________________________________________________

    # SECTION: `.append()`

    # Add items to the end of a list

    player_scores.append(44)
    player_scores.append(66)
    print(f"player_scores: {player_scores}")
    # player_scores: [56, 10, 7, 3, 44, 66]

    # _________________________________________________________________________

    # SECTION: `.remove(element)`

    player_scores.remove(10)
    print(f"player_scores: {player_scores}")
    # player_scores: [56, 7, 3, 44, 66]

    # _________________________________________________________________________

    # SECTION: `.clear()`

    # Remove all elements from a list
    
    # player_scores.clear()
    # print(f"player_scores: {player_scores}")
    # player_scores: []

    # _________________________________________________________________________
  
    # SECTION: `.max()`

    # Get the largest value in a list

    print(f"player_scores: {player_scores}")
    # player_scores: [56, 7, 3, 44, 66]

    print(f"largest value in player_scores: {max(player_scores)}")
    # largest value in player_scores: 66

    # _________________________________________________________________________
    
    # SECTION: `.min()`

    # Get the smallest value in a list

    print(f"smallest value in player_scores: {min(player_scores)}")
    # smallest value in player_scores: 3

    # _________________________________________________________________________


if __name__ == "__main__":
    main()
