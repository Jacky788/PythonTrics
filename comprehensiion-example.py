def main():
    seq = range(11)
    seq2 = [(x, x**2) for x in seq]
    seq3 = {x for x in 'bbbaaa' if x not in 'pd'}  # this will be a set!
    print(seq2)
    print(seq3)

if __name__ == '__main__': main()