vowels = ('a','e','i','o','u')

def new_word(word):
	first_letter = word [0]
	if first_letter in vowels:
		return word + "ay"
	else:
		return word[1:] + word[0] +"ay"
		
print ('Enter a word to translate to Pig Latin:')

text = raw_input()

print ('Your new word is:' + new_word(text))