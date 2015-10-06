# Name: Henry Rebbeck
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
#  Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
# Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument\
     when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


########################################################################
# Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
a_count = 0
c_count = 0
g_count = 0
t_count = 0
err_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

    # next, if the bp is as A or a T,
    if bp == 'A' or bp == "T":
        at_count = at_count + 1
    if bp == 'G':
        g_count = g_count + 1
    if bp == 'C':
        c_count = c_count + 1
    if bp == 'A':
        a_count = a_count + 1
    if bp == 'T':
        t_count = t_count + 1
    '''
    if bp != 'A' and bp != 'C' and bp != 'G' and bp != 'T':
        err_count = err_count + 1
        print("Error at count", a_count + c_count + g_count + t_count)
        print("BP = ", bp)
    '''

# divide the gc_count by the total_count to find %
# use the g,c,a,t count rather than total as there are
# some errors in the total which should not be included

sum_gcat = g_count + c_count + a_count + t_count
gc_content = float(gc_count) / sum_gcat

# divide the at count by the total_count to find %
at_content = float(at_count) / sum_gcat

# divide the indvidual count by the total_count to find %
g_content = float(g_count) / total_count
c_content = float(c_count) / total_count
a_content = float(a_count) / total_count
t_content = float(t_count) / total_count


# Print the answer
print('GC-content:', gc_content)
#  Print the answer
print('AT-content:', at_content)

#  Print the % of ecah nucleotide
''' Not needed
print('G-content:', g_content)
print('C-content:', c_content)
print('A-content:', a_content)
print('T-content:', t_content)
'''

# Print the count of each nucleotide
print('G-Count:', g_count)
print('C-Count:', c_count)
print('A-Count:', a_count)
print('T-Count:', t_count)

# print the sum of each letter
sum_count = a_count + c_count + g_count + t_count
print('Sum of G,C,A,T count', sum_count)

# Check to see if the total % nucleotide summs to 100%
# sum_content = a_content + c_content + g_content + t_content
# print('Sum of G, C, A and T:', sum_content)
print('Total count:', total_count)
length_of_seq = len(seq)
print('Length of sequence:', length_of_seq)

# Print the AT/GC Ratio
print('AT/GC Ratio: ', (a_count + t_count) / (g_count + c_count))

# print errors
# print('Error count', err_count)

# Classify the resulting GC content into high, medium low GC
if gc_content > 0.6:
    print('GC Classification: high GC content')
elif gc_content < 0.4:
    print('GC Classification: low GC content')
else:
    print('GC Classification: moderate GC content')
