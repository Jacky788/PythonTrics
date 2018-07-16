def main():
    for i in inclusive_range(0, 5, 2):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError('expected at least 1 argment, got {}'.format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('expected at most 3 argment, got {}'.format(numargs))
    
    # generator
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()