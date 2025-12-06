#PALINDROME IN PYTHON

my_list = [
    'mummy',
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon',
    'no melon',
    'some men interpret nine memos',
    'madam',
]
def clearWhiteSpace():
    TEMP = []
    for chars in my_list:
        x = ''.join(chars.split(' '))
        TEMP.append(x)
    return TEMP

for chars in clearWhiteSpace(): #['mummy', 'hannah', 'murderforajarofredrum', 'mom', 'seagull', 'tomato', 'nolemon', 'nomelon', 'somemeninterpretninememos', 'madam']
    x = [] # ['y', 'm', 'm', 'u', 'm']
    for ch in chars:
        x.insert(0, ch)
    if chars == ''.join(x):
        print(f"{my_list[clearWhiteSpace().index(chars)]}: Is Palindrome")
    else:
        print(f"{my_list[clearWhiteSpace().index(chars)]}: Is Not Palindrome")