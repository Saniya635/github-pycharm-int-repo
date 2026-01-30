for i in range(5):
    for j in range(i + 1):
        print(chr(65 + j), end="")
    print()



for i in range(1, 5):
    for j in range(i):
        print("#", end=" ")
    print()


letters = ['p', 'y', 't', 'h', 'o']

for i in range(len(letters)):
    print(letters[i] * (i + 1))


word = "python"
for i in range(len(word)):
        print(word[:i + 1])

