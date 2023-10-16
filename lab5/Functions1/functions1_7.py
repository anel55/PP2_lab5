def has__33(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        if list_of_numbers[i] == list_of_numbers[i+1] == 3:
            return True
    return False

list = []
print("Enter a number of elements in list")
n = int(input())
print("Enter elements of list")
for i in range(0, n):
    elements = int(input())
    list.append(elements)
print(has__33(list))