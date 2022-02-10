vowels = ['a', 'e', 'i', 'o', 'u']

# word = "Milliways"
word = input("Provide a word to search for vowels: ")
found = {}
print('input length is :', len(word))
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times.')
