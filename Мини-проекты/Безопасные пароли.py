from random import sample
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
char = ''

def generate_password(length, chars):
    return ''.join(sample(chars, length))
    
n = int(input(('Укажите количество паролей для генерации: ')))
d = int(input(('Укажите длину одного пароля: ')))
print('Ответьте на следующие вопросы да или нет')
dig = input('Включать ли цифры 0123456789? ')
if dig == 'да':
   char += digits
   
ABC = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
if ABC == 'да':
   char += uppercase_letters
   
abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
if abc == 'да':
   char += lowercase_letters

ch = input('Включать ли символы !#$%&*+-=?@^_? ')
if ch == 'да':
   char += punctuation
   
chl = input('Исключать ли неоднозначные символы il1Lo0O? ')
if chl == 'да':
    char = list(char)
    for c in 'il1Lo0O':
        if c in char:
            char.remove(c)
    char = ''.join(char)
    
for i in range(n):
    print(generate_password(d, char))