import argparse
import sys

def read_file(filename="", encoding="utf-8"):
	f = open(filename, "r", encoding=encoding)
	try:
		for line in f.readlines():
			yield line
	except UnicodeDecodeError:
		sys.exit("Please select the correct encoding.")
	f.close()


def get_data_by_key(filename, keyword, encoding=""):
	for data in read_file(filename, encoding):
		if keyword in data[:len(keyword)]:
			yield data

def main():
	parser = argparse.ArgumentParser(
		prog='get_data_by_key',
		description='This code get all lines with a keyword from file')
	parser.add_argument('-f', '--filename')
	parser.add_argument('-k', '--keyword')
	parser.add_argument('-e', '--encoding')
	parser.add_argument('-v', '--verbose',
	action='store_true')
	
	filename = None
	keyword = None

	args = parser.parse_args(None if sys.argv[1:] else ['--help'])

	if args.filename is not None:
		filename = args.filename 
	else:
		sys.exit("Please select a filename")
	if args.keyword is not None:
		keyword = args.keyword
	else:
		sys.exit("Please select a keyword")
	if args.encoding is not None:
		encoding = args.encoding
	else:
		encoding = "utf-8"
	if (filename is not None) and (keyword is not None):
		for x in get_data_by_key(filename, keyword, encoding):
			print(x, end="\n")

if __name__ == "__main__":
	main()
