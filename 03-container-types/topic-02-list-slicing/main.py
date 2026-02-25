# ABOUT: List slicing

# This is used to retrieve a section of a list
# The syntax is: string[`start index`:`stop index`:`step`]

# The `start index` is inclusive
# The `stop index`  is exclusive

# E.g.
# `player_scores[2,5]` means,
# I want the elements starting from index 2 (including index 2),
# to index 5 (excluding index 5)

# So in simple terms. I want index 2, index 3, and index 4

# slicing does not modify the original list. It creates a new list

# The `step`, this how the slice will progress to the next element.
# By default this is set to `+1`. As in move forward by one step.
# E.g. index 0, index 1, index 2...

# ______________________________________________________________________________


def main():

    # _________________________________________________________________________

    # SECTION: Standard slicing

    # indexes:                  0,  1,  2,  3,  4, 5, 6,  7
    player_scores: list[int] = [7, 78, 12, 52, 10, 4, 10, 18]

    print(f"player_scores: {player_scores}")
    # player_scores: [7, 78, 12, 52, 10, 4, 10, 18]

    print(f"index 2 to index 5 (exclusive): {player_scores[2:5]}")
    # index 2 to index 5 (exclusive): [12, 52, 10]

    print(f"player_scores: {player_scores}")
    # player_scores: [7, 78, 12, 52, 10, 4, 10, 18]

    # _________________________________________________________________________

    # SECTION: Slicing without the start index

    # If you leave out the start index, Python will automatically start
    # at index 0

    print(f"index 0 to index 4 (exclusive): {player_scores[:4]}")
    # index 0 to index 4 (exclusive): [7, 78, 12, 52]

    # _________________________________________________________________________

    # SECTION: Slicing without the stop index

    # If you leave out the stop index, Python will give you all the elements
    # in the list starting from the start index.

    # This is inclusive on BOTH ends so the last item in the list
    # is included as well.

    print(
        f"All elements starting from index 5 (inclusive): {player_scores[5:]}"
    )
    # index 5 to index 4 (exclusive): [4, 10, 18]

    # _________________________________________________________________________

    # SECTION: Using the reverse index to get the lastest values in a list

    # You can access elements of a list by using the `reverse index` notation

    # With this method:
    # The last element in a list is at index `-1`
    # The second lastest element is at index `-2`
    # The third lastest element is at index `-3`

    # indexes:                         -6, -5, -4, -3, -2, -1
    closing_stock_prices: list[int] = [20, 40, 18, 15, 10, 12]

    print(f"The last closing price is: {closing_stock_prices[-1]}")
    print(f"The second last closing price is: {closing_stock_prices[-2]}")
    print(f"The third last closing price is: {closing_stock_prices[-3]}")
    # The last closing price is: 12
    # The second last closing price is: 10
    # The third last closing price is: 15

    print(
        f"The last 3 closing_stock_prices are: {closing_stock_prices[-3:]}"
    )
    # The last 3 closing_stock_prices are: [15, 10, 12]

    # _________________________________________________________________________


if __name__ == "__main__":
    main()
