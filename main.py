from dictionary import dictionary
from logo import logo
print(logo)
text=input("Text to be transalted:")
letters=list(text)
code=''
for letter in letters:
    if letter != ' ':
        code += f'{dictionary[letter]} '
    else:
        code += '/'
print(code)