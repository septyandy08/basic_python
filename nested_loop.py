for i in range(3):
    print("i: {}".format(i))
    for j in range(3):
        print("j: {}".format(j))

for i in range(2):
    for j in range(3):
        print("{}.{}".format(i+1, j+1), end = " ")
    print()

count = 1
for baris in range(5):
    for kolom in range(5):
        print(count, end = " ")
        count = count + 1
    print()