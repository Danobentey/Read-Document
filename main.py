# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    story = open(filename, 'r').read()
    
    return story

#read_file_content('story.txt')

def count_words(text):
    text = read_file_content(text).lower()
    
    x, y = text.count('as '), text.count('would ')

    return {"as": x, "would": y}

count_words("story.txt")
