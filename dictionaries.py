# # Exercise 1 - Fixed keys
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print (phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '938-489-1234'
print phonebook_dict

del(phonebook_dict['Alice'])
print phonebook_dict

phonebook_dict['Bob'] = '968-345-2345'
print phonebook_dict


# Exercise 2 - Nested Dictionaries - Fixed Keys
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}


ramit_mail = (ramit['email'])
print ramit_mail
ramit_interests = (ramit['interests'] [0])
print ramit_interests
jas_email = (ramit ['friends'] [0] ['email'])
print jas_email
jan_interests = (ramit ['friends'] [1] ['interests'] [1])
print jan_interests


# Letter Summary
def letter_histogram(word):
	letter_dict = {}
	for letter in word:
		if (letter in letter_dict):
			letter_dict[letter] += 1
		else:
			letter_dict[letter] = 1
	return letter_dict

print (letter_histogram("hippopotamus"))

		# alternate way
# def letter_histogram(word):
# 	letter_dict = {}
# 	for i in word:
# 		if not letter_dict.has_key(i):
# 			letter_dict[i] = 1
# 		else:
# 			letter_dict[i] += 1

# Word Summary

def word_histogram(paragraph):
	word_dict = {}
	split_paragraph = paragraph.split()
	for word in split_paragraph:
		if (word in word_dict):
			word_dict[word] += 1
		else:
			word_dict[word] = len(word)
	return word_dict

print (word_histogram("There was an old lady who lived in a shoe"))


# Bonus Challenge
# use code from previous two (Letter and Word) questions.

word_dict = letter_histogram("Bananana")
steves_list = []	
for key in word_dict:	
	steves_list.append([key, word_dict[key]])
steves_list.sort (key = lambda x: x[1])
print steves_list[-1]
print steves_list[-2]
print steves_list[-3]



# Super Bonus
# list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]
# def make_final_dictionary(list):
# 	final_dictionary = {}
# 	intems_dictionary = {}
# 	for item in list:
# 		if (item in items_dictionary):
# 			items_dictionary[item] += 1
# 		else:
# 			items_dictionary = 1
# 	for organized_item in items_dictionary:
# 		if (items_dictionary[organized_item] == 1):




