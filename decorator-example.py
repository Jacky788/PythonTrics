import time

# def f1(f):
#     def f2():
#         print('This is before function call')
#         f()
#         print('this is after function call')
#     return f2
# @f1
# def f3():
#     print('this is f3')

# f3()  # f3's original form is no longer available

# print('--------------------------------------')

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print('Elapsed time: {} ms'.format((t2 - t1) * 1000))
    return wrapper

@elapsed_time
def big_sum():
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print('Big sum: {}'.format(sum(num_list)))

def main():
    big_sum()

if __name__ == '__main__': main()