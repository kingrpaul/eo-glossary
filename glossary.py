from pprint import pprint
import re
import csv
import pprint


esperanto_uppercase = 'ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ'
esperanto_lowercase = 'abcĉdefgĝhĥijĵklmnoprsŝtuŭvz'
esperanto_letters = esperanto_uppercase + esperanto_lowercase
# string.ascii_letters
# string.ascii_lowercase
# string.ascii_uppercase¶

# v.
# v.tr
# v.ntr
# n.
# adj.
# adv.
# int.
# prep.
# corr. | table-word

glossary = []

class Entry:
    english = ""
    esperanto = ""
    comment = ""
    phrase = False
    noun = False 
    verb = False
    adverb = False
    ajective = False

    def __str__(self):
        return self.english + ",  " + self.esperanto + ":  " + self.comment[:20]

def is_table_word(g):
    s = g.esperanto
    if g.comment.startswith('corr.'):
        return(True)
    else:
        return(False)

def is_conjunction(g):
    s = g.esperanto
    if g.comment.startswith('conj.'):
        return(True)
    else:
        return(False)

def is_noun(g):
    s = g.esperanto
    if s.endswith('o'):
        return("noun")
    elif s.endswith('ojn'):
        return("noun_plural_accusative")
    elif s.endswith('oj'):
        return("noun_plural")
    elif s.endswith('on'):
        return("noun_accusative")
    elif g.comment.startswith('n.'):
        return(True)
    else:
        return(False)

def is_adjective(g):
    s = g.esperanto
    if s.endswith('a'):
        return("adjective")
    elif s.endswith('ajn'):
        return("adjective_plural_accusative")
    elif s.endswith('aj'):
        return("adjective_plural")
    elif s.endswith('an'):
        return("adjective_accusative")
    elif g.comment.startswith('adj.'):
        return(True)
    else:
        return(False)

def is_adverb(g):
    s = g.esperanto
    if s.endswith('e'):
        return("adverb")
    elif s.endswith('en'):
        return("adverb_accusative")
    elif g.comment.startswith('adv.'):
        return(True)
    else:
        return(False)

def is_verb(g):
    s = g.esperanto
    if s.endswith('i'):
        return("verb_infinitive")
    if s.endswith('as'):
        return("verb_present")
    if s.endswith('is'):
        return("verb_past")
    if s.endswith('os'):
        return("verb_future")
    if s.endswith('u'):
        return("verb_imperative")
    if s.endswith('us'):
        return("verb_conditional")
    elif g.comment.startswith('v.'):
        return(True)
    else:
        return(False)

def is_interjection(g):
    s = g.esperanto
    if g.comment.startswith('int.'):
        return(True)
    else:
        return(False)

def is_preposition(g):
    s = g.esperanto
    if g.comment.startswith('prep.'):
        return(True)
    else:
        return(False)

def is_multword(g):
    s = g.esperanto
    if ' ' in s:
        return(True)
    else:
        return(False)

pattern_line = re.compile("^.+\t.+\t.+")
dup_check = ""

import os
import string

word_list = []

for tsv_file in os.listdir():
    if tsv_file[-3:] == 'tsv' and 'wik' not in tsv_file:
        with open(tsv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter='	', quotechar='|')
            entries = [row for row in reader if len(row) > 0 and row[0][0] != '#' ]
            word_list.extend(entries)



invalid_entres = [l for l in word_list if not l[0][0].isalnum()]
if invalid_entres:
    pprint.pprint(invalid_entres)
    exit()

wrong_length_entries = [l for l in word_list if len(l) != 4]
if wrong_length_entries:
    pprint.pprint(wrong_length_entries)
    exit()

print(len(word_list))


            # for entry in entries:
            #     if len(entry) != 4:
            #         print(entry)

            # # No entry shall have more than 4 columns
            # long_entries = [entry[0] for entry in entries if len(entry)>4]
            # if long_entries:
            #     print("Too long entries:\n " + '-'*6 + '\n ' + " \n ".join(long_entries))
        
            # # No entry shall have fewer than 4 columns
            # short_entries = [entry[0] for entry in entries if len(entry)<4]
            # #Using VSCode: ^[^\t]+\t[^\t]+\t[^\t]+$
            # if short_entries:
            #     print("Too short entries:\n " + '-'*6 + '\n ' + " \n ".join(short_entries))
            
            # # Every entry shall one character in column-4
            # print(entries)
            # improper_final_column = [entry[0] for entry in entries if entry[3] and len(entry[3])>1]
            # if improper_final_column:
            #     print("Invalid last element:\n " + '-'*6 + '\n ' + " \n ".join(improper_final_column))

            # # Every entry shall indicate the part of speech at start of column-3
            # entry_types = ['v.', 'n.', 'adj.', 'adv.', 'int.', 'prep.', 'corr.', 'phr.', 'conj.', 'art.', 'int.', 'part.', 'abbr.']
            # def isvalid(s):
            #     for t in entry_types:
            #         if s.startswith(t):
            #             return(True)
            #     return(False)
            # no_part_of_speech = [entry[0] for entry in entries if not isvalid(entry[2])]
            # if no_part_of_speech:
            #     print("Invalid part of speech:\n " + '-'*6 + '\n ' + " \n ".join(no_part_of_speech))
      
    # CHECK IF VERBS ARE TRANSITIVE OR NOT 
     
           
    # lines = csvfile.readlines()
    # for line in lines:
    #     if "&&" in line:
    #         continue
    #     if not pattern_line.match(line):
    #         print("Misformed: " + line)
    #     if len(line.strip()) > 0:
    #         entry = Entry()
    #         try:
    #             entry.english, entry.esperanto, entry.comment = line.split('\t')
    #         except:
    #              print("Misformed: " + line)
            
    #         if "&" + entry.english + "&" + entry.esperanto + "&" in dup_check:
    #             print("Duplicate: ", entry)
    #         dup_check = dup_check + "&" + entry.english + "&" + entry.esperanto + "&"
            

    #         glossary = glossary + [entry]
    # num_table_words, num_conjunctions, num_nouns, num_adjectives, num_adverbs, num_verbs, num_interjections, num_prepositions, num_multiword = 0,0,0,0,0,0,0,0,0
    # for g in glossary:
    #     if is_table_word(g):
    #         num_table_words += 1
    #     elif is_conjunction(g):
    #         num_conjunctions += 1
    #     elif is_noun(g):
    #         num_nouns += 1
    #     elif is_adjective(g):
    #         num_adjectives += 1
    #     elif is_adverb(g):
    #         num_adverbs += 1
    #     elif is_verb(g):
    #         num_verbs += 1
    #     elif is_interjection(g):
    #         num_interjections += 1
    #     elif is_preposition(g):
    #         num_prepositions += 1
    #     elif is_multword(g):
    #         num_multiword += 1
    #     else:
    #         # print(g)
    #         pass

    # print(len(glossary) - 
    #       num_table_words - 
    #       num_conjunctions - 
    #       num_nouns - 
    #       num_adjectives - 
    #       num_adverbs - 
    #       num_verbs - 
    #       num_interjections - 
    #       num_prepositions - 
    #       num_multiword)