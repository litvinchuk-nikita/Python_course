import sys
with open('bakery.csv', 'a', encoding='utf-8') as f:
    add_sale = sys.argv[1]
    f.write(f'{add_sale}\n')
