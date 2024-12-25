# Solution 1: Even or Odd Function
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Solution 2: Count Vowels in a String
def get_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Solution 3: Transform Number to String
def number_to_string(num):
    return str(num)