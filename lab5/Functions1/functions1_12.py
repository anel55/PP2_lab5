def histogram(number_list):

    number_list = list(number_list.split())
    integer_number_list = []

    for i in number_list:
        integer_number_list.append(int(i))

    for i in range(len(integer_number_list)):
        print(integer_number_list[i] * "*")

string = input()
histogram(string)