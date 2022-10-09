#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = input('input text:')

words = [word for word in text.split() if '"абв"' not in word]

print(text, '->', ' '.join(words))
