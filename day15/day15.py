#!/usr/bin/env python3

s = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1"""

s = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
import re

from collections import namedtuple
from operator import mul
from functools import reduce

Ingredient = namedtuple('Ingredient', 'name capacity durability flavor texture calories teaspoons')



ingredients = []
ingr_types = ['capacity', 'durability', 'flavor', 'texture']

def calculate(attr):
    val = 0
    for ing in ingredients:
        if ing.name == 'Butterscotch':
            val += int(getattr(ing, attr))*ing.teaspoons
        elif ing.name == 'Cinnamon':
            val += int(getattr(ing, attr))*ing.teaspoons
    return val

def main(s):
    for line in s.splitlines():
        ing_args = re.search(r'(\w+).* (-?\d+).* (-?\d+).* (-?\d+).* (-?\d+).* (-?\d+)', line).groups()
        print(ing_args)
        ing_args = list(ing_args)
        ing_args.append(0)
        ingredients.append(Ingredient._make(ing_args))
    ingredients[0].teaspoons = 44
    ingredients[1].teaspoons = 56


    # for attr in ingr_types:
    #     for ing in ingredients:
    #         print(getattr(ing, attr))
    #print([calculate(attr) for attr in ingr_types])
    ls = [calculate(attr) for attr in ingr_types]
    total = reduce(mul, ls, 1)


    print(total)

if __name__ == "__main__":
    main(s)
