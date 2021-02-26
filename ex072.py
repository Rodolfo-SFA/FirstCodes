extenso1 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

inteiro = int(input('Digite um número entre 0 e 20: '))

while inteiro not in range(0, len(extenso1)):
    inteiro = int(input('Tente novamente! Digite um número entre 0 e 20: '))
print(f'O número que você digitou é {extenso1[inteiro]}.')