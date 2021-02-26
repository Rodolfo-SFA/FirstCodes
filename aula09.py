frase = 'Curso em Vídeo Python'
print('Resposta 1: {}'.format(frase, end='\n'))
print('Resposta 2: {}'.format(frase[3], end='\n'))
print('Resposta 3: {}'.format(frase[3:13], end='\n'))
print('Resposta 4: {}'.format(frase[:13], end='\n'))
print('Resposta 5: {}'.format(frase[6:], end='\n'))
print('Resposta 6: {}'.format(frase[1:15:2], end='\n'))
print('Resposta 7: {}'.format(frase[1::2], end='\n'))
print('Resposta 8: {}'.format(frase[::2], end='\n'))
print('Resposta 9: {}'.format(frase.count('o')))
print('Resposta 10: {}'.format(frase.count('O')))
print('Resposta 11: {}'.format(frase.upper().count('O')))
print('Resposta 12: {}'.format(len(frase)))
print('Resposta 13: {}'.format(frase.replace('Python', 'Android')))
print('Resposta 14: {}'.format('Curso' in frase))
print('Resposta 15: {}'.format(frase.find('Curso')))
print('Resposta 16: {}'.format(frase.find('Vídeo')))
print('Resposta 17: {}'.format(frase.find('vídeo')))
print('Resposta 18: {}'.format(frase.lower().find('vídeo')))
print('Resposta 19: {}'.format(frase.split()))
print('Resposta 19A: {}'.format(frase[::-1]))

dividido = frase.split()
print('Resposta 20: {}'.format(dividido[0]))  #O dividido recebe a lista criada de ['Curso', 'em', 'Vídeo', 'Python'], onde o primeiro da lista é "Curso" que corresponde ao 0.
print('Resposta 21: {}'.format(dividido[2][2:4]))  #Você escolhe o número da lista que é "Vídeo" e pega as letras
print('Resposta 22: {}'.format('-'.join(dividido)))


frase.replace('Python', 'Android')
print('Resposta 23: {}'.format(frase))

frase = frase.replace('Python', 'Android')
print('Resposta 24: {}'.format(frase))

frase2 = '   Curso em Vídeo Python  '
print('Resposta 25: {}'.format(len(frase2)))
print('Resposta 26: {}'.format(len(frase2.strip())))




print(end='\n')

print("""Neste livro fascinante, Taleb mostra que, ao contrário do que defende a maioria dos economistas, estamos constantemente à mercê do inesperado. 
A estes acontecimentos imprevisíveis o autor dá o nome de Cisne Negro 
(animal que se considerava inexistente até ser visto, pela primeira vez, inesperadamente, na Austrália, no século XVII).
Um Cisne Negro é um evento com três características altamente improváveis: 
é imprevisível, ocasiona resultados impactantes e, após sua ocorrência, 
inventamos um meio de torná-lo menos aleatório e mais explicável. 
O sucesso surpreendente do Google foi um cisne negro, assim como o 11 de Setembro.""")