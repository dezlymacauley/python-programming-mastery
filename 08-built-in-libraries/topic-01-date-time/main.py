# ABOUT: datetime

# Useful time related functions

# ______________________________________________________________________________

# NOTE: When using the platform QuantConnect, 
# the datetime library is already imported.

from datetime import datetime, timedelta, timezone


def main():
    datetime_object = datetime(
        year=2026, month=2, day=26, hour=14, minute=7, tzinfo=timezone.utc
    )
    print(f"datetime_object: {datetime_object}")
    # datetime_object: 2026-02-26 14:07:00+00:00

    print(f"year: {datetime_object.year}")
    # year: 2026

    # __________________________________________________________________________

    # SECTION: Comparing two time periods

    second_datetime_object = datetime(
        year=2025, month=1, day=14, hour=12, minute=5, tzinfo=timezone.utc
    )

    if datetime_object < second_datetime_object:
        print(f"The second_datetime_object happens later")
    else:
        print(f"The second_datetime_object happens earlier")

    # __________________________________________________________________________

    # SECTION: Adding additional time to a datetime object

    third_datetime_object = datetime(
        year=2025, month=2, day=14, hour=12, minute=5
    )
    print(f"third_datetime_object: {third_datetime_object}")
    # third_datetime_object_10_hours_later: 2025-02-14 22:05:00

    # __________________________________________________________________________

    # SECTION: Adding additional time to a datetime object using `timedelta`

    third_datetime_object_10_hours_later = third_datetime_object + timedelta(
        hours=10
    )

    print(
        f"third_datetime_object_10_hours_later: {third_datetime_object_10_hours_later}"
    )
    # third_datetime_object_10_hours_later: 2025-02-14 22:05:00

    # __________________________________________________________________________

    # TIP: How is timedelta used in algo trading?
    # One of the most important usese of timedelta() is to check how long
    # it's been since an order was submitted and still not completely filled.

    order_submission_date = datetime(
        year=2026, month=2, day=26, hour=13, minute=15, tzinfo=timezone.utc
    )

    one_minute_since_submission_date = order_submission_date + timedelta(
        minutes=1
    )

    current_time = datetime.now(timezone.utc)
    print(f"current_time: {current_time}")

    if current_time >= one_minute_since_submission_date:
        print("It has been 1 minute since you submitted your order")
    else:
        print("Please wait 1 minute")

    # __________________________________________________________________________


if __name__ == "__main__":
    main()
