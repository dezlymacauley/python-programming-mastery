# ABOUT: functions

# A function is a tool that performs actions when it is called.
# It may accept no arguments, or multiple arguments.
# It may return no elements, or multiple elements back to the caller.

#______________________________________________________________________________

# SECTION: 1. Function that accepts no arguments, and returns no elements


def greet_stranger() -> None:
    print("Hello stranger")


#______________________________________________________________________________

# SECTION: 2. Function that accepts a single argument, and returns no elements


def greet_user(user_name: str) -> None:
    print(f"Hello {user_name}")


#______________________________________________________________________________

# SECTION: 3. Function that accepts multiple arguments,
# and returns no elements


def display_user_age(user_name: str, user_age: int) -> None:
    print(f"{user_name} is {user_age} years old")

#______________________________________________________________________________

# SECTION: 4. Function that returns a single element

def add_two(num_1: int, num_2: int) -> int:
    total = num_1 + num_2  
    return total

#______________________________________________________________________________


# SECTION: 5. Function that returns a mutiple element

def doubled_scores(num_1: int, num_2: int) -> tuple[int, int]:
    first_score_doubled = num_1 * 2
    second_score_doubled = num_2 * 2
    return (first_score_doubled, second_score_doubled)

#______________________________________________________________________________

def main():
    greet_stranger()
    greet_user("Dezly")
    display_user_age(user_name="Mark", user_age=20)

    saturday_sales: int = 20
    sunday_sales: int = 40
    weekend_sales = add_two(saturday_sales, sunday_sales)
    print(f"weekend_sales: {weekend_sales}")

    doubled_score_01, doubled_score_02 = doubled_scores(10, 5)

    print(f"doubled_score_01: {doubled_score_01}")
    print(f"doubled_score_02: {doubled_score_02}")

if __name__ == "__main__":
    main()
