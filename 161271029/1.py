#1

def main():
    vec = input().split()
    a = int(vec[0])
    b = int(vec[1])
    print("%6d" % a)
    print("%6d" % b)
    print("%6s" % "--")
    print("%6d" % (a * b))


if __name__ == '__main__':
    main()