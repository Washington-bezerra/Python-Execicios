#Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
ano = int(input('Digite o ano ou precione 0 para analisa o ano atual: '))

if ano ==0:
    ano = datetime.date.today().year
if ano % 4 ==0 and ano%100 !=0 or ano%400 ==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {}NÃO é bissexto'.format(ano))