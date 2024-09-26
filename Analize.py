import os
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

samples_dir = r'd:\Descargas\ServicioSocial\SamplesTxt'

ignore_words = {'contactar', 'contact'}

for filename in os.listdir(samples_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(samples_dir, filename), 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            filtered_words = ' '.join(word for word in first_line.split() if word.lower() not in ignore_words)
            names = f'{filtered_words}'
            print(names)