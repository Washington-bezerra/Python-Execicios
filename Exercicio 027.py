#Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
nome = str(input('Digite seu nome completo: '))
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))