farm_animals = ['cow', 'pig', 'horse']
domestic_animals = ['dog', 'cat', 'gold fish']
zoo_animals = ['lion', 'elephant', 'gorilla']
animals = farm_animals + domestic_animals + zoo_animals
animals = farm_animals + domestic_animals + zoo_animals
for i in range(len(animals)):
    print('animal index{0}:value{1}'.format(i, animals[i]))

animals_dictionary = {}
animals_list = ['cow', 'pig', 'horse']
other_list = [4567, [4, 'turn', 7, 'left'], 'Animals are great.']

for i in range(len(animals_list)):
    if animals_list[i] not in animals_dictionary:
        animals_dictionary[animals_list[i]] = other_list[i]  # 字典的赋值
for key, value in animals_dictionary.items():
    print('{0}:{1}'.format(key, value))

list_of_lists = [['cow', 'pig', 'horse'], ['dog', 'cat', 'gold fish'], ['lion', 'elephant', 'gorilla']]
for item in list_of_lists:
    lenght = len(item)
    strparam = ''
    for index in range(lenght):
        if index < lenght - 1:
            strparam = strparam + str(item[index]) + ','  # 注意变量命名不要使用str等
        else:
            strparam = strparam + str(item[index]) + '\n'
    print(strparam)
