n = int(input())
target = int(input())
myList = [int(ele)for ele in input().split()]

found = False
for i in myList:
    if i == target:
        found = True
        break

if found == True:
    print("yes")
else:
    print("no")