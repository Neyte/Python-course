S = input("Vvedite stroku: ").lower()
vowel_counter = 0
letters_counter = 0
for i in range(len(S)):
    if S[i] in set(('e','y','u','i','o','a')):
        vowel_counter += 1
for i in range(len(S)):
    if S[i] not in set((' ','.',',','!','?')):
        letters_counter += 1
print("All :{0}, Vovels:{1}, Consonants:{2}".format(letters_counter, vowel_counter, letters_counter - vowel_counter))
