def sort_on(item):
    return item["count"]

def count_characters(text):
    text = text.lower()
    character_counts = {}

    for character in text:
        if character.isalpha():
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1

    # Turn dictionary into list of dictionaries
    character_counts_list = [{"char": c, "count": n} for c, n in character_counts.items()]
    
    # sort the list by count
    character_counts_list.sort(key=sort_on, reverse=True)

    return character_counts_list

def count_words(text):
    words = text.split()
    return len(words)

def main():
    # Open the file with read permissions
    with open("books/frankenstein.txt", "r") as f:
        # Read all contents of the file into a string
        file_contents = f.read()

        # Print the start of the report
        print("--- Begin report of frankenstein.txt ---")

        # Count and print the number of words in the book
        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document")

        # Count and print the number of each character in the book
        character_counts = count_characters(file_contents)
        for character_info in character_counts:
            print(f"The '{character_info['char']}' character was found {character_info['count']} times")

        # Print the end of the report
        print("--- End report ---")

# Run the main function
if __name__ == "__main__":
    main()

