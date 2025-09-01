# Array Functions
# Familiarization with numpy's array functions

import numpy as np

def main():
    a = np.array([[1,2,3],
                 [4,5,6]])

    print(np.append(a, [7,8,9]))
    print(np.insert(a, 3, [4,5,6]))
    print(a) # Will not save to the array "a," as it is not being assigned to
    print(np.delete(a, 0))
    print(np.delete(a, 1))
    print(np.delete(a, 2))
    print(np.delete(a, 1, 0)) # Deletes by row and column; delete row 1
    print(np.delete(a, 0, 0))
    print(np.delete(a, 1, 1)) # Delete column 1

    a = np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20]])
    
    print(f"The shape of the matrix is: {a.shape}")
    print(a.reshape(5,4)) # Resize the rows and columns (*Transpose*)
    print(f"The shape of the matrix is: {a.shape}")
    print(a.reshape(1,20))
    print(a.reshape(20,1))
    print(a.reshape(2,2,5))
    print(a.resize((10,2)))
    print(a.flatten()) # Returns a COPY of a 1 row matrix, it will not change value
    print(a.ravel()) # Returns a VIEW of the array (the actual array), will update if values are changed

    a = np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20]])
    
    print(a.transpose())
    print(a.T) # Also transposes the matrix (swaps rows x columns)
    print(a.swapaxes(0,1)) # Solely swaps rows 1 & 2

    a1 = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
    
    a2 = np.array([[11,12,13,14,15],
                  [16,17,18,19,20]])
    
    # Inputs are tuples
    print(np.concatenate((a1, a2), axis=0)) # Add two rows from the first axis of the second matrix
    print(np.concatenate((a1, a2), axis=1)) # Add two rows from the first axis of the second matrix
    a = np.stack((a1, a2)) # Stack with a space in between the arrays, adding a new dimension to the array
    print(a)
    
    a = np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20]])
    
    print(np.split(a, 2, axis=0))
    print(np.split(a, 4, axis=0))

    print(a.min())
    print(a.max())
    print(a.mean())
    print(a.std())
    print(a.sum())
    print(np.median(a))

    number = np.random.randint(100) # Generate a random number from 0 - 99
    print(number)

    numbers = np.random.randint(100, size=(2,3,4)) # Generates random integers 0 - 99 in two 3x4 arrays
    print(numbers)

    binomial = np.random.binomial(10, p=0.5, size=(5, 10))
    print(binomial)

    choice = np.random.choice([10,20,30,40,50], size=(5, 10)) # Randomly chooses numbers out of the provided matrix and generates a 5x10 matrix using the randomly chosen numbers
    print(choice)

    # np.save("filename.npy", a) # Saves the binary file with the given array/matrix provided
    # np.load("filename.npy") # Loads the saved array into the given program


if __name__ == "__main__":
    main()

