import random

POINTS = [100, 50, 25, 10, 0]
WORDS = ('птица', 'подарок', 'война', 'офицер', 'президент', 'лагерь',
         'собака', 'звонок', 'отношение', 'женщина', 'кошка')
word = random.choice(WORDS)
correct = word
jumble = ''
attempt = 1
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
    '''
                Добро пожаловать в игру "Анаграммы"!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Enter, не вводя своей версии.)
    '''
)
print(f'Вот анаграмма: {jumble}')
print('У вас пять попыток')
print(f'\n{attempt} попытка')
guess = input('Попробуйте отгадать исходное слово: ')
while guess != correct and guess != '':
    print('К сожалению вы не правы.')
    attempt += 1
    if attempt > 5:
        print('Игра окончена! =(')
        break
    hint = input('Вам нужна подсказка? Да/Нет: ').lower()
    if hint == 'да':
        print(f'Загаданное слово начинается с буквы: {correct[0].upper()}')
    print(f'\n{attempt} попытка')
    guess = input('Попробуйте отгадать исходное слово: ')

if guess == correct:
    print('Да, именно так! Вы отгадали!\n')
    print(f'Вы отгадали слово с {attempt} попыток и заработали {POINTS[attempt - 1]} очков')
    print('Спасибо за игру.')
    input('\n\nНажмите Enter, чтобы выйти')
