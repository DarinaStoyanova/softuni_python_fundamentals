received_text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
text_with_no_vowels = [let for let in received_text if let not in vowels]
print("".join(text_with_no_vowels))