from pprint import pprint

file_name = 'recipes.txt'

def catalog_reader(file_name):
    with open(file_name, encoding='UTF-8') as file:
        result = {}
        for line in file:
            dish = line.strip()
            result[dish] = []
            for item in range(int(file.readline())):
                product = file.readline().split(' | ')
                result[dish].append({'ingredient_name': product[0],
                                        'quantity': (int(product[1])),
                                        'measure': product[2].strip()})
            file.readline()
        return result


catalog = catalog_reader(file_name)
pprint(catalog) # проверка задания 1


def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    cook_book = catalog_reader(file_name)
    for item in dishes:
        if item in cook_book:
            for i in range(len(cook_book[item])):
                name = cook_book[item][i]['ingredient_name']
                if cook_book[item][i]['ingredient_name'] not in dishes_dict:
                    dishes_dict.setdefault(cook_book[item][i]['ingredient_name'],
                                           {'measure': cook_book[item][i]['measure'],
                                            'quantity': int((cook_book[item][i]['quantity']) * person_count)})
                else:
                    dishes_dict[name]['quantity'] *= 2
    return dishes_dict

menu1 = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(menu1) # проверка задания 2



