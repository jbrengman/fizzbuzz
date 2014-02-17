def fizz_buzz(n):
	s = ''
	if (n % 3 == 0):
		s += 'Fizz'
	if (n % 5 == 0):
		s += 'Buzz'
	if (n % 3 != 0 and n % 5 != 0):
		s = str(n)
	return s

def fizz_buzz_ext(n, dict):
	s = ''
	for key in dict:
		if (n % key == 0):
			s += dict[key]
	if (n % 3 == 0 or n % 5 == 0):
		s = fizz_buzz(n) + s
	if ( s == ''):
		s = str(n)
	return s

if __name__ == '__main__':
	dictionary = {7: "Sivv", 8: "Fuzz", 9: "Bizz", 10: "Zubz", 11: "Fibz"}

	print('\nSimple FizzBuzz: \n')
	for x in range(25):
		print(str(x) + ':\t' + fizz_buzz(x))
	print('\nExtended FizzBuzz: \n(replacements: ' + str(dictionary) + ')\n')
	for x in range(25):
		print(str(x) + ':\t' + fizz_buzz_ext(x, dictionary))