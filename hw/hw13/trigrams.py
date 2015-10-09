import random

# Load the file and get first line
#  filename = "sherlock.txt"
#  filename = "sherlock_small.txt"
filename = "sherlock_med.txt"
#  filename = "testdata.txt"
print("Opening the file...")
target = open(filename, 'r')

booktext = target.readline()
booktext = booktext.rstrip('\n')
for line in target:
    line = line.rstrip('\n')  # remove end of line character
    booktext = booktext + ' ' + line  # remember to add a space at end of line

# use string functions to split into words
# and create a list of words
senwords = booktext.split(' ')
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
worddict = {'two words': ['word1', 'word2']}

# Make a loop to run through each word extracted from
# the first line in the file
no_of_words = len(senwords)
for i in range(no_of_words - 2):
    print('We are in loop {0} of {1} words {2} percent complete'
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
print(i)

# print(worddict)
print(str(len(worddict)))


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


def next_word(keyword, worddictionary):
    # Check that the keyword exists in the dictionary
    if keyword not in worddictionary:
        return False
    # get the list from the correct key
    next_word_list = worddictionary[keyword]
    print('next option list: ' + str(next_word_list))

    # Find at random the word from the word list
    i = 0
    select_index = random.randrange(0, len(next_word_list))
    for item in next_word_list:
        if i == select_index:
            outputindex = i
        i = i + 1

    return next_word_list[outputindex]


''' MAIN LOOP TO BUILD BOOK STARTS HERE  '''

# find a random word pair to start from
select_index = random.randrange(0, len(worddict))
print(select_index)
i = 0
for startkey in worddict:
    if i == select_index:
        text_out = startkey
    i = i + 1
print('The random start words are: {0}'.format(text_out))


# The starting keywords is text_out, use that to find the next word
next_word_is = next_word(text_out, worddict)
text_out = text_out + ' ' + next_word_is

# Loop around until there is no
wordlimit = 200
j = 0
con = True
while con is True:
    j = j + 1

    text_words = text_out.split(' ')
    # Select the last word pair from the new sentence
    keyword = text_words[-2] + ' ' + text_words[-1]

    # Look up this pair in the dictionary and find a random following word
    next_word_to_add = next_word(keyword, worddict)
    if next_word_to_add is False:
        print("No word pair exists in the dictionary so end the story here")
        con = False
        break

    # add to sentence
    text_out = text_out + ' ' + next_word_to_add

    if j == wordlimit:
        con = False

print(text_out)
