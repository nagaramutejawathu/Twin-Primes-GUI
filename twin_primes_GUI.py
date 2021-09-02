import math
import turtle

rows = 31  #set values
columns = 59
start = 4275
countPrimes = 0
large_int = rows * columns +start -1


# This function returns True if the number is prime else False
def isPrime(num): #check if prime numbers
	if num<=1: #prime number cannot be less than 1,in this question,prime number cannot be negative
		return False
	for i in range (2,int(math.sqrt(num))+1): # sqrt(prime) /prime cannot be 0
		if (num %i)==0:
			return False
	else:  #except for above those 2 conditions,other is prime
		return True


def get_twin_primes(start, large_int): #check if twin prime numbers from the prime
	twin_primes = []
	for i in range(start,large_int): #set the range of start and the end number.
		j = i + 2 #because we are looking for the prime number that differ 2.
		if(isPrime(i) and isPrime(j)):#if they the number fit those two conditions
			# Adding current i and j values to the list
			twin_primes.append(i)
			twin_primes.append(j)
	# Return twin_primes list
	return twin_primes

# Function call to get twin primes
twin_primes = get_twin_primes(start, large_int)

# Turtle object
t = turtle.Turtle()
t.speed(20)
# Setting initial coordinates for turtle
x_pos = -655
y_pos = 250

# Loop to draw boxes inclusinga numbers inside
for i in range(start, large_int+1, columns):
	t.penup()
	t.setpos(x_pos, y_pos)
	t.pendown()
	for j in range(i, i+columns):
		t.forward(22)
		t.left(90)
		t.forward(15)
		t.left(90)
		t.forward(22)
		t.left(90)
		t.forward(15)
		t.left(90)
		# If current j value is in twin_primes list then
		# printing j value in red color
		if j in twin_primes:
			t.pencolor('red')
			t.write("  "+str(j), align="left", font=("Arial", 6))
			t.pencolor('black')
		# If current j value is a prime number then printing
		# j value in blue color
		elif isPrime(j):
			t.pencolor('blue')
			t.write("  "+str(j), align="left", font=("Arial", 6))
			t.pencolor('black')
		# If current j value is not a prime number then printing
		# j value in normal black color
		else:
			t.write("  "+str(j), align="left", font=("Arial", 6))
		t.forward(22)
	# Changing y cordinate
	y_pos -= 15

# Input to exit the program
input("Press 'Enter' key to exit")

