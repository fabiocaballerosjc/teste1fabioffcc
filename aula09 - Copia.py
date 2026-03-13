
import pygame
nome=input('Nome: ')
dividido=nome.split()
ult_nome=dividido[-1]
pri_nome=dividido[0]
print(nome)
print(pri_nome)
print(ult_nome)
print(nome.title())
print(nome.upper())
print(len(nome))
print(nome.count('a'))
print(nome.replace(' ',''))
print(len(nome.replace(' ','')))
print('#'*45)
print(nome.strip())
print('#'*45)
print('#'*45)
print('#'*45)



pygame.mixer.init()
# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar a musica...')