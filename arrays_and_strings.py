# 1.1 to find unique characters, do a list count of all alphabets. if count >=2 then not unique.
def unique_characters(str):
    c_str = str.lower()
    template = 'abcdefghijklmnopqrstuvwxyz'
    for k in range(len(template)):
        if c_str.count(template[k]) >= 2:
            return k, False


test_str = 'dsvnadnvkasnsdanfadf'
# 1.2 pretty easy, sort string and check if they're equal
def permutation_check(str1,str2):
    if sorted(str1) != sorted(str2):
        return False
    else:
        return True

t_str = 'derpatologist'
t_str2 = 'tologderpaist'
permutation_check(t_str,t_str2)


# 1.3 strategy: transform string to list, then using enumerate find the idx
# of the 'replace' char, then replace and join str
def char_replacement(str, to_replace, replacement):
    char_list = list(str)
    indices = [idx for idx, value in enumerate(char_list) if value == to_replace]
    for g in range(len(indices)):
        char_list[indices[g]] = replacement
    output = "".join(char_list)
    return output

t_str = ' derp is derp derp'
char_replacement(t_str, ' ', '%30')


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


# 1.5 strategy: 1) if == num characters 2) if abs(num_char(str1) - num_char(str2))==1, else FALSE
# building on 1) enumerate match?
def one_away(str1, str2):
    roll_idx = [0] * min([len(str1),len(str2)])
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                roll_idx[i] = 0
            else:
                roll_idx[i] = 1
        if sum(roll_idx) <= 1:
            return True
        else:
            return False
    else:
        print('error')

one_away('derp','perp')



