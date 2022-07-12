from random import choice
word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]

def get_word():
    return choice(word_list).upper()
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

word = get_word()
def play(word):
    word_completion = ['_' for i in range(len(word))]  # строка, содержащая символы _ на каждую букву задуманного слова                       
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print('Количество букв в слове:')
    print(*word_completion, sep=' ')
    print('Введите одну букву русского алфавита или попытайтесь угадать всё слово.')
    print(f'У Вас осталось {tries} попыток.')
    while True:
        let_word = input('Введите букву или слово: ').upper()
        if not let_word.isalpha():
            print('Вы ошиблись. Попробуйте ещё раз!')
            continue
        if let_word in guessed_letters or let_word in guessed_words:
            print('Уже было. Попробуйте ещё раз!')
            continue
        if len(let_word) > 1:
            if let_word == word:
                print('Вы угадали слово. Победа!')
                break
            else:
                guessed_words.append(let_word)
                tries -= 1
                if tries > 0:
                    print(f'Не угадали. У Вас осталось {tries} попыток.')                
                    print(display_hangman(tries))
                else:
                    print(f'Вы не смогли угадать. Загаданное слово: {word}')
                    print(display_hangman(tries))
                    break
        else:
            guessed_letters.append(let_word)
            if let_word in word:                               
                for t in range(len(word)):
                    if word[t] == let_word:                       
                        word_completion[t] = let_word
                print(*word_completion, sep=' ')                        
                if ''.join(word_completion) == word:
                    print('Вы угадали слово. Победа!')
                    break
                continue
            else:
                tries -= 1
                if tries > 0:
                    print(f'Не угадали. У Вас осталось {tries} попыток.')                
                    print(display_hangman(tries))
                else:
                    print(f'Вы не смогли угадать. Загаданное слово: {word}')
                    print(display_hangman(tries))
                    break
            
play(word)
            
            
        
        
        
                
            
            














