mat = [[0, 9, 75, 0, 0], [9, 0, 95, 19, 42], [75, 95, 0, 51, 66], [0, 19, 51, 0, 31], [0, 42, 66, 31, 0]]
v = 5
l = []
cost = 0
s = 0
k = 0
print("The MST is : ")
while len(l) < (v - 1):
    m = 999999
    l.append(s)
    for i in l:
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                continue
            elif mat[i][j] < m and j not in l:
                m = mat[i][j]
                s = j
                k = i
    print(k,"-->",s," : ",m)

    cost += m
print("Total cost is: ")
print(cost)