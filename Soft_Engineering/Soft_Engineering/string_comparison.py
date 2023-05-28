def compare_strings(str1, str2):
    i = 0
    while i < len(str1) and i < len(str2):
        if str1[i] != str2[i]:
            return ord(str1[i]) - ord(str2[i])
        i += 1
    if len(str1) > len(str2):
        return 1
    elif len(str1) < len(str2):
        return -1
    else:
        return 0
