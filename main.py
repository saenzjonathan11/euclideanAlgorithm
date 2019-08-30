# This is a script is designed to output
# the gcd of two number. It used the Euclidean alogrithm
# and outputs the list of coefficents and each step of
# the alogrith equation in a file called GCD.txt

import math


def main(s):
    f = open("GCD.txt", "w")
    for i in range(0, len(s)):
        a = s[i][0]
        b = s[i][1]
        q = math.floor(a/b)
        r = a - q*b
        out = "{:d} = {:d}({:d}) + {:d}".format(int(a), int(b), int(q), int(r))
        # print(out)
        f.write(out + "\n")
        ll = [q]
        while r != 0:
            a = b
            b = r
            q = math.floor(a/b)
            r = a - q*b
            out = "{:d} = {:d}({:d}) + {:d}".format(int(a), int(b),
                        int(q), int(r))
            # print(out)
            f.write(out + "\n")
            ll.append(q)
        # print(ll)
        ll = [int(i) for i in ll]
        f.write(str(ll) + "\n\n")


if __name__ == "__main__":
    # Greatest number of LHS
    s1 = [291, 252]
    s2 = [85652, 16261]
    s3 = [139024789, 93278890]
    s4 = [16534528044, 8332745927]

    s = [s1, s2, s3, s4]

    # use fo user input
    # num = int(input("Enter the number of sets"))
    # s = []
    # for i in range(0, num):
    #     a = int(input("Enter Greatest number"))
    #     b = int(input("Enter 2nd Greatest number"))
    #     s.append([a,b])

    main(s)

