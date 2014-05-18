
def main():
	output_file = open("output.txt","w")
	input_file = open("1.txt")
	words = input_file.readlines()
	words = set([word.lower() for word in words])
	for word in words:
		output_file.write(str(word))
	output_file.close()

if __name__ == '__main__':
	main()