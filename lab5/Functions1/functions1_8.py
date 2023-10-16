def spy_game(list_of_nums):
    count=0
    for i in list_of_nums:
        if(i==0 and count==0):
            count=1
        if(i==0 and count==1):
            count=2
        if(i==7 and count ==2):
            count = 3
    if(count == 3):
        return True
    else:
        return False

print("Enter size of list")
n = int(input())
print("Enter elements of list")
list = []
for i in range(n):
    elemtns = int(input())
    list.append(elemtns)
print(spy_game(list))