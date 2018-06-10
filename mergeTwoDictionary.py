dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
mergedDic1 = {**dict1, **dict2}
print(mergedDic1)
# you will see {'a': 1, 'b': 3, 'c': 4}

mergedDic2 = {**dict2, **dict1}  # the trick here is which one you put front
print mergedDic2)

# {'b': 2, 'c': 4, 'a': 1}

