if __name__ == '__main__':
    list_1 =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_1.append([name,score])
    minimum = 10**6
    second_minimum = 10**6
    for j in list_1:
        if j[1]<minimum:
            second_minimum=minimum
            minimum=j[1]
        else:
            if  minimum<j[1] and second_minimum>j[1]:
                second_minimum=j[1]
    names =[]            
    for k in list_1:
        if k[1]==second_minimum:
            names.append(k[0])
        names.sort()
    for n in names:
        print(n)
        