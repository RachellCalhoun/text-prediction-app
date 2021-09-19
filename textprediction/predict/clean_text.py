#import needed packages

import numpy as np
import nltk

import textstat
from collections import Counter

def count_intersections(lst1, lst2):
    c1 = Counter(lst1)
    c2 = Counter(lst2)
    return { k: min(c1[k], c2[k]) for k in c1.keys() & c2.keys() }


def clean_text_input(text):
    my_file = open('BasicEnglish.csv', "r")
    content = my_file.read()
    basic_english = content.split(",")
    my_file.close()
    basic_english = [x.strip(' ') for x in basic_english]

  #length of string
    length = len(text)

  #number of characters
    char_count = textstat.char_count(text, ignore_spaces=True)
    letter_count = textstat.letter_count(text,  ignore_spaces=True)

  #tag each for in a sentence with part of speech, then swap all proper nouns with the word "noun".
    tagged_sentence = nltk.tag.pos_tag(text.split())
    text_nouns_removed = [word if tag != 'NNP' else 'noun' for word,tag in tagged_sentence]
    text_nouns_removed = ' '.join(text_nouns_removed)

  #calculate text stat variables
    flesch_reading_ease = textstat.flesch_reading_ease(text_nouns_removed)
    gunning_fog =  textstat.gunning_fog(text_nouns_removed)
    automated_readability_index =  textstat.automated_readability_index(text_nouns_removed)
    coleman_liau_index = textstat.coleman_liau_index(text_nouns_removed)
    dale_chall_readability_score =  textstat.dale_chall_readability_score(text_nouns_removed)
    text_standard = textstat.text_standard(text_nouns_removed,  float_output=True)

  #other various sentence features
    syllable_count = textstat.syllable_count(text_nouns_removed)
    num_of_words_nopunct =  textstat.lexicon_count(text_nouns_removed,  removepunct=False)
    num_of_words = textstat.lexicon_count(text_nouns_removed,  removepunct=True)
    polysyllable_word_count =  textstat.polysyllabcount(text_nouns_removed)

    is_num = 0

    avg_syllables = syllable_count/num_of_words if syllable_count and num_of_words else 0

    basic_english_count = sum(count_intersections(str(text_nouns_removed).split(), basic_english).values())
    perct_basic_english = basic_english_count / num_of_words if basic_english_count and num_of_words else 0


    values = [
        flesch_reading_ease,
        gunning_fog,
        automated_readability_index,
        coleman_liau_index,
        dale_chall_readability_score,
        text_standard,
        avg_syllables,
        num_of_words_nopunct,
        polysyllable_word_count,
        length,
        char_count,
        letter_count,
        perct_basic_english
    ]
    return np.array([values])