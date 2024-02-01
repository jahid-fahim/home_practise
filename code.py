t = int(input())

while t:
    len = int(input())
    str = input()
    lst = list(str)
    lst.sort()
    print(ord(lst[len-1])-97+1)
    t-=1

