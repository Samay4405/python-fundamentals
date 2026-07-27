# Word Counter Tool

# Ask user for the file name
file_name = input("Enter text file name: ")

try:
    # Open the file in read mode
    with open(file_name, "r") as file:
        text = file.read()   # read entire file content

    # Count number of characters
    char_count = len(text)

    # Count number of lines
    line_count = text.count("\n") + 1 if text else 0

    # Split text into words using whitespace
    words = text.split()
    word_count = len(words)

    # Display results
    print("\n--- File Statistics ---")
    print("Lines      :", line_count)
    print("Words      :", word_count)
    print("Characters :", char_count)

except FileNotFoundError:
    # Handle case where file does not exist
    print("Error: File not found.")

except Exception as e:
    # Handle any unexpected errors
    print("Error:", e)
