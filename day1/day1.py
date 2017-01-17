#!/usr/bin/env python3

def main(floor_str):
    return floor_str.count('(') - floor_str.count(')')

def my_func(count, mychar):

    if mychar == '(':
        count += 1
    elif mychar == ')':
        count -= 1

    return count

def find_fllor_minus1(floor_str):
    count = 0
    istr = iter(floor_str)
    index = 0
    while count != -1:
        index += 1
        my_char = istr.__next__()
        count = my_func(count, my_char)
    return index


if __name__ == "__main__":
    with open('1.in', 'r') as f:
        file_str = f.read()
        print(main(file_str))
        print(find_fllor_minus1(file_str))
