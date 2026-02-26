# ABOUT: statistics

# This library contains functions for making mathematical calculations

# mean()
# This is average of the data

### stdev()
# The standard deviation
# This measures how much data points in a set vary from the average of the
# data set.

# A Low standard deviation means that the data 
# is tighly clustered around the average.

# A high standard deviation indicates the data is more spread out.

#______________________________________________________________________________

import statistics


def main() -> None:
    new_list = [100, 101, 102, 103, 104]
    mean_of_list = statistics.mean(new_list)

    print(f"mean_of_list: {mean_of_list}")
    # mean_of_list: 102

    standard_deviation_of_list = statistics.stdev(new_list)
    print(f"standard_deviation: {standard_deviation_of_list}")
    # standard_deviation_of_list: 1.5811388300841898

if __name__ == "__main__":
    main()
