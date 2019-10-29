def create_intervals(data):
    data_list = sorted(data)
    result = []
    if not data_list:
        return []
    start = data_list[0]
    for i in range(len(data_list) - 1):
        if data_list[i + 1] != data_list[i] + 1:
            result.append((start, data_list[i]))
            start = data_list[i + 1]
    result.append((start, data_list[-1]))
    return result


print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)])
print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)])
