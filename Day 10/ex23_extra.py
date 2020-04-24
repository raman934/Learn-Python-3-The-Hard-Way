def main(language_file):

	line = language_file.readline().encode('raw_unicode_escape')

	if line:
		print_line(line)
		return main(language_file)


def print_line(line):
	next_lang = line.strip()

	raw_string = next_lang.decode()
	cooked_bytes = raw_string.encode('utf-8')

	print(raw_string, "<===>", cooked_bytes)


languages = open("sample.txt", 'r', encoding = 'unicode_escape')

main(languages)
