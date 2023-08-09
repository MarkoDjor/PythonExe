def extract_first_word(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.strip().split()
            if words:
                return words[0]
    return None

def main():
    file_path = '/home/marko/Documents/tiny_python_projects/text_rnd.txt'

    first_word = extract_first_word(file_path)

    if first_word is not None:
        print("The first word in the file is:", first_word)
    else:
        print("The file is empty or does not contain any words.")

if __name__ == "__main__":
    main()