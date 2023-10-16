def unique_list(number_list):
  unique_list = []
  for i in number_list:
    if i not in unique_list:
      unique_list.append(i)
  return unique_list

numbers = list(input())
print(unique_list(numbers))