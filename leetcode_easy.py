import collections


def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    cleaned_emails = [0] * len(emails)
    for g in range(len(emails)):
        iterate_1 = emails[g].split('@')
        iterate_2 = iterate_1[0].split('+')
        to_replace = [i for i, x in enumerate(iterate_2[0]) if x == '.']
        char_list = list(iterate_2[0])
        for k in to_replace:
            char_list[k] =  ""
        cleaned_emails[g] = "".join(char_list + ['@'] + list(iterate_1[1]))

    unique_list = []
    for b in range(len(cleaned_emails)):
        if cleaned_emails[b] not in unique_list:
            unique_list.append(cleaned_emails[b])

    return len(unique_list)

test_case = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]


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


# a default dict lets you add values not encountered before without a KeyError
def containsNearbyDuplicates(nums, k):
    d, flag = collections.defaultdict(int), False  # hashset, flag
    for i, a in enumerate(nums):
        if a in d:  # appeared more than once
            if i - d[a] <= k:
                flag = True
        d[a] = i  # value: position
    return flag

# twoSum Easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_one, val_one in enumerate(nums): 
            for idx_two, val_two in enumerate(nums):
                if idx_one != idx_two:
                    sum_value = val_one+val_two 
                    if sum_value == target:
                        return [idx_one, idx_two]
