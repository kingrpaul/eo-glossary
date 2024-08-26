from pprint import pprint
import re


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
with open("raw.txt") as raw:
    lines = raw.readlines()
    for line in lines:
        if "&&" in line:
            continue
        if not pattern_line.match(line):
            print("Misformed: " + line)
        if len(line.strip()) > 0:
            entry = Entry()
            try:
                entry.english, entry.esperanto, entry.comment = line.split('\t')
            except:
                 print("Misformed: " + line)
            
            if "&" + entry.english + "&" + entry.esperanto + "&" in dup_check:
                print("Duplicate: ", entry)
            dup_check = dup_check + "&" + entry.english + "&" + entry.esperanto + "&"
            

            glossary = glossary + [entry]
    num_table_words, num_conjunctions, num_nouns, num_adjectives, num_adverbs, num_verbs, num_interjections, num_prepositions, num_multiword = 0,0,0,0,0,0,0,0,0
    for g in glossary:
        if is_table_word(g):
            num_table_words += 1
        elif is_conjunction(g):
            num_conjunctions += 1
        elif is_noun(g):
            num_nouns += 1
        elif is_adjective(g):
            num_adjectives += 1
        elif is_adverb(g):
            num_adverbs += 1
        elif is_verb(g):
            num_verbs += 1
        elif is_interjection(g):
            num_interjections += 1
        elif is_preposition(g):
            num_prepositions += 1
        elif is_multword(g):
            num_multiword += 1
        else:
            # print(g)
            pass

    print(len(glossary) - 
          num_table_words - 
          num_conjunctions - 
          num_nouns - 
          num_adjectives - 
          num_adverbs - 
          num_verbs - 
          num_interjections - 
          num_prepositions - 
          num_multiword)