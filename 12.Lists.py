if __name__ == '__main__':
    N = int(input())
    list_1 = []
    for i in range(N):
        command = input().split()
        if command[0]=="append":
            list_1.append(int(command[1]))
        elif command[0]=="insert" :
            list_1.insert(int(command[1]),int(command[2]))
        elif command[0]=="remove":
            list_1.remove(int(command[1]))
        elif command[0]=="sort":
            list_1.sort()
        elif command[0]=="pop":
            list_1.pop()
        elif command[0]=="reverse":
            list_1.reverse()
        elif command[0]=="print":
            print(list_1)                       
            
        