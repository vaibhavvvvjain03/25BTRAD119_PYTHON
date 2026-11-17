text = input("Enter a sentence: ").lower()

words = text.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print("\nWord Frequencies:")

for word, frequency in count.items():
    print(word, ":", frequency)

print("\nTotal words:", len(words))
print("Unique words:", len(count))