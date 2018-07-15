# goal:

input = {'Duration', 'F0', 'F1', 'F2', 'F3'}
#output: dictionary {'Duration' : 0, 'F0' : 1, 'F1', 'F2' : 2, 'F3' : 3}

output = {f : i for i, f in enumerate(input)}

print(output)
print(type(output))