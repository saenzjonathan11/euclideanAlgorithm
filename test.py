import termtables as tt
s = [1, 1]
q = [1, 6, 2, 6]
qRow = [None, None] + q
rows, col = [2, len(q) + 2]

table = [[0 for i in range(col)] for j in range(rows)]
table[0][1] = 1
table[1][0] = 1

for row in table:
    for i in range(col):
        if i > 1:
            row[i] = row[i - 1] * q[i - 2] + row[i - 2]
    print("\n")
bList = []
for i in range(0, col):
    bList.append(s[0] * table[0][i] + s[1] * table[1][i])
print(bList)
header = qRow
data = table

string = tt.to_string(
    data,
    header=qRow,
    style=tt.styles.ascii_thin_double,
    padding=(0, 1),
)
# print(string)

ll = [[1, 2], [2, 4]]
print(ll)
ll.append([55, 66])
print(ll)