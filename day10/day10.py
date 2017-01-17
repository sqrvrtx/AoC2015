"""

    1 becomes 11 (1 copy of digit 1).
    11 becomes 21 (2 copies of digit 1).
    21 becomes 1211 (one 2 followed by one 1).
    1211 becomes 111221 (one 1, one 2, and two 1s).
    111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 1113222113.
"""
import re
def join_list(ls):
    nls = []
    for fragment in ls:
        nls.append(str(len(fragment)) + fragment[0])
    return ''.join(nls)

def split_list(s):
    return re.findall(r'1+|2+|3+|4+|5+|6+|7+|8+|9+', s)

def main(inp, num_iterations):

    for i in range(num_iterations):
        ilist = split_list(inp)
        inp = join_list(ilist)

    return inp

if __name__ == "__main__":

    print(main('1', 5))
    print(len(main('1113222113', 40)))
    print(len(main('1113222113', 50)))
    # assert main('1') == '11'
    # assert main('111221') == '312211', main('111221')
