import random


def open_file(filename):
    print("Opening the file...")
    target = open(filename, 'r')
    return target


def read_file(filetoread):
    booktext = filetoread.readline()
    booktext = booktext.rstrip('\n')
    for line in filetoread:
        line = line.rstrip('\n')  # remove end of line character
        booktext = booktext + ' ' + line  # add a space at end of line
    return booktext


''' **************************************************'''
''' These settings are used to print stuff out or not '''
debug = True
detaildebug = True


# Load the file and get first line
#  bookfilename = "sherlock.txt"
#  bookfilename = "sherlock_small.txt"
#  bookfilename = "testdata.txt"
bookfilename = "sherlock_fourlines.txt"
#  bookfilename = "sherlock_med.txt"
bookfile = open_file(bookfilename)
booktext = read_file(bookfile)

# use string functions to split into words
# and create a list of words
senwords = booktext.split(' ')
if debug:
    print('The file is opened ready to combine words...')


''' The loop strategy is
First find the first 2 words in the sentence
    Check - is that pair a key in the dictionary?
        if Yes
            Add the following word to the list for that key in the dictionary
        if no
            Append the key:[list] pair to the dictionay
repeat for the next word in the sentence until end of sentence
'''
# Initialise the dictionary
# (there must be a better way so i don't need to do this)
worddict = {'initialise': ['initialise']}

# Make a loop to run through each word extracted from
# the first line in the file
no_of_words = len(senwords)
for i in range(no_of_words - 2):
    if debug:
        print('We are in loop {0} of {1} words. {2} percent complete'
              .format(i, len(senwords), str(100 * i / no_of_words)))
    newkey = senwords[i] + " " + senwords[i + 1]

    # first check if the first two words already exist in our dictionary
    for existingkey in worddict:
        if existingkey == newkey:
            KeyExists = True
            break
        else:
            KeyExists = False

    if KeyExists is True:
        # key is already in dictionary so add to the list
        worddict[newkey].append(senwords[i + 2])
    else:
        # key does not exist so add Key :value[list]
        worddict[newkey] = [senwords[i + 2]]

#  Remove the initialisation wordkey from dict
del worddict['initialise']

# close the file
bookfile.close


if detaildebug:
    print('Counter {}'.format(i))

# print(worddict)
print(booktext)
print(worddict)
if detaildebug:
    print('length (number of wordpair keys with following word) '
          'of stored dictionary {}'.format(str(len(worddict))))


#  now to reassemble the text
'''
The Logic is select a starting word pair at random
    then select at random one of the subsequent list to follow it
    now find the last two words of the new sentecne
    then look up those words and randomly find a potential following words
    repeat till we find a word pair that is not in the dictionary or till
    the word limit is met
'''

#  Create a Function that will find the next word by inputing two
#  words and selecting at random from the dictionary
# Function next word takes a keyword and dictionary and selects
# a random output from the list.


def rand_word_from_list(wordlist, debug):
    # Find at random the word from a word list
    i = 0
    outputindex = 0
    select_index = random.randrange(0, len(wordlist))
    for item in wordlist:
        if i == select_index:
            outputindex = i
        i = i + 1
    outputwrd = wordlist[outputindex]
    if debug:
        print('The random item from the list is {}'.format(outputwrd))
    return outputwrd


def next_word(keyword, worddictionary, debug):
    # Check that the keyword exists in the dictionary
    if keyword not in worddictionary:
        return False
    # get the list from the correct key
    next_word_list = worddictionary[keyword]
    if detaildebug:
        print('next option list: ' + str(next_word_list))

    # Find at random the word from the word list and output
    return rand_word_from_list(next_word_list, debug)

''' MAIN LOOP TO BUILD BOOK STARTS HERE  '''

# find a random word pair to start from
select_index = random.randrange(0, len(worddict))
if detaildebug:
    print('random starting index {}'.format(select_index))
i = 0
for startkey in worddict:
    if i == select_index:
        text_out = startkey
    i = i + 1
if detaildebug:
    print('The random starting words are: {0}'.format(text_out))


# The starting keywords is text_out, use that to find the next word
next_word_is = next_word(text_out, worddict, debug)
text_out = text_out + ' ' + next_word_is

# Loop around until no wordpair exists in dictionary or wordlimit hit
wordlimit = 200
j = 0
con = True
while con is True:
    j = j + 1

    text_words = text_out.split(' ')
    # Select the last word pair from the new sentence
    keyword = text_words[-2] + ' ' + text_words[-1]

    # Look up this pair in the dictionary and find a random following word
    next_word_to_add = next_word(keyword, worddict, debug)
    if next_word_to_add is False:
        if debug:
            print('The word pair {} does not have a list (following word)'
                  ' in the dictionary'
                  ' so end the story here'.format(keyword))
        con = False
        break

    # add to sentence
    text_out = text_out + ' ' + next_word_to_add

    if j == wordlimit:
        con = False

#  text_out = add_third_word(text_out)
print(text_out)
