import termtables as tt

q = [1, 6, 2, 6]
qRow = [None, None] + q
rows, col = [2, len(q) + 2]

table = [[0 for i in range(col)] for j in range(rows)]
table[0][1] = 1
table[1][0] = 1

for row in table:
    for i in range(col):
        if i > 1:
            row[i] = row[i-1]*q[i-2] + row[i - 2]
    print("\n")

header = qRow
data = table

string = tt.to_string(
    data,
    header=qRow,
    style=tt.styles.ascii_thin_double,
    padding=(0, 1),
)
print(string)
