def one_away(str1, str2):
    '''
    Time Complexity: O(n), where n is the length of either string input
    Space Complexiy: O(1)
    '''
    if abs(len(str1) - len(str2)) >= 2 or str1 == str2:
        return False
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i] and str1[i+1:] != str2[i+1:]:
                return False
        return True
    return is_added_or_deleted(str1, str2)



def is_added_or_deleted(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    for i in range(len(str2)):
        if str1[i] != str2[i] and str1[i + 1:] != str2[i:]:
            return False

    return True


print(one_away('palb', 'pale'))
