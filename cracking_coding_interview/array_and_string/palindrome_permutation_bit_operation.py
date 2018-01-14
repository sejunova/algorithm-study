def palindrome_permutation_bit_operation(string):
    '''
    :param string: accept string only with lower case alphabets.
    Time complexity : O(n) where n is the length of string input.
    Space complexity: O(1), bit_vector and bit_compared are the only space needed
    '''
    bit_vector = 0
    for char in string:
        bit_compared = 1 << (ord(char) - ord('a'))
        if bit_vector & bit_compared:
            bit_vector ^= bit_compared
        else:
            bit_vector |= bit_compared
    return bit_vector == 0 or bit_vector&(bit_vector-1) == 0


print(palindrome_permutation_bit_operation('babea'))