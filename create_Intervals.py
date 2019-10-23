# 1. With transformation to list
def create_intervals_list(data):
    data_list = sorted(list(data))
    result = []
    if len(data_list) == 0:
        return []
    start = data_list[0]
    for i in range(len(data_list)):
        if i < len(data_list) - 1 and data_list[i + 1] != data_list[i] + 1:
            result.append((start, data_list[i]))
            start = data_list[i + 1]
    result.append((start, data_list[-1]))
    return result


# 1. Without transformation to list
def create_intervals(data):
    if len(data) == 0:
        return []
    result = []
    start, end = min(data), min(data)
    while end <= max(data):
        if end + 1 not in data and end in data:
            result.append((start, end))
        elif end + 1 in data and end not in data:
            start = end + 1
        end += 1
    return result


print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)])
print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)])
