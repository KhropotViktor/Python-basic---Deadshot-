print( '1.Define the id of next variables:')
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a)), print(id(str_b)), print(id(set_c)), print(id(lst_d)), print(id(dict_e))

print('2. Append 4 and 5 to the lst_d and define the id one more time.')
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

print('3. Define the type of each object from step 1.')
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

print('4*. Check the type of the objects by using isinstance.')
print(isinstance(int_a, int))
print(isinstance(str_b, int))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))


print('    String formatting:')
print('    Replace the placeholders with a value:')
print('    Anna has ___ apples and ___ peaches.')

print('5. With .format and curly braces {}')
print("Anna has {} apples and {} peaches" .format(25, 35))

print('6. By passing index numbers into the curly braces.')
print(' Anna has {1} apples and {0} peaches' .format(30, 40))

print('7. By using keyword arguments into the curly braces.')
print(' Anna has {apples} apples and {peaches} peaches' .format(apples=45, peaches=77))

print('8*. With indicators of field size (5 chars for the first and 3 for the second)')
print(' Anna has {0:5} apples and {0:4} peaches' .format(30, 40))

print('9. With f-strings and variables')
apples = 26
peaches = 47
print(f'Anna has {apples} apples and {peaches} peaches')

print('10. With % operator')
print('Anna has %s apples and %s peaches,' % (11, 17))

print('11*. With variable substitutions by name (hint: by using dict)')

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]



