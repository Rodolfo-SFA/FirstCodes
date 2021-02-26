nasc_ano = int(input('Escreva o ano do seu nascimento: '))
idade = 2020 - nasc_ano

if 17 <= idade <= 18:
    print('Você deve se alistar em uma junta militar.')
elif idade > 18:
    idp = idade - 18
    print('Você já passou {} anos do tempo de alistamento'.format(idp))
elif idade < 17:
    ida = 18 - idade
    print('Falta {} anos para você ter que se alistar.'.format(ida))
