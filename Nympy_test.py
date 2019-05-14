import numpy as np

def main():
    #n_dimentional array
    arr1 = np.array([1, 2, 3])#a array of 3 elements, 1D
    arr2 = np.array([ [1,2,3], [4,5,6] ])#a array of 6 elements, 2D

    #messing with the minimum dimension
    min_dimen = np.array([1,2,3], ndmin= 2)
    # the array has a min dimension of 2

    #with complex type of data
    comp_data = np.array([1,2,3], dtype = complex)
    #this array is of type complex, so the output will reflect that

    print ("The array in 1D with 3 elements: ")
    print (arr1)
    print ("The array in 2D with 6 elements: ")
    print (arr2)
    print("Changing the shape of the array: ")
    arr2.shape = (3, 2)#the shape function
    print(arr2)
    print ("The array with a min of 2D, elements only in the first dimension: ")
    print (min_dimen)
    print ("The array of complex data type: ")
    print (comp_data)
    print ("The size of each item in the complex data array is (bytes): ")
    print (comp_data.itemsize)

    #create a 1D array
    _1darr = np.arange(30)
    _1darr.ndim
    print(_1darr)

    #reshape it
    #2x3x5 arrays within a array
    reshape = _1darr.reshape (2, 3, 5)
    print (reshape)

    #converting a array to a ndarray
    a = [1,2,3]
    nda = np.asarray(a)
    print ("a array converted to ndarray is: ")
    print (nda)
    print ("the array with a complex dtype: ")
    print ( np.asarray(a, dtype = complex) )
    

if __name__ == "__main__":
    main()
