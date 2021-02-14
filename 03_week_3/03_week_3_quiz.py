for x in range(0, 10):
    print(x)

the_type = {"key_1": "value_1", "key_2": "value_2"}
print(type(the_type))

the_list = ['hello', 25, '5.0', 23.32]
print(the_list)

import pandas as pd 
df = pd.DataFrame(the_list)
print(df)

second_list = [1, 2, 3, 4, 5]
print(second_list * 2)

third_list = [['John', 20], ['Jane', 25], ['Tom', 33], ['Summer', 18]]
print(third_list)
for item in third_list:
    print(item[0] + ' ' + str(item[1]))

for key, item in third_list: print(key, item)

try:
    print('hello' + 12)
catch Exception as e:
    print('There is an error.')