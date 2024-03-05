text = input("Enter a string: ")
text = text.lower()
letter_counts = {}

for char in text:
    if char.isalpha():
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

if letter_counts:
    print("Letter frequency:")
    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")
else:
    print("No lowercase letters found in the string.")
