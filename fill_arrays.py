# Full Arrays
# Fill a sample data set in an array utilizing numpy

import numpy as np

def main():
    a = np.full((2,3,4), 9) # Creates two 3x4 arrays filled with 9
    print(a)

    a = np.empty((5,5,5)) # Allocates memory to five 5x5 arrays

    x_values = np.arange(0, 1000, 5) # Generate a list of numbers from 0 - 1000, skipping by 5
    print(x_values)

    y_values = np.linspace(0, 1000, 2) # Solely creates two values based amongst an event distribution between the minimum and maximum values
    print(y_values)

    print(np.isnan(np.nan)) # Checks if the input is "Not A Number"
    print(np.isinf(np.inf)) # Checks if the input is "Infinity"
    print(np.isnan(np.sqrt(-1)))
    print(np.isinf(np.array([10]))/0)


if __name__ == "__main__":
    main()