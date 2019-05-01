# Patrick Gravelle 10141195 Assignment no. 4
# For the optional portion of the assignment the most used word over 5 letters
# that occurs in all 4 speeches is the word "people".
def edits(filename, newfile) :
    """ Inputing the speech file analyzes the data, and return
    the results of the speech.
    """
    holder = open(filename)
    file = holder.read()
    sentences = file.count(".")+file.count("!")+file.count("?")
# Clean up of the file
    file = file.replace("\n"," ")
    file = file.replace("-"," ")
    file = file.lower()
    while file.count("  ") > 0 :
        file = file.replace("  "," ")
    clean = ""
    for aChar in file :
        if aChar.isalpha() or aChar == " " :
            clean = clean + aChar
    characters = len(clean)
    print(f"{characters} characters.")
    print(f"{sentences} sentences.")
    words = clean.count(" ") + 1
    print(f"{words} words.")
# Further organizing the file into a sorted list and set
    cleaned = sorted(clean.split())    
    uniqueWords = set(cleaned)
    print(str(len(uniqueWords)) + " unique words.")
    print(str("%.2f" % (len(uniqueWords) / words*100)) + "% of the words are unique.")
# Computing the occurences of words
    self = cleaned.count("i")
    print(str("%.2f" % (self/words*100)) + "% of the words are I.")
# Finding the longest words
    longword = 0
    for word in cleaned :
        length = len(word)
        if length > longword :
            longword = length
            output = word
        if word not in output and length == longword :
            output = output, word
    print("The longest word(s) is(are): ", output)
# Creating lists to combine to form a dictionary
    unilist = sorted(uniqueWords)
    occurences = []
    for word in unilist :
        num = cleaned.count(word)
        occurences.append(num)
    dictionary = dict()
    for i in range(len(unilist)) :
        dictionary[unilist[i]] = occurences[i]
# Creating a new file containing each word and its frequency
    outputfile = open(newfile,'w')
    for key in unilist :
        line = str(key) + " " + str(dictionary[key])+"\n"
        outputfile.write(line)
    outputfile.close()
# Optional portion of the assignment
    optional = []
    for word in unilist :
        if len(word) > 5 :
            optional.append(word)
    optcount = []
    for word in optional :
        total = cleaned.count(word)
        optcount.append(total)
    paired = zip(optional,optcount)
    combined = list(paired)
    frequent = sorted(combined, key=lambda frequency: frequency[1], reverse = True)
    i = 0
    print("The 10 most used words over 5 letters are: ")
    while i < 10 :
        print(frequent[i])
        i = i + 1
    holder.close()
    
def main() :
    try :
        print("Harper's Speech:")
        edits('harper.txt', 'harperdict.txt')
        print("\n"+"-------------------"+"\n")
        print("Obama's Inugural Speech:")
        edits('obama.txt', 'obamadict.txt')
        print("\n"+"-------------------"+"\n")
        print("Obama's Berlin Speech:")
        edits('obamaberlin.txt', 'obamaberlindict.txt')
        print("\n"+"-------------------"+"\n")
        print("Trump's Speech:")
        edits('trump.txt', 'trumpdict.txt')
        print("\n"+"-------------------"+"\n")
    except OSError :
        print("No such file or directory. Exiting.")
        return
    except ValueError :
        print("Value Error, exiting.")
        return
    
main()
