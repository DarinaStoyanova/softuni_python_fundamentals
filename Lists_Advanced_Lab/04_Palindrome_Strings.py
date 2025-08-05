sequence = input().split(" ")
palindrome = input()

palindromes_in_sequence = [palin for palin in sequence if palin == palin[::-1]]
print(palindromes_in_sequence)
palindrome_count = [pal for pal in palindromes_in_sequence if pal == palindrome]
palindrome_count_times = len(palindrome_count)
print(f"Found palindrome {palindrome_count_times} times")