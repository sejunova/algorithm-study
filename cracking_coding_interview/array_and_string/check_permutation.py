def check_permutation(one, other):
    '''

    :param one: string
    :param other: string
    :return: return True if two params are permutations, otherwise return False

    Time complexity: O(n) where n is the length of either string
    Space complexity: O(n) where n is the length of either string
    '''
    if len(one) != len(other): return False
    one_chars = char_counter(one)
    other_chars = char_counter(other)
    return one_chars == other_chars


def char_counter(string):
    '''
    return dict that has counters of each characters in string input.
    '''

    ret = {}
    for char in string:
        if char in ret:
            ret[char] += 1
        else:
            ret[char] = 1
    return ret

def check_permutation2(one, other):
    if len(one) != len(other): return False
    return sorted(one) == sorted(other)

def check_permutation3(one, other):
    '''
    removed unnecessary redundancy from check_permutation solution by checking
    whether there is a char used in other not used in one or more used that one.
    Also Space complexity reduced by half as I made only one dict to hold only one string.
    '''
    if len(one) != len(other): return False
    chars = {}
    for char in one:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char in other:
        if char in chars:
            chars[char] -= 1
            if chars[char] < 0:
                return False
        else:
            return False

    return True


print(check_permutation3('abcdss', 'dbacss'))
