sentence = input(" Enter a sentence \n")

vowels = "aeiouAEIOU"

consonants = "bcdghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

v_count=0
c_count = 0

for char in sentence:
    if char in vowels:
        v_count+=1

    if char in consonants:
        c_count+=1


print(f"Number of vowels: {v_count}")
print(f"Number of consonants: {c_count}")