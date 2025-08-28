#Creating the input.txt file
print("Creating input.text file...")
try:
    with open("input.txt, "w") as f:
        f.write("Here we go..\n")
        f.write("Python is a versatile programming language.\n")
        f.write("File handling in Python is easy and powerful.\n")
        f.write("This is the fourth line of text.\n")
        f.write("And this is the fifth and final line.\n")
    print("input.txt created successfully.")
except IOError as e:
    print(f"Error creating input.txt: {e}")
    # Exit the script if file creation fails.
    exit()

# Part 2: Process the text from input.txt and write to output.txt
# This part reads the input file, processes the content, and writes the results to a new file.
print("\nProcessing text and creating output.txt...")
try:
    # Read the entire content of input.txt
    with open("input.txt", "r") as infile:
        content = infile.read()

    # 1. Count the number of words in the file.
    # The split() method on a string, with no arguments, splits by any whitespace and handles multiple spaces gracefully.
    word_count = len(content.split())

    # 2. Convert all text to uppercase.
    processed_content = content.upper()

    # 3. Write the processed text and the word count to output.txt.
    with open("output.txt", "w") as outfile:
        outfile.write("PROCESSED TEXT:\n\n")
        outfile.write(processed_content)
        outfile.write("\n\n--------------------\n")
        outfile.write(f"WORD COUNT: {word_count}\n")

    # 4. Print a success message.
    print("Success! output.txt has been created with the processed text and word count.")

except FileNotFoundError:
    print("Error: The file input.txt was not found. Please ensure it exists.")
except IOError as e:
    print(f"Error reading or writing files: {e}")

