# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ').split()
for i in text:
    if 'абв' in i:
        text.remove(i)
print(' '.join(text))