sequence = input().split(" ")
final_text = ""

for word in sequence:
    repeated_times = len(word)
    final_text += word * repeated_times

print(final_text)