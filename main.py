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
print(shop_list)