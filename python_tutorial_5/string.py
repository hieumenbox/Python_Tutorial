''' 
Topic #2: Chuỗi kí tự (string), a sequence of characters

'''
#String: ordered, immutable, text presentation

# use single or double quotes
# my_string = 'Hello World'
# my_string = "My name 's Hieu"
# print(my_string, type(my_string))

# Escaping Backslash \
# my_string = 'I\'m a "cuu hoc sinh THPT Tan An"'
# my_string = "I'm living in \"Viet Nam\""
# print(my_string)

# backslash if you want to continue in the next line

# my_string = "Voi mong muon tao nen mot platform \
# chia se nhung kien thuc ve Lap Trinh    "
# print(my_string)

''' 
Access characters and substrings
'''
my_string = "Hello World"
# get character by referring to index
# char = my_string[-2]
# print(char)

# String is immutable -> Cannot be changed
#my_string[0] = "M"

#Substring with slicing
# stringName[startIndex:endIndex]
# start at index 1 and go until index 5 ( not include #5)
# sub_string = my_string[1:5]
# sub_string = my_string[:5]
# sub_string = my_string[6:]

# sub_string = my_string[::-1] # Reverse the String
# sub_string = my_string[::2]  # Take every second character
# print(sub_string)

'''
Concatenate teo or more strings
'''

# concat string with +
# greeting = "Hello, Xin Chao Cac Ban, "
# channel = "Codexplore"
# sentence = greeting + "Chao Mung Cac Ban Den Voi Channel cua " + channel
# #print(sentence)

# # joint elements of a list into a stirng .join()
# my_list = ['How', 'are', 'you', 'doing']
# sentence = ' '.join(my_list)
# print(sentence)

'''
Iterating
'''
# Iterating over a string by using a for in loop
my_string = "Hello Xin Chao Cac Ban"

# for char in my_string:
#     print(char)

# if "X" in my_string:
#     print("Yes")
# else:
#     print("No")

'''
Basic & Useful Function (Hàm cơ bản và Hũu ích)
'''

#strip()
# 'I am alone' --> Strips all whitespace characters from both ends.
print('    I am alone   '.strip() )
print("On an island".strip('O'))

#split()
print('but life is good'.split())
print('but, very boring'.split(','))

# replace()
# print('Help me'.replace("me","you"))

# my_string = 'Need to make a fire'
# print(my_string.startswith('Need'))
# print(my_string.endswith('Need'))

my_string = 'bye bye bae'
print(my_string.index('e'))