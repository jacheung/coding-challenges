# 1.1 to find unique characters, do a list count of all alphabets. if count >=2 then not unique.
def unique_characters(str1):
    c_str = str1.lower()
    template = 'abcdefghijklmnopqrstuvwxyz'
    for k in range(len(template)):
        if c_str.count(template[k]) >= 2:
            return template[k], False


# 1.2 pretty easy, sort string and check if they're equal
def permutation_check(str1, str2):
    if sorted(str1) != sorted(str2):
        return False
    else:
        return True


# 1.3 strategy: transform string to list, then using enumerate find the idx
# of the 'replace' char, then replace and join str
def char_replacement(str, to_replace, replacement):
    char_list = list(str)
    indices = [idx for idx, value in enumerate(char_list) if value == to_replace]
    for g in range(len(indices)):
        char_list[indices[g]] = replacement
    output = "".join(char_list)
    return output


# 1.4 strategy: count number of odd alphabet counts. If odd num of odds palindrome = true, else = false.
def palindromic_check(str):
    odds_evens = [0] * 2
    c_str = str.lower()
    template = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(template)):
        num_counter = c_str.count(template[i])
        if num_counter % 2 == 0 and num_counter != 0:
            odds_evens[1] = odds_evens[1]+1
        else:
            odds_evens[0] = odds_evens[0]+1
    if odds_evens[0] % 2 != 0:
        return True
    else:
        return False


# 1.5 strategy:
# 1) if == num characters then compare each character
# 2) if distance between characters is 1 then iteratively delete a single char and compare
# 3) else return False
def one_away(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    roll_idx = [0] * min([len(str1), len(str2)])
    if len(str1) == len(str2):  # 1) if character length is equal
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                roll_idx[i] = 0
            else:
                roll_idx[i] = 1
        if sum(roll_idx) <= 1:
            return True
        else:
            return False
    elif abs(len(str1) - len(str2)) == 1:  # 2) if character length is one difference
        long_str = max([str1, str2], key=len)
        short_str = min([str1, str2], key=len)
        for b in range(len(long_str)):
            mod_str = long_str.replace(long_str[b], '')
            if mod_str == short_str:
                return True
    else:  # 3) else return false
        return False






