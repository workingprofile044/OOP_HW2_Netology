def read_recipe_file(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for i in range(ingredient_count):
                ingredient_line = f.readline().strip().split(' | ')
                ingredient_name = ingredient_line[0]
                ingredient_quantity = int(ingredient_line[1])
                ingredient_unit = ingredient_line[2]
                ingredients.append({'ingredient': ingredient_name,
                                    'quantity': ingredient_quantity,
                                    'measure': ingredient_unit})
            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book

cook_book = read_recipe_file('recipes.txt')
#print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name not in shop_list:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[name]['quantity'] += quantity
    return shop_list

dishes = ['Омлет', 'Запеченный картофель']
person_count = 4
shop_list = get_shop_list_by_dishes(dishes, person_count)
#print(shop_list)

import codecs

file1 = "1.txt"
file2 = "2.txt"
file3 = "3.txt"

def get_num_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

files = [(file1, get_num_lines(file1)), (file2, get_num_lines(file2)), (file3, get_num_lines(file3))]

files.sort(key=lambda x: x[1])

merged_file = "result.txt"

with open(merged_file, 'w', encoding='utf-8') as f:
    for i, file in enumerate(files):
        filename = file[0]
        num_lines = file[1]
        f.write(f"Файл {filename} - {num_lines} строк\n")
        with codecs.open(filename, 'r', encoding='utf-8') as f1:
            for j, line in enumerate(f1):
                f.write(f"строка {j+1} из файла {filename} - {line}")
        f.write('\n')

with open(merged_file, 'a', encoding='utf-8') as f:
    f.write('\n')