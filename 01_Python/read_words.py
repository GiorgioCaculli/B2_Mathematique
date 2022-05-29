# nous ouvrons le fichier
file_words = open('words', 'r')
# nous lisons toutes les lignes qui s'y trouvent
words = file_words.readlines()
# on affiche le tout
print(words)
# nous fermons le fichier
file_words.close()

# petit souci : le caractère \n se trouve dans notre tableau
# nous allons donc l'effacer

words_without_return = [word[:-1] for word in words]
print(words_without_return)
