# Mathematical Operations
# Practice utilizing mathematical operations from numpy

import numpy as np

def main():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10]

    a1 = np.array(l1)
    a2 = np.array(l2)

    print(l1 + l2)
    print(a1 * a2)

    b1 = np.array([1,2,3])
    b2 = np.array([[1],
                  [2]])

    print(b1 + b2)


if __name__ == "__main__":
    main()