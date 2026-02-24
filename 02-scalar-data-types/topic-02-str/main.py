# ABOUT: str

# The data type `str` is short for string. 
# This is data type is for working with text in Python.

# ______________________________________________________________________________

# Brings the `dedent` function from the `textwrap` module of the Python
# standard library.

# This is used to remove the indentation when printing 
# multi-line strings in Python.
from textwrap import dedent


def main() -> None:

    # How to create a single-line string
    user_name: str = "Tenshin"
    print(f"user_name: {user_name}")

    # How to create multi-line string
    my_messages = dedent("""
    Message A: Learn 🦀 Rust
    Message B: Learn 🔹 C
    Message C: Learn 🔷 C++
    Message D: Learn 🐍 Python
    """)

    print(f"my_messages: {my_messages}")

if __name__ == "__main__":
    main()

# ______________________________________________________________________________
