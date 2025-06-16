# Open and read the contents of a text file
file_path = "FileHandling/notes.txt"  # Replace with your file name

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
