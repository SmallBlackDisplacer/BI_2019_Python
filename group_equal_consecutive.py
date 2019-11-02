def group_equal(els):
    result_list = []
    for i in range(len(els)):
        if i == 0 or els[i] != els[i - 1]:
            current_list = []
        current_list.append(els[i])
        if i == len(els) - 1 or els[i + 1] != els[i]:
            result_list.append(current_list)
    return result_list


print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]])
print(group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]])
print(group_equal([1]) == [[1]])
print(group_equal([]) == [])
