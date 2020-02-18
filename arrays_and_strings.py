# 1.1
def unique_characters(str):
    c_str = str.lower()
    template = 'abcdefghijklmnopqrstuvwxyz'
    for k in range(len(template)):
        if c_str.count(template[k]) >= 2:
            return k, False

# 1.2
def permutation_check(str1,str2):
    if sorted(str1) != sorted(str2):
        return False
    else:
        return True

t_str = 'derpatologist'
t_str2 = 'tologderpaist'
permutation_check(t_str,t_str2)


# 1.3
def char_replacement(str, to_replace, replacement):









sorted(t_str)


unique_characters(t_str)