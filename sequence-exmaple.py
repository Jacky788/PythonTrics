x = [ 1, 2, 3, 4, 5] # list is mutable
x[2] = 42
for i in x:
    print('i is {}'.format(i))

y = (1, 2 , 3, 4, 5)
# y[2] = 10  # tuple is immutable
# one should prefer tuple unless one knows the values need to be changed in the container

dict = {'zero': 0, 'one' : 1, 'two': 2, 'three': 3}
dict['zero'] = -1 # dictionrary is mutable
for k, v in dict.items():
    print('k: {}, v:{}'.format(k, v))


x = (1, 'two', 3.0, [4, 'four'], 5)
print(type(x))
if isinstance(x, tuple):
    print("tuple")
else:
    print("nope")





