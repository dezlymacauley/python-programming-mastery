# ABOUT: datetime

# Useful time related functions

# ______________________________________________________________________________
from calendar import month

import datetime


def main():
    datetime_object = datetime.datetime(
        year=2026, month=2, day=26, hour=14, minute=7
    )
    print(f"datetime_object: {datetime_object}")
    # datetime_object: 2026-02-26 14:07:00

    print(f"year: {datetime_object.year}")
    # year: 2026

    #__________________________________________________________________________

    # SECTION: Comparing two time periods

    second_datetime_object = datetime.datetime(
        year=2025, month=1, day=14, hour=12, minute=5
    )

    if datetime_object < second_datetime_object:
        print(f"The second_datetime_object happens later")
    else:
        print(f"The second_datetime_object happens earlier")
    
    #__________________________________________________________________________

if __name__ == "__main__":
    main()
