abbreviations = {}

def readIntoDict(abbreviations_list):
	abbreviations = {}
	for abbreviation in abbreviations_list:
		abbreviation = abbreviation.split(" ")
		abbreviations[abbreviation[0]] = (" ").join(abbreviation[1:]).strip()
	return abbreviations


def replace_abbreviations(input_text):
	sentences = input_text.split(".")
	# sub_sentences = input_text.split(',')
	# print sub_sentences
	replaced_text = ""

	for eachSentence in sentences:
		words = eachSentence.split(" ")
		for i in range(len(words)):
			if abbreviations.has_key(words[i]):
				words[i] = abbreviations[words[i]]
		replaced_text = replaced_text + (" ").join(words)
	
	return replaced_text



def main():
	global abbreviations
	abbreviations_file = open("Abbreviations.txt")
	abbreviations = readIntoDict(abbreviations_file.readlines())
	abbreviations_file.close()

	# print abbreviations
	input_text = "dis is one of d biggest n common problm hv seen,but tis is a prgm to correct it. Bt nt a big deal!"
	new_text = replace_abbreviations(input_text)
	print new_text
if __name__ == '__main__':
	main()