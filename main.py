def main():
    """
    Asks the user for the name of a book they'd like a report for and prints
    the contents of the report to standard output.
    """

    # ask user for title of book
    book = input('What book would you like a report for? ')

    # read lines of text from frankenstein.txt
    with open(f'books/{book.lower()}.txt') as f:
        file_contents = f.read()
    
    # process text to get number of words and counter of alphabetical chars
    n_words = len(file_contents.split())
    counter = count_characters(file_contents)

    # create lines of report
    first_line = '--- Begin report of books/frankenstein.txt ---'
    second_line = f'{n_words} words found in the document'
    last_line = '--- End report ---'

    # iterate through sorted counter dict and format strs with char and count
    # then joins the list of strings with the newline character.
    main_body = '\n'.join([
        f"The '{k}' character was found {v} times" 
        for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True)
        ])

    # create list of strings that contain the contents of the report
    contents = [
        first_line,
        second_line,
        '', # blank line between word count line and main body of report
        main_body,
        last_line
    ]

    # join each string with the newline character
    report = '\n'.join(contents)

    # print report to stdout
    print(report)

def count_characters(text):
    """Counts the number of times characters appear in some text"""
    counter = dict()

    for char in text.lower():
        if not char.isalpha():
            continue
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    
    return counter

if __name__ == '__main__':
    main()