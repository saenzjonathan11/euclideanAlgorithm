# This is a script is designed to output
# the gcd of two number. It used the Euclidean alogrithm
# and outputs the list of coefficents and each step of
# the alogrith equation in a file called GCD.txt

import math
import termtables as tt


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
        f.write(str(ll) + "\n")

        llRow = [None, None] + ll
        rows, col = [2, len(ll) + 2]

        table = [[0 for i in range(col)] for j in range(rows)]
        table[0][1] = 1
        table[1][0] = 1

        table2 = [[0 for i in range(col)] for j in range(rows)]
        table2[0][0] = 1
        table2[1][1] = 1
        
        for row in table:
            for i in range(col):
                if i > 1:
                    row[i] = row[i-1]*ll[i-2] + row[i - 2]

        for row in table2:
            for i in range(col):
                if i > 1:
                    row[i] = row[i - 2] - row[i-1]*ll[i-2]

        data = table
        string = tt.to_string(
            data,
            header=llRow,
            style=tt.styles.ascii_thin_double,
            padding=(0, 1),
        )
        f.write(string)
        f.write("\n\n")

        data = table2
        string = tt.to_string(
            data,
            header=llRow,
            style=tt.styles.ascii_thin_double,
            padding=(0, 1),
        )
        f.write(string)
        f.write("\n\n")


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

