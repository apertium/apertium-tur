#! /usr/bin/ python
# -*- coding: iso-8859-15 -*-
import urllib
from urllib.parse import urlparse
import urllib.request

def s(string):
	return string.encode("iso-8859-9")

def replaceLTGT(word):
	"""Replaces what's between LT('<') and  GT('>'). IE: somethin<g> returns something, som<pE>thing returns somEthing"""
	letters	= "abcdefghijklmnopqrstuvwxyz"
	for letter in letters:
		while 1:
			try:
				beginIndex	= word.index('<' + letter + '>')
				word			= word[:beginIndex] + letter + word[beginIndex + 3:]
			except ValueError:
				break
	for vowel in ['A','E','I','O','U']:
		while 1:
			try:
				beginIndex = word.index('<p' + vowel + '>')
				word = word[:beginIndex] + vowel + word[beginIndex + 4:]
			except ValueError:
				break
	while 1:
		try:
			beginIndex = word.index('<')
			word	= word[:beginIndex] + word[word.index('>') + 1:]
		except ValueError:
			break
	return word.lower()

def parse(text,separator):
	"""Parses text, returning all words within it; separator is a list of things which should not be contained in any word and it should separate them."""
	result = []
	while len(text):
		firstSeparator = len(text)
		for x in range(len(separator)):
			try:
				aux = text.index(separator[x])
				if aux < firstSeparator:
					firstSeparator = aux
			except ValueError:
				pass
		if firstSeparator == 0:
			text = text[1:]
			continue
		#here comes the rules part:
		
		word		= text[:firstSeparator]
		word		= replaceLTGT(word)
		
		#end of rules part
		if word in text:
			print("Word \"" + word + "\" is duplicate")
		result.append(word)
		text = text[firstSeparator + 1:]
	return result

def parseLine(line, commentChars):
	if len(line) == 0:
		return 0;
	for char in commentChars:
		if char in line:
			line = line[:line.index(char)]
	line	= replaceLTGT(line)
	return line

def contains(string, toFind, separator):
	"""checks if string contains toFind between separators or in the begining/end"""
	begin = 0
	l	= len(toFind)
	while toFind in (string[begin:]):
		indexFound	= string[begin:].index(toFind) + begin

		if indexFound == 0 and begin == 0:
			if string[l] in separator:
				return 1

		if indexFound == len(string) - l:
			if string[len(string) - l - 1] in separator:
				return 1

		if string[indexFound - 1] in separator and string[indexFound + l] in separator:
			return 1
		begin = indexFound + l
	return 0

def getDefinition(word,separator,part_of_speech_index):
	
	urlName = "http://tdkterim.gov.tr/bts/arama/"
	
	urlValues	= "kategori=verilst&" + "kelime=" + urllib.request.quote(word.encode("iso-8859-9")) + "&ayn=tam"
	
	fullUrl = urlName + '?' + urlValues
	req2 = urllib.request.Request(fullUrl)
	req2.add_header('Referer'	,"http://tdkterim.gov.tr/bts/arama/index.php")
	urlHTML	= urllib.request.urlopen(req2).read().decode("iso-8859-9")


	exist	= [	0, #'adjectives'	
				0, #'adverbs'
				0, #'conjunctions' 
				0, #'interjections'
				0, #'nouns'
				0, #'postpositions'
				0, #'pronouns'
				0, #'proper_nouns'
				0] #'verbs'
	meanings = urlHTML
	meanings	= urlHTML[urlHTML.index('</table'):]
	meanings	= meanings[:meanings.index('<script')]
	
	if unknown_word in meanings:
		#word not found
		out.write	("ERROR: " + word + " not found (sözü bulunamadi).\n")
		print	("ERROR: " + word + " not found (sözü bulunamadi).\n")
		return 0
	
	for x in range(len(pos)):
		#for each word type:
		for i in range(len(meanings)):
			#for each index in urlHTML
			#if startingIndexCompare(meanings,pos[x], i,separator):
			if contains(meanings,pos[x],separator):
				#if we find the specified string between separators:
				exist[x] = 1
				#check if the word is in that file
				if not (word in text[x]):
					out.write	(word + " isn't in (any of) the " + types[x] + " file(s), even though " + pos[x] + " was found.\n")
					print	(word + " isn't in (any of) the " + types[x] + " file(s), even though " + pos[x] + " was found.\n")
				break
	
	if exist[part_of_speech_index] == 0:
		out.write	("Warning: " + word + " might not be a(n) " + types[part_of_speech_index] + " because " + pos[part_of_speech_index] + " could not be found.\n")
		print	("Warning: " + word + " might not be a(n) " + types[part_of_speech_index] + " because " + pos[part_of_speech_index] + " could not be found.\n")

