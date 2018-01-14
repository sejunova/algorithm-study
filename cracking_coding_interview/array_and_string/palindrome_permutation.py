def palindrome_permutation(string):
    '''
    Time complexity : O(n) where n is the length of string input.
    Space complexity: O(n) where n is the length of string input.
    '''
    string = string.replace(" ", "").lower()
    chars_dict = char_counter(string)
    odd_count = 0
    for val in chars_dict.values():
        if val % 2 == 1:
            if len(string) % 2 == 0:
                return False
            else:
                odd_count += 1
                if odd_count > 1:
                    return False
    return True


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


print(palindrome_permutation('b a'))
