# Your optional code here
# You can import some modules or create additional functions


def checkio(data: list) -> list:
    dict_with_elem = {}
    data_non_uniq = []
    for elem in data:
        if elem in dict_with_elem:
            dict_with_elem[elem] = True
        else:
            dict_with_elem[elem] = False
    for elem in data:
        if dict_with_elem[elem]:
            data_non_uniq.append(elem)
    return data_non_uniq


data = [1, 2, 3, 1, 3]
checkio(data)

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list
