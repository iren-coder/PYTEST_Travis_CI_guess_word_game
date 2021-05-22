#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random

def word_choice():
    words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    choice = random.choice(words)

    return choice

def check_letter(letter, word):
    if letter in word:
        return True
    else:
        return False


def update_underscore(letter, word, underscore):
    guess_word = underscore.split()
    for i in range(len(word)):
        if letter == word[i]:
            guess_word[i] = letter

    return " ".join(guess_word)


def main():
    print('\nДавай поиграем в игру? Ха-ха! Я загадываю слово - а ты должен его угадать!')
    print('Если ты ошибаешься, то получаешь штрафное очко. Всего можно ошибиться 4 раза.\n')
    ready = input('Готов начать? (y,n): ')

    if ready == 'y':
        fails = 0
        max_fails = 4
        word = word_choice()
        underscore = ' _' * len(word)

        while fails < max_fails and underscore.replace(" ", "") != word:
            print('В этом слове ' + str(len(word)) + ' букв: ' + underscore)
            letter = input('Введите букву: ')
            if letter in underscore and letter != '_':
                print('Такая буква уже была.\n')
            elif check_letter(letter, word):
                underscore = update_underscore(letter, word, underscore)
                print('Ты угадал!\n')
            else:
                print('\nТы ошибся!\n')
                fails += 1
                print('Количество ошибок -', fails)

        if underscore.replace(" ", "") == word:
            print('-------------------------------')
            print('Ты выиграл!')
        else:
            print('-------------------------------')
            print('Ты проиграл!')

        print('Загаданное слово было -', word)
        print('Количество ошибок -', fails)
        print('-------------------------------')

    elif ready == 'n':
        print('Всего хорошего! Пока!')
    else:
        print('Нажми Y или y - если хочешь начать игру и N или n - если хочешь завершить игру.')


if __name__ == '__main__':
    main()
