'''
1. The Ticket Machine (If-Else & Number System)


You are designing a self-service metro ticket machine. The machine asks the user torente
their age and determines the fare based on the following rules:


.


Children (age <10) ride for free.


.


Teenagers (10 < age < 18) get a 50% discount.


.


Seniors (age > 60) get a 30% discount.


.


Everyone else pays the full price of $10.


Task:
Write a program that takes the age as input and prints the final ticket price.

'''

age= int(input("Enter your age: "))


if age < 10:
    ticket_price=0
elif 10 <= age < 18: 
    ticket_price = 10 * 0.5 
elif age >= 60: 
    ticket_price = 10 * 0.7 
else:
    ticket_price =10 


print(f"Final ticket price: s
fticket_price)")

'''
2. The Festival Discount (Number System & If-Else)





During a festival, a store offers discounts based on the last digit of a customer's phone

number:

.If the last digit is even, they get a 10% discount•





.If the last digit is odd, ihey get a 15% discount



.If the last digit is 0, they get a 20% discount.


'''
def calculate_festival_discount(phone_number, total_purchase):
    """
    Calculates the festival discount based on the last digit of the phone number.

    Args:
        phone_number: The customer's phone number (string).
        total_purchase: The total purchase amount (float).

    Returns:
        The discounted price (float).
    """

    last_digit = int(phone_number[-1]) 

    if last_digit == 0:
        discount_percentage = 0.20  
    elif last_digit % 2 == 0:  
        discount_percentage = 0.10  
    else:
        discount_percentage = 0.15  

    discount_amount = total_purchase * discount_percentage
    discounted_price = total_purchase - discount_amount
    return discounted_price

# Example usage:
phone_number = input("Enter your phone number: ")
total_purchase = float(input("Enter the total purchase amount: "))

final_price = calculate_festival_discount(phone_number, total_purchase)

print(f"The final price after discount is: ${final_price:.2f}")


'''
3. The Bank Account Pin (Number System & Loops)


A bank has a PIN validation system where:


A user is given 3 attempts to enter a 4-digit PIN.


.If they enter the correct PIN, they get access.


• If they fail all 3 attempts, their account is locked.


Task:


Write a program that keeps asking for a PIN until the user enters the correct one or runs out


of attempts.

'''
def validate_pin(correct_pin):
    """
    Validates a user's PIN with 3 attempts.

    Args:
        correct_pin: The correct 4-digit PIN (string).
    """

    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")

        if entered_pin == correct_pin:
            print("Access granted!")
            return  
        attempts -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts}")

    print("Account locked. Too many incorrect attempts.")

# Example usage:
correct_pin = "1234"  
validate_pin(correct_pin)


'''
4.Print all prime numbers in a given range - min number and max number
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(min_num, max_num):
    """Prints all prime numbers within the given range."""
    print(f"Prime numbers between {min_num} and {max_num}:")
    for num in range(min_num, max_num + 1):
        if is_prime(num):
            print(num)

# Example usage:
min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

find_primes_in_range(min_number, max_number)

'''
5.Write a python code to print the sum of odd digits in a number. f input : 2355 output : 13)
'''
def sum_of_odd_digits(number):
  

  sum_odd = 0
  number_str = str(number)  

  for digit in number_str:
    digit_int = int(digit)  
    if digit_int % 2 != 0:  
      sum_odd += digit_int

  return sum_odd

# Example usage:
input_number = int(input("Enter a number: "))
result = sum_of_odd_digits(input_number)
print(f"Sum of odd digits: {result}")