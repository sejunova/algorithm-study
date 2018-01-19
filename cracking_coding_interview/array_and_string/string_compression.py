def string_compression(string):
    cur_char, char_count = string[0], 1
    compression_list = []
    for i in range(len(string)):
        if len(compression_list) > len(string):
            return string
        if i + 1 == len(string):
            compression_list.append(cur_char)
            compression_list.append(str(char_count))
            break

        if cur_char == string[i + 1]:
            char_count += 1
        else:
            compression_list.append(cur_char)
            compression_list.append(str(char_count))
            cur_char = string[i + 1]
            char_count = 1

    return ''.join(compression_list)


print(string_compression('abceeddaa'))
