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
                                        'quantity': (product[1]),
                                        'measure': product[2].strip()})
            file.readline()
        return result


catalog = catalog_reader(file_name)
pprint(catalog)


