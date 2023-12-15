#1. print "softwarica" 10 times.
for i in range(10):
    print("softwarica")

#2. Sum of a list
my_list = [1, 2, 3, 4, 5]
my_sum = sum(my_list)
print(my_sum)

#3. print each character using indexing
string = "HELLO"
for i in range(len(string)):
    print(string[i])

#4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
my_list = [1, "a", "c", 2, 3, 4]

for element in my_list:
    if type(element) == int:
        print(element)

#5. multiplication of a each element. given list=[4,5,3,2]
lst = [4, 5, 3, 2]
n = 2
result = [x * n for x in lst]
print(result)

#6. multiplication table of a given number
num = 5
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

#7. reverse a list
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)

#8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]
lst = [1, 2, 3, 4]
result = [x + 1 for x in lst]
print(result)

#9. Given list is lst=[1,2,3,4] but print 1 and 4 only 
lst = [1, 2, 3, 4]
print(lst[0], lst[3])

#10. Given list is lst=[1,2,3,4] but print 1 2 and 4 only 
lst = [1, 2, 3, 4]
for i in range(3):
    print(lst[i])

#11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst = [1, 2, 3, 4]
lst[1] = "a"
for i in range(len(lst)):
    if lst[i] == 2:
        lst[i] = "a"
print(lst)

#12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
lst = [1, 2, 3, 4, 5]
odd = []
even = []
for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(odd)
print(even)

#13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
lst = [1, 2, 3, "d", 4, 5, "a"]
integers = []
strings = []
for x in lst:
    if type(x) == int:
        integers.append(x)
    elif type(x) == str:
        strings.append(x)
print(integers)
print(strings)

#14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
lst = [1, 2, 3, 4, "a", "b"]
types = []
for x in lst:
    types.append(type(x))
print(types)

#15. Python program that accepts a string and calculate the number of digits and letters and space
s = "This is a string with 123 numbers and spaces"
digits = 0
letters = 0
spaces = 0
for c in s:
    if c.isdigit():
        digits += 1
    elif c.isalpha():
        letters += 1
    elif c.isspace():
        spaces += 1
print(digits)
print(letters)
print(spaces)

#16. Python program to check the validity of username and password input by users
username = "admin"
password = "1234"

user_input = input("Enter username: ")
pass_input = input("Enter password: ")

if user_input == username and pass_input == password:
    print("Login successful")
else:
    print("Invalid username or password")

#17. program to print the given number is odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#18. factorial of a given number
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("The factorial of", n, "is", factorial)
     
#19. Print multiplication table of 1,2,3,4,5,6,7,8
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for num in numbers:
    print("-" * 20)
    for i in range(1, 11):
        print(f"{num:2} x {i:2} = {num * i:3}")

#20. Given list is lst=[1,2,3,4] but print 1 and 2 only
lst = [1, 2, 3, 4]
for num in numbers:
    print(num)

#21. Python program to calculate the sum of all the odd numbers within the given range.
def sum_odd(a, b):
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 1:
            total += i
    return total

#22. Python program to calculate the sum of all the even numbers within the given range.
def sum_even_numbers(start, end):
  sum = 0
  for i in range(start, end + 1):
    if i % 2 == 0:
      sum += i
  return sum

print(sum_even_numbers(1, 10))
print(sum_even_numbers(5, 15))
print(sum_even_numbers(0, 100))

#23. Python program to count the space of a given string
# Define a function to count the space of a given string
def count_space(string):
  count = 0
  for char in string:
    if char == " ":
      count += 1
  return count

print(count_space("Hello world"))
print(count_space("This is a test"))
print(count_space("NoSpaceHere"))

#24. given list is [1,2,3,4] but expected output is [1,8,27,64]
def cube_list(numbers):
  cubes = []
  for num in numbers:
    cube = num ** 3
    cubes.append(cube)
  return cubes

