#lab assignment 1
with open("input.txt", "r") as f:
    content = f.read()
upper_content = content.upper()
with open("output.txt", "w") as f:
    f.write(upper_content)
print("File copied with uppercase content.")

#lab assignment 2
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")
with open(source, "r") as f1, open(destination, "w") as f2:
    for line in f1:
        if not line.strip().startswith("#"):
            f2.write(line)
print("\nSource File Content:")
with open(source, "r") as f:
    print(f.read())
print("\nDestination File Content (without comments):")
with open(destination, "r") as f:
    print(f.read())