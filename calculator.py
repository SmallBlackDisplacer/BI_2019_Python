
# Class_checker asks for a number to enter, then returns int for int, float for float, and, if string inputed, gives you an enother chance.
def class_checker ():
    numb = input('Enter a number: ')
    try:
        if '.' in numb:
            return float(numb)
        else:
            return int(numb)
    except ValueError:
        print ("Not a number! Please try again")
        return class_checker()

# Operator_checker asks for operator to enter. If you make a mistake, you should try again.
def operator_checker ():
    op = input('Enter operator (+, -, * or /): ')
    opers = {'+', '-', '*', '/'}
    if op not in opers:
        print ("Incorrect operator! Please try again")
        return operator_checker ()
    else:
        return op

first_num = class_checker()
operator = operator_checker ()
second_num = class_checker()

if operator == '+':
    print (first_num + second_num)
elif operator == '-':
    print (first_num - second_num)
elif operator == '*':
    print (first_num * second_num)
elif operator == '/':
    print (first_num / second_num)