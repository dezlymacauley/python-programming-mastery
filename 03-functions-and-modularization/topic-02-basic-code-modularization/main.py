from custom_functions import (
    greet_stranger,
    greet_user,
    display_user_age,
    add_two,
    doubled_scores,
)


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
