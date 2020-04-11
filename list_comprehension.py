# 1. Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.

list_one = [x for x in range(1, 101) if '7' in str(x)]
print(list_one)

# 2. Взять предложение **Would it save you a lot of time if I just gave up and went mad now?**
# и сделать его же без гласных. **up:** можно оставить в виде списка слов и не собирать строку.

message_two = 'Would it save you a lot of time if I just gave up and went mad now?'
result_two = ''.join([x for x in message_two if x not in 'aeiou'])
print(result_two)

# 3. Для предложения **The ships hung in the sky in much the same way that bricks don't**
# составить словарь, где слову соответствует его длина.

message_three = "The ships hung in the sky in much the same way that bricks don't"
dict_three = {el: i for el, i in zip(message_three.split(' '), list(map(lambda x: len(x), message_three.split(' '))))}
print(dict_three)

# 4*. Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).


# 5*. Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.

list_five = [x for x in range(1, 1001) if sum(list(map(lambda y: x % y == 0, range(2, 10)))) == 0]
print(list_five)
