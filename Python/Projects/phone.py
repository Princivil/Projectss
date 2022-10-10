
import re

def extract_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

def extract_all_phones(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)
	

print(extract_phone('my number is 845 098-5555'))
print(extract_phone('my number is 845 098-55555 or 094 869-3456'))
print(extract_phone('845 098-5555'))



def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False
	

is_valid_phone('567 065-6758')
is_valid_phone('my num: 467 065-6758')
is_valid_phone('467 065-6758 g')
