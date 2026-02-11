lst = list(map(int,input().split()))
lst = lst[5::6]
javab = [x for x in lst if x % 6 == 0]
print(*javab)