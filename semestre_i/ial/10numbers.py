#!/usr/bin/env python
# -*- coding: utf-8 -*-

quantidade_de_numeros = input('Quantos números você quer somar? ')
acumulador = 0
for i in range(quantidade_de_numeros):
    numero = input('Digite o ' + str(i+1) + '° número: ')
    acumulador += numero
print('A soma dos números que você digitou é ' + str(acumulador))
