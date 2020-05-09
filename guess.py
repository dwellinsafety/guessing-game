from random import randint

num=randint(1,10)

print("Welcome to the guessing game!")

guess = input("\nGuess an integer between 1 and 10.")
guess = int(guess)

def main():
	while True:
		if guess is not num:
			guess = input("Guess again: ")
			guess = int(guess)
		else:
			print("You guessed correctly!")
			break

if __name__ == '__main__':
	main()
	