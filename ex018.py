from math import cos, tan, sin, radians
ang = float(input('Escolha um angulo: '))
cs = cos(radians(ang))
tg = tan(radians(ang))
sn = sin(radians(ang))

print('Cosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(cs, sn, tg))
