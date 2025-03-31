# 1. Fibonacci Sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

# 2. Prime Number Check
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 3. Palindrome Checker
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # remove spaces and convert to lowercase
    return s == s[::-1]

# 4. Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 5. Sum of Digits
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# 6. Find the Largest Element in a List
def find_largest_element(lst):
    return max(lst)

# 7. Anagram Check
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# 8. Reverse a String
def reverse_string(s):
    return s[::-1]

# 9. Count Vowels in a String
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

# 10. Find GCD (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 11. Count Words in a String
def count_words(s):
    return len(s.split())

# 12. Sort List of Tuples by Second Element
def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

# 13. Find Missing Number in List
def find_missing_number(lst, n):
    total_sum = n * (n + 1) // 2
    list_sum = sum(lst)
    return total_sum - list_sum

# 14. Merge Two Sorted Lists
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

# Example usage for each function:
print(f"Fibonacci sequence: {fibonacci(10)}")
print(f"Is 29 prime? {is_prime(29)}")
print(f"Is 'A man a plan a canal Panama' a palindrome? {is_palindrome('A man a plan a canal Panama')}")
print(f"Factorial of 5: {factorial(5)}")
print(f"Sum of digits of 12345: {sum_of_digits(12345)}")
print(f"Largest element in [3, 5, 7, 2, 8, 1]: {find_largest_element([3, 5, 7, 2, 8, 1])}")
print(f"Are 'listen' and 'silent' anagrams? {are_anagrams('listen', 'silent')}")
print(f"Reverse of 'hello': {reverse_string('hello')}")
print(f"Number of vowels in 'hello world': {count_vowels('hello world')}")
print(f"GCD of 56 and 98: {gcd(56, 98)}")
print(f"Number of words in 'Hello, how are you?': {count_words('Hello, how are you?')}")
print(f"Sorted list by second element: {sort_by_second_element([(1, 3), (2, 2), (3, 1)])}")
print(f"Missing number in [1, 2, 4, 5]: {find_missing_number([1, 2, 4, 5], 5)}")
print(f"Merged sorted list: {merge_sorted_lists([1, 3, 5], [2, 4, 6])}")
