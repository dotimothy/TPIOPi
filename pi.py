def main():
	digits = input("How Many Digits of Pi Would Like To See: ")
	print("Here is " + digits + " digit(s) of Pi: ")
	digits = int(digits)
	if(digits > 1000000):
		print("Sorry, we only support 1000000 digits right now.")
		exit()
	if(digits != 1):
		digits = digits + 1
	pi = open("pi.txt", "r")
	print(pi.read(int(digits))),
	
main()