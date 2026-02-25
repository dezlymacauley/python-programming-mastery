# ABOUT: List

# Unlike Rust, C, and C++,
# Python does not have the concept of a fixed-sized list.
# In Python all lists are dynamically-sized.

# Another major difference in Python is that the elements in a list do not
# have to be of the same data type.

# ______________________________________________________________________________


def main():

    # _________________________________________________________________________

    # SECTION: Homogeneous list

    # This is a list that should contain integers
    my_standard_list: list[int] = [7, 78, 12]
    print(f"my_standard_list: {my_standard_list}")

    # _________________________________________________________________________

    # SECTION: Heterogeneous list

    # This is a list that can contain `int` and `str` data types.
    # The order does not matter. What matters is that you specify
    # all of the potential data types that the list can contain.
    my_mixed_list: list[int | str] = ["Dezly", 7, 50, "Hello", True]
    print(f"my_mixed_list: {my_mixed_list}")

    # _________________________________________________________________________

    # SECTION: Accessing elements by index

    # Indexes:                    0        1        2
    player_scores: list[str] = ["Gojo", "Kento", "Dezly"]

    print(f"The value at index 0 is {player_scores[0]}")
    print(f"The value at index 1 is {player_scores[1]}")
    print(f"The value at index 2 is {player_scores[2]}")
    # The value at index 0 is Gojo
    # The value at index 1 is Kento
    # The value at index 2 is Dezly

    # Changing a value in a list
    player_scores[0] = "Cassie"
    print(f"The value at index 0 is {player_scores[0]}")
    # The value at index 0 is Cassie

# _________________________________________________________________________

if __name__ == "__main__":
    main()
