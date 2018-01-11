def is_unique_char(string):
    # ASCII code라고 가정했을 때 유일한 문자의 집합이 128개를 넘길 수 없다.
    '''
    시간복잡도 O(c), c는 문자열의 크기
    공간복잡도 O(1), 왜냐하면 128로 사이즈가 고정이기 때문이다.
    '''
    if len(string) > 128: return False
    char_set = set()
    for char in string:
        if char in char_set: return False
        char_set.add(char)
    return True


def is_unique_char2(string):
    '''
    string이 a~z까지의 소문자만 사용한다고 가정했을 때의 비트연산
    1. 문자열을 순회하면서 각 문자와 'a'와의 차이를 연산한다.
    2. 위에서 구한 값만큼 1을 비트 이동시킨다음, 그 값을 checker와 &연산해서 그 값이 0보다 크면 False를 리턴한다.
    3. 그렇지 않다면 checker를 위의 값에서 &연산을 |연산으로 바꾼 값으로 업데이트한다.

    위와 같은 비트연산으로 중복체크가 가능한 이유는
    알파벳 a와의 거리를 통해 특정 숫자에 대한 정보를 숫자로 담고 그 만큼 << 만큼 시켜주면 이진법으로 표기된
    각 자리수로 해당 알파벳이 나타났는지 알 수 있기 때문이다.
    예를 들어, abcde라는 string 값이 주어지면,
    a : checker = 0, 거리는 0이므로 연산할 값은 1-> &연산 결과는 0, chekcer는 1로 업데이트
    b : checker = 1, 거리는 1이므로 연산할 값은 10 -> &연산 결과는 0, checker는 11로 업데이트...
    이런 식으로 특정 거리의 알파벳이 이전에 나온적이 없다면 &연산의 결과는 0이 되고 추가되는 알파벳의 정보가
    |연산의 결과로 저장되게 되는 것이다.

    시간복잡도 O(n)
    공간복잡도 O(1) >> 이번에는 set() 을 사용해서 알파벳을 미리 저장하지 않아도 된다.
    '''
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if checker & (1 << val): return False
        checker |= (1 << val)
    return True

print(is_unique_char2('bcdeab'))