given_list = [1, 2, 3, 4]
expected_output = [1, 8, 27, 64]
print(cube_list(given_list) == expected_output)

#25. reverse of a string a="programming". 
def reverse_string(string):
  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
  return reversed_string

a = "programming"
print(reverse_string(a))

#26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
for i in range(50):
  print(i)
  if i == 7:
    break

#27. Write a for loop that iterates through a string and prints every letter.
string = "Hello world"

for letter in string:
  print(letter)

#28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
a = ["ram", "shyam", 1, 2]

for name in a:
  print("Hello!" + str(name))

#29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a = ["ram", "shyam", 1, 2]

lst = []

for item in a:
  lst.append("Dr." + str(item))

print(lst)

#30. Write a for loop which appends the square of each number to the new list.
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
  square = num ** 2
  squares.append(square)

print(squares)

#31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]

new_list = []

for num in lst1:
  if num > 0:
    new_list.append(num)

print(new_list)

#32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
list = [0, 1, 2, 3, 4, 5, 6]

for num in list:
  if num == 3 or num == 6:
    continue
  print(num)

#33. Write a for loop which appends the type of each element in the first list to the second list.
first_list = [1, "hello", 3.14, True, None]

second_list = []

for element in first_list:
  element_type = type(element)
  second_list.append(element_type)

print(second_list)

#34. Use else block to display a message “Done” after successful execution of for loop.
numbers = [1, 2, 3, 4, 5]

for num in numbers:
  print(num)
else:
  print("Done")

#35. Write a for loop statement to print the following series: 105 98 -------7
value = 105
while value >= 7:
  print(value)
  value -= 7

#36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
result = ""
for char in string:
  if char not in bad_chars:
    result += char
print(result)

#37. Python program to count the number of even and odd numbers from a series of numbers.  
def count_even_odd(numbers):
  even_count = 0
  odd_count = 0
  for num in numbers:
    if num % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  return even_count, odd_count

print(count_even_odd([1, 2, 3, 4, 5]))
print(count_even_odd([10, 15, 20, 25, 30]))
print(count_even_odd([0, -1, -2, -3, -4]))

#38. Write a python program to display all the prime numbers within a given range.
def is_prime(number):
  if number < 2:
    return False
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False
  return True

def display_prime_numbers(start, end):
  for num in range(start, end + 1):
    if is_prime(num):
      print(num)

display_prime_numbers(10, 20)
display_prime_numbers(50, 100)

#39. given number is prime or not
def is_prime(number):
  if number < 2:
    return False
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False
  return True

print(is_prime(2))
print(is_prime(17))
print(is_prime(15))
print(is_prime(1))

#40. program to check given number is palindrome or not
def is_palindrome(number):
  number_str = str(number)
  reversed_str = number_str[::-1]
  if number_str == reversed_str:
    return True
  return False

print(is_palindrome(121))
print(is_palindrome(123))
print(is_palindrome(0))
print(is_palindrome(11))

#41. program to check given number is armstrong or not
def is_armstrong(number):
  number_str = str(number)
  length = len(number_str)
  sum = 0
  for digit in number_str:
    digit = int(digit)
    power = digit ** length
    sum += power
  if sum == number:
    return True
  return False

print(is_armstrong(153))
print(is_armstrong(370))
print(is_armstrong(123))
print(is_armstrong(0))

#42. Python program to check a number is perfect square
def is_perfect_square(number):
  if number < 0:
    return False
  root = number ** 0.5
  if int(root) == root:
    return True
  return False

print(is_perfect_square(16))
print(is_perfect_square(25))
print(is_perfect_square(18))
print(is_perfect_square(-4))

#43. python program to check a number is perfect number
def is_perfect_number(number):
  sum = 0
  for i in range(1, number // 2 + 1):
    if number % i == 0:
      sum += i
  if sum == number:
    return True
  return False

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(15))
print(is_perfect_number(0))