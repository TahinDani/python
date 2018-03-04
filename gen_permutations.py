# Generates all possible n length permutations of 1 and 0


def permutations_recur(lst, num, max_depth, result_list, depth=0):
    if depth < max_depth:
        lst.append(num)
        depth += 1
        permutations_recur(lst[:], 0, max_depth, result_list, depth)
        if depth < max_depth:
            # if max depth already reached with "permutations_recur(lst[:], 0, max_depth, result_list, depth)"
            # don't call this line bc it would append the same list to result_list.
            # not nice, need to find proper break condition.
            permutations_recur(lst[:], 1, max_depth, result_list, depth)
    else:
        result_list.append(lst)
        return


def gen_permutations(n):
    permutations = []
    max_depth = n
    permutations_recur([], 0, max_depth, permutations)
    permutations_recur([], 1, max_depth, permutations)
    return permutations


print(gen_permutations(3))
# output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
