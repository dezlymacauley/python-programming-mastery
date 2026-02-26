Every project has two files:

_______________________________________________________________________________

1. main.py
2. research.ipynb
_______________________________________________________________________________

research.ipynb
```python
# Quantbook
qb = QuantBook()

# Add NVDA
NVDA = qb.add_equity("NVDA")

# History
history = qb.history(qb.securities.keys(), 5, Resolution.DAILY)

# Print index
print(history.index)
```

This code will make a request for 5 daily bars of historical data for 
the Nvidea stock. Then it prints the index of all the bars

The output will look like this:

```
MultiIndex([(NVDA, '2026-02-18 16:00:00'),
            (NVDA, '2026-02-19 16:00:00'),
            (NVDA, '2026-02-20 16:00:00'),
            (NVDA, '2026-02-23 16:00:00'),
            (NVDA, '2026-02-24 16:00:00')],
           names=['symbol', 'time'])
```
_______________________________________________________________________________

You are only allowed to use libraries in QuantConnect that are whitelisted

```
https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/libraries
```

E.g. This is how to import the statistics model

```python
# Import the statistics library
# It contains functions for making mathematical calculations
import statistics

new_list = [100, 101, 102, 103, 104]
mean_of_list = statistics.mean(new_list)

print(mean_of_list)

standard_deviation = statistics.stdev(new_list)
print(standard_deviation)
```

The mean is 102

The standard deviation is 1.5811388300841898

_______________________________________________________________________________

### mean()
- The average of data

### stdev()
- The standard deviation
- This measures how much data points in a set vary from the average of the
data set.

- Low standard deviation means that the data is tighly clustered around the
average.
- High standard deviation indicates the data is more spread out.

_______________________________________________________________________________
