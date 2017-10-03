def oddEven():
    for i in range(1,2001):
        if i%2 == 0:
            print "Number is {}. This is an even number".format(i)
        else:
            print "Number is {}. This is an odd number".format(i)

oddEven()

def multiply(arr, x):
    newStr = []
    for i in arr:
        newStr.append(i*x)
    return newStr

a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiplier(arr):
    newArr = []
    for i in arr:
        entry =[]
        for count in range(0, i):
            entry.append(1)
        newArr.append(entry)
    return newArr

x = layered_multiplier(multiply([2,4,5],3))
print x