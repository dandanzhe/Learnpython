#Given the numerical series as argument. Write a function to move all zeros to the end non-zero elements will be sorted into their natural order (from smaller to bigger).
#For instance: Given numbers (0, 3, 0, 1, 9, 6). Your function should return an array of numbers: [1, 3, 6, 9, 0, 0].
#Note: You must do this in-place without making a copy of the array. Don't use .sort & .sort! methods. Main idea of this kata is realisation algo without a built-in methods.


def move_zeroes(*args):
    a=[]
    nu=0
    for i in args:
        if i==0:
            nu += 1
        else:
            a.append(i)
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                b=a[i]
                a[i]=a[j]
                a[j]=b
    for i in range(nu):
        a.append(0)
    return a