out = open("output.txt","w")
unknown_word	= open("unknown",'r').read().encode("iso-8859-9").decode("iso-8859-9")
unknown_word	= unknown_word[:len(unknown_word) - 1]

pos = []
pos.append('sf.'	)	#'adjectives'	
pos.append('zf.'	)	#'adverbs'
pos.append('bag.'	)	#'conjunctions' 
pos.append('??.'	)	#'interjections'
pos.append('a.'		)	#'nouns'
pos.append('??.'	)	#'postpositions'
pos.append('??.'	)	#'pronouns'
pos.append('??.'	)	#'proper_nouns'
pos.append('??.'	)	#'verbs'
#pos	= ['a.'] -> for nouns only :D

types = []
types.append('adjectives'	)	#'adjectives'
types.append('adverbs'		)	#'adverbs'
types.append('conjunctions'	)	#'conjunctions'
types.append('interjections'	)	#'interjections'
types.append('nouns'		)	#'nouns'
types.append('postpositions')	#'postpositions'
types.append('pronouns'		)	#'pronouns'
types.append('proper_nouns'	)	#'proper_nouns'
types.append('verbs'		)	#'verbs'

files = []
files.append(['adjectives'				])				#'adjectives'
files.append(['adverbs'					])				#'adverbs'
files.append(['cnjadv','cnjcoo','cnjsub'])				#'conjunctions'
files.append(['interjections'			])				#'interjections'
files.append(['nouns'					])				#'nouns'
files.append(['postpositions'])#,'postpositions_infl'])	#'postpositions'
files.append(['pronouns'				])				#'pronouns'
files.append(['proper_nouns'			])				#'proper_nouns'
files.append(['verbs','verbs_iv','verbs_tv'])			#'verbs'
#files = [ 'nouns'] -> for nouns only :D

print("Reading and checking for duplicates...",)
separator				= [' ','	','\n', ',',';','.','\’','=','#','>','<']
separator_without_gtlt	= [' ','	','\n', ',',';','.','\’','=','#']
comment				= ['=','#','%','\t']
#for i in range(len(separator)):
#	separator[i] = s(separator[i])
f	= []
text	= []
for i in range(len(types)):
	print("Category " + types[i] + ':')
	for j in range(len(files[i])):
		print("File " + files[i][j])
		f.append(open('lexicon/' + files[i][j],'r'))
		text.append([])
		while 1:
			string	= f[i].readline()
			string	= string[:len(string) - 1]
			someWord	= parseLine(string,comment)
			if someWord == 0:
				break
			if len(someWord) == 0:
				continue
			text[i].append(someWord)
print("Done")
i = 0;

#for i in range(len(wordList)):
	#wordList[i] = urllib.request.quote(wordList[i].encode("iso-8859-9"))

print()
print("Begining checking parts of speech...")

for i in range(len(types)):
	if '??' in pos[i]:
		print("his category has unknown abreviation, so it will be skipped. Change the main python file in order to avoid this. (Search for \"pos.append\")")
		continue
	for j in range(len(text[i])):
		print(text[i][j] + "	in category " + types[i])
		getDefinition(text[i][j],separator,i)



