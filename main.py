import os
import sys

cwd = os.getcwd()
file_name = 'cookbook.txt'
folder_name = 'files'
full_file_name = os.path.join(cwd, folder_name, file_name)

try:
    file = open(full_file_name, 'rt', encoding='utf-8')
except FileNotFoundError:
    print(f'File "{full_file_name}" not found or access denied')
    sys.exit(1)

cook_book = {}

for dish in file:
    ingredients_count = int(file.readline())
    ingredients = []
    for _ in range(ingredients_count):
        ingredient_name, quantity, measure = file.readline().split(' | ')
        ingredients.append({'ingredient_name': ingredient_name.strip(),
                            'quantity': int(quantity),
                            'measure': measure.strip()})
    cook_book[dish.strip()] = ingredients
    file.readline()

file.close()
print(cook_book)

