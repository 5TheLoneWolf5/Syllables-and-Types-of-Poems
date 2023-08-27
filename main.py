print("--- Escreva um Poema ---")

firstLine = input("Primeira linha: ")
secondLine = input("Segunda linha: ")
thirdLine = input("Terceira linha: ")
fourthLine = input("Quarta linha: ")

joinedPoem = [firstLine, secondLine, thirdLine, fourthLine]
vowels = ['a', 'e', 'i', 'o', 'u']
lastSyllable = [[], [], [], []]

# Find last syllable (last vowel in a syllable), if there is not vowel, then the entire word is the syllable. Not case-sensitive.

for idx, line in enumerate(joinedPoem):
  lastWord = line.split(" ")[-1].lower()
  lastVowelIndex = 0
  for vowel in vowels:
    if vowel in lastWord:
      currentVowel = lastWord.rindex(vowel)
      if lastVowelIndex == 0 or lastVowelIndex < currentVowel:
        lastVowelIndex = currentVowel
        # print(vowel, lastVowelIndex)

    # Values that are closest to the end of the word will be added.

    # Deleting last entry added, since a closer (to the end) syllable has been found.
    if len(lastSyllable[idx]) > 0:
      del lastSyllable[idx][0]
      
    lastSyllable[idx].append(lastWord[lastVowelIndex:])
    
  if len(lastSyllable[idx]) < 1:
    lastSyllable[idx].append(lastWord)

# print(lastSyllable)

lastSyllableFirst = lastSyllable[0]
lastSyllableSecond = lastSyllable[1]
lastSyllableThird = lastSyllable[2]
lastSyllableFourth = lastSyllable[3]

# Rima Perfeita.

if lastSyllableFirst == lastSyllableSecond and lastSyllableFirst == lastSyllableThird and lastSyllableFirst == lastSyllableFourth:
  print("Rima Perfeita.")
  
# Rima Par.

elif lastSyllableFirst == lastSyllableSecond and lastSyllableThird == lastSyllableFourth and lastSyllableFirst != lastSyllableThird:
  # Implicit that second must also be different to the third and fourth.
  print("Rima Par.")

# Rima Cruzada.

elif lastSyllableFirst == lastSyllableThird and lastSyllableSecond == lastSyllableFourth and lastSyllableFirst != lastSyllableSecond:
  # Implicit as well.
  print("Rima Cruzada.")

# Rima Concha.

elif lastSyllableFirst == lastSyllableFourth and lastSyllableSecond == lastSyllableThird and lastSyllableFirst != lastSyllableSecond:
  # Implicit as well.
  print("Rima Concha.")

# Rima Livre.

else:
  print("Rima Livre.")

################################
#Tests and beta versions below.#
################################

# lastLetterFirst = firstLine[-1].lower()
# lastLetterSecond = secondLine[-1].lower()
# lastLetterThird = thirdLine[-1].lower()
# lastLetterFourth = fourthLine[-1].lower()

# # Rima Perfeita.

# if lastLetterFirst == lastLetterSecond and lastLetterFirst == lastLetterThird and lastLetterFirst == lastLetterFourth:
#   print("Rima Perfeita.")
  
# # Rima Par.

# elif lastLetterFirst == lastLetterSecond and lastLetterThird == lastLetterFourth and lastLetterFirst != lastLetterThird:
#   # Implicit that second must also be different to the third and fourth.
#   print("Rima Par.")

# # Rima Cruzada.

# elif lastLetterFirst == lastLetterThird and lastLetterSecond == lastLetterFourth and lastLetterFirst != lastLetterSecond:
#   print("Rima Cruzada.")

# # Rima Concha.

# elif lastLetterFirst == lastLetterFourth and lastLetterSecond == lastLetterThird and lastLetterFirst != lastLetterSecond:
#   print("Rima Concha.")

# # Rima Livre.

# else:
#   print("Rima Livre.")