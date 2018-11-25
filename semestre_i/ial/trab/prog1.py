#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
import os

file = open('arq_func.dat', 'wb')
os.system('clear') # limpa a tela

while True:
    hasError = False

    print(' == Novo funcionário ==\n')

    while True:
        id = input('Código: ')
        id = int(id) if id.isdigit() else 0

        if id > 0:
            break

        wantToCorrect = ''
        print('Campo inváido')
        while wantToCorrect != 's' and wantToCorrect != 'n':
            wantToCorrect = input('Deseja corrigir? (s/n) ')

        if wantToCorrect == 'n':
            haseError = True
            break

    if id == 9999:
        break

    if not hasError:
        while True:
            name = input('Nome: ')

            if name[0].isupper() and len(name) <= 30:
                break

            wantToCorrect = ''
            print('Campo inváido')
            while wantToCorrect != 's' and wantToCorrect != 'n':
                wantToCorrect = input('Deseja corrigir? (s/n) ')

            if wantToCorrect == 'n':
                hasError = True
                break

    if not hasError:
        while True:
            salary = input('Salário: ')
            try:
                salary = float(salary)
            except ValueError:
                salary = 0

            if salary > 0:
                break

            wantToCorrect = ''
            print('Campo inváido')
            while wantToCorrect != 's' and wantToCorrect != 'n':
                wantToCorrect = input('Deseja corrigir? (s/n) ')

            if wantToCorrect == 'n':
                hasError = True
                break

    if not hasError:
        while True:
            admission = input('Data de admissão: ')
            print(admission, len(admission))

            if len(admission) == 8:
                admission = int(admission)
                break

            wantToCorrect = ''
            print('Campo inváido')
            while wantToCorrect != 's' and wantToCorrect != 'n':
                wantToCorrect = input('Deseja corrigir? (s/n) ')

            if wantToCorrect == 'n':
                hasError = True
                break

    os.system('clear')
    if not hasError:
        reg = struct.pack(
            'i30sfi',
            id,
            name.encode('ascii'),
            salary,
            admission
        )
        file.write(reg)
        print('Funcionário escrito!')

file.close()
os.system('clear')
print('Saindo do programa...')
