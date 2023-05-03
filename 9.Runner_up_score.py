if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maximum = -10**6
    second_maximum = -10**6
    for i in arr:
        if i>maximum:
            second_maximum=maximum
            maximum=i
        else:
            if maximum>i and second_maximum<i :
                second_maximum=i   
                
    print(second_maximum)            