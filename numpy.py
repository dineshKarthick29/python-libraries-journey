import numpy as np

"""
#print(np.__version__)

arr=[1,2,3,4,5]

arr*=2
print(arr)

array = np.array(arr)
array*=2
print(array)


a=np.array([1,2,3,4,5])
print(a)
print(array.dtype)
print(array.nbytes)


array=np.array([1,2,3,4,5],dtype=np.int8)
print(array)
print(array.dtype)
print(array.nbytes)



flort_demo= np.array([5.1,6.2,7.3,8.4,9.5,1.0])
print(flort_demo)
print(flort_demo.dtype)
print((flort_demo.nbytes))


string_demo=np.array(["dinesh","karthick","yogitha","samar","suganth"])
print(string_demo)
print(string_demo.dtype)
print(string_demo.nbytes)

"""

# multidimenstions and shape ,reshape

sk = np.array(5)
print(sk)
print(sk.ndim)

dimen = np.array([5, 7, 8])
print(dimen)
print(dimen.ndim)

b = np.array(
    [
        [2, 3, 4],
        [
            5,
            6,
            7,
        ],
    ]
)
print(b)
print(b.dtype)
print(b.nbytes)
print(b.ndim)




