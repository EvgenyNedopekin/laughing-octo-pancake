import random


def rock_paper_scissors():
    while True:
        variants = ('камень', 'ножницы', 'бумага')
        computer_option = random.choice(variants)
        human_option = input('Введите: камень, ножницы или бумага\n').lower()

        if human_option not in variants:
            print('Слово введено с ошибкой')

        elif human_option == computer_option:
            print(f'Компьютер выбрал: {computer_option}. Вы выбрали: {human_option}')
            print('Ничья. Сыграйте еще раз\n')

        elif human_option == 'камень' and computer_option == 'ножницы'\
                or human_option == 'ножницы' and computer_option == 'бумага'\
                or human_option == 'бумага' and computer_option == 'камень':
            print(f'Компьютер выбрал: {computer_option}. Вы выбрали: {human_option}')
            print('Вы выиграли\n')

        else:
            print(f'Компьютер выбрал: {computer_option}. Вы выбрали: {human_option}')
            print('Вы проиграли\n')

        enter = input('Введите 1 для выхода в меню или Enter для продолжения игры\n')
        if enter == '1':
            break


def guess_the_number():
    while True:
        count = 1
        print('Я загадал число от 1 до 100.')
        computer_number = random.randint(1, 100)
        while True:
            answer = int(input('Угадайте загаданное число: '))
            if answer > computer_number:
                print('Не верно. Оно меньше\n')
            elif answer < computer_number:
                print('Не верно. Оно больше\n')
            elif answer == computer_number:
                print(f'Поздравляю!!! Вы отгадали за {count} попыток\n')
                break
            count += 1
        enter = input('Введите 1 для выхода в меню или Enter для продолжения игры\n')
        if enter == '1':
            break


def mainMenu():
    while True:
        print('''Вас приветствует приложение игр!
1. Игра - 'Камень, ножницы, бумага'\n2. Игра - 'Угадай число\'''')
        print('Выберет пункт 1 или 2 для выбора игры')
        choice = input('Для выхода нажмите Enter:\n ')
        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            guess_the_number()
        else:
            break


mainMenu()