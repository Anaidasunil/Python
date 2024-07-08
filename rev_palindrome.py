def reverse_num(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    while True:
        reversed_n = reverse_num(n)
        sum_n = n + reversed_n
        if is_palindrome(sum_n):
            return sum_n
        n = sum_n

num = int(input("Enter a number: "))
result = reverse_and_add(num)
print("The resulting palindrome is:", result)
