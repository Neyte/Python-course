#S = input("Введите что-нибудь:")
#our_file = open('Privet.jpg', 'w')
#print(S, file=our_file)
#our_file.close()

#with open('Privet.jpg', 'r') as our_file:
#    fs = our_file.read()
#with open('Privet.jpg', 'w') as our_file:
#    our_file.write(input(fs))

word = input('Введите слово: ').lower()
our_file = open('literature.txt', 'r', encoding='utf-8')
counter = 0
words = []
for file_line in our_file:
    file_line = file_line.lower().strip()
    word_list = file_line.split()
    for one_word in word_list:
        if one_word[:len(word)] == word:
            counter += 1
            if one_word not in words:
                words.append(one_word)
our_file.close()
print('Число слов: {}'.format(counter))
#for w in (words):
#    print(w)
