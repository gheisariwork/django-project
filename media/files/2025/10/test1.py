# # print("hello")
# # print("264")
# # print("salam", 9.4, 'bachehaye 264')
# # single line
# '''
# multi
# line
# '''
#
# """
# hello
# world
# """
#
# print('i\'m ' ,end="*")
# print('_backend developer')
# print('ali','mohamad', 'reza',sep=",")
#
a = "i \'m backend developer"
print('first character to upper case:', a.capitalize())
print('title :', a.title())
str_upper = a.upper()
print('upper:', str_upper)
print('lower str_upper:', str_upper.lower())
print('is upper:', a.isupper())
print('is upper  variable a:', a.isupper())
print('is upper  variable str_upper:', str_upper.isupper())
print('is lower  variable a:', a.islower())
print('is lower  variable str_upper:', str_upper.islower())
print('count developer:', a.count('e'))
print('len developer:', len(a))
print('strip :', a.strip())
a = "i \'m backend developer"
print('index char b :', a[5])
print('index char backend :', a[5:12])
# a:b:c->start : end: step -> 1:12:3
print('index start:1->end:12->setp:2 :', a[1:12:2])
print('step 2:', a[::2])
print('reverse', a[::-1])
txt = "welcome to class {0} {1} {2}"
print("method format: ", txt.format(264, 'bamdad', 'sobhan'))
name = 'ali'
class_name = 264
m = 'ict'
age = 23
print(f"welcome to class {class_name} {m} {name} {age}")
