# ABOUT: List

# Unlike Rust, C, and C++,
# Python does not have the concept of a fixed-sized list.
# In Python all lists are dynamically-sized.

# Another major difference in Python is that the elements in a list do not
# have to be of the same data type.

# ______________________________________________________________________________


def main():

    # This is a list that should contain integers
    my_standard_list: list[int] = [7, 78, 12]
    print(f"my_standard_list: {my_standard_list}")

    # This is a list that can contain `int` and `str` data types.
    # The order does not matter. What matters is that you specify
    # all of the potential data types that the list can contain.
    my_mixed_list: list[int | str] = ["Dezly", 7, 50, "Hello", True]
    print(f"my_mixed_list: {my_mixed_list}")


if __name__ == "__main__":
    main()
