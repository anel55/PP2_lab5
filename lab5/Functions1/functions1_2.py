def farenheit_to_celsium(temp_f):
    temp_c = (5/9)*(temp_f - 32)
    return temp_c
farenheits = float(input())
print(farenheit_to_celsium(farenheits))