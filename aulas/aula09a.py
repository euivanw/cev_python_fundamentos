# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento
# de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(),
# strip(), junção com join().

frase = 'Curso em Vídeo Python'
print('frase: {}'.format(frase))
print('frase[3]: {}'.format(frase[3]))
print('frase[3:13]: {}'.format(frase[3:13]))
print('frase[:13]: {}'.format(frase[:13]))
print('frase[13:]: {}'.format(frase[13:]))
print('frase[1:15:2]: {}'.format(frase[1:15:2]))
print('frase[::2]: {}'.format(frase[::2]))
print('frase.count(\'o\'): {}'.format(frase.count('o')))
print('frase.count(\'O\'): {}'.format(frase.count('O')))
print('frase.upper().count(\'O\'): {}'.format(frase.upper().count('O')))
print('len(frase): {}'.format(len(frase)))
print('len(frase.strip()): {}'.format(len(frase.strip())))
print('frase.replace(\'Python\', \'Android\'): {}'.format(frase.replace('Python', 'Android')))
print('frase: {}'.format(frase))
print('\'Curso\' in frase: {}'.format('Curso' in frase))
print('frase.find(\'Curso\'): {}'.format(frase.find('Curso')))
print('frase.find(\'Vídeo\'): {}'.format(frase.find('Vídeo')))
print('frase.find(\'video\'): {}'.format(frase.find('video')))
print('frase.lower().find(\'vídeo\'): {}'.format(frase.lower().find('vídeo')))
print('frase.split(): {}'.format(frase.split()))

dividido = frase.split()
print('dividido[0]: {}'.format(dividido[0]))
print('dividido[2][3]: {}'.format(dividido[2][3]))

print("""
Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(),
strip(), junção com join().
""")
