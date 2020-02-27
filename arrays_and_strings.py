import numpy as np

# 1.1 to find unique characters, do a list count of all alphabets. if count >=2 then not unique.
def unique_characters(str1):
    c_str = str1.lower()
    for k in range(len(c_str)):
        for g in range(k+1, len(c_str)):
            if c_str[k] == c_str[g]:
                return False
    return True


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
    if odds_evens[0] % 2 != 0 or odds_evens[0] == 0:
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


# 1.6 challenge: transform aaabbbccaa to a3b3c2a2
def string_compression(str1):
    idx = [0] * len(str1)
    for i in range(len(str1)-1):
        if str1[i] != str1[i+1]:
            idx[i] = 1
    break_points = [i+1 for i, x in enumerate(idx) if x == 1]
    break_points.insert(0, 0)
    break_points.append(len(str1))
    number_counts = list(np.diff(break_points))
    final_string = ""
    for i in range(len(break_points)-1):
        final_string += str1[break_points[i]] + str(number_counts[i])
    if len(final_string) < len(str1):
        return final_string
    else:
        print('cannot compress string further')


def moving_average(array):
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_array[i] = sum(array[0:i+1]) / (i+1)
    return new_array

def heightChecker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    number_changes = 0
    s_heights = sorted(heights)
    for k in range(len(heights)):
        if heights[k] - s_heights[k] != 0:
            number_changes += 1
    return number_changes


def uniqueOccurrences(arr):
    occurence_list = []
    unique_list = []
    for x in arr:
        if x not in unique_list:
            unique_list.append(x)
    for b in unique_list:
        if arr.count(b) not in occurence_list:
            occurence_list.append(arr.count(b))
        else:
            return False
    return True




