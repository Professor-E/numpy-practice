# Arrays
# Create and analyze data sets utilizing arrays and numpy

import numpy as np

def main():
    # Code
    a = np.array([1,2,3,4,5])
    print(type(a))
    print(a)
    print(a[1])
    print(a[1:])
    print(a[:-2])

    a[2] = 28
    print(a)

    a_nul = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])
    print(type(a_nul))
    print(a_nul)
    print(a_nul[0])
    print(a_nul[0, 1])
    print(a_nul.shape)
    print(a_nul.ndim) # Two total lists
    print(a_nul.size) # Tptal number of elements
    print(a_nul.dtype)

    b = np.array([[1,2,3],
                 [4,"Hello",6],
                 [7,8,9]]) # The array is typcasted into strings, due to the inclusion of a string
    
    print(a.dtype) 


if __name__ == "__main__":
    main()