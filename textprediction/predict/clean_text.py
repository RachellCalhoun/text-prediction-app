#import needed packages

# import numpy as np
# import nltk

import textstat
from collections import Counter

basic_english_words = ['come', 'get', 'give', 'go', 'keep', 'let', 'make', 'put', 'seem', 'take', 'be', 'do', 'have', 'say', 'see', 'send', 'may', 'will', 'about', 'across', 'after', 'against', 'among', 'at', 'before', 'between', 'by', 'down', 'from', 'in', 'off', 'on', 'over', 'through', 'to', 'under', 'up', 'with', 'as', 'for', 'of', 'till', 'than', 'a', 'the', 'all', 'any', 'every', 'no', 'other', 'some', 'such', 'that', 'this', 'I', 'he', 'you', 'who', 'and', 'because', 'but', 'or', 'if', 'though', 'while', 'how', 'when', 'where', 'why', 'again', 'ever', 'far', 'forward', 'here', 'near', 'now', 'out', 'still', 'then', 'there', 'together', 'well', 'almost', 'enough', 'even', 'little', 'much', 'not', 'only', 'quite', 'so', 'very', 'tomorrow', 'yesterday', 'north', 'south', 'east', 'west', 'please', 'yes', 'account', 'act', 'addition', 'adjustment', 'advertisement', 'agreement', 'air', 'amount', 'amusement', 'animal', 'answer', 'apparatus', 'approval', 'argument', 'art', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'back', 'balance', 'base', 'behaviour', 'belief', 'birth', 'bit', 'bite', 'blood', 'blow', 'body', 'brass', 'bread', 'breath', 'brother', 'building', 'burn', 'burst', 'business', 'butter', 'canvas', 'care', 'cause', 'chalk', 'chance', 'change', 'cloth', 'coal', 'colour', 'comfort', 'committee', 'company', 'comparison', 'competition', 'condition', 'connection', 'control', 'cook', 'copper', 'copy', 'cork', 'cotton', 'cough', 'country', 'cover', 'crack', 'credit', 'crime', 'crush', 'cry', 'current', 'curve', 'damage', 'danger', 'daughter', 'day', 'death', 'debt', 'decision', 'degree', 'design', 'desire', 'destruction', 'detail', 'development', 'digestion', 'direction', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'doubt', 'drink', 'driving', 'dust', 'earth', 'edge', 'education', 'effect', 'end', 'error', 'event', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'fact', 'fall', 'family', 'father', 'fear', 'feeling', 'fiction', 'field', 'fight', 'fire', 'flame', 'flight', 'flower', 'fold', 'food', 'force', 'form', 'friend', 'front', 'fruit', 'glass', 'gold', 'government', 'grain', 'grass', 'grip', 'group', 'growth', 'guide', 'harbour', 'harmony', 'hate', 'hearing', 'heat', 'help', 'history', 'hole', 'hope', 'hour', 'humour', 'ice', 'idea', 'impulse', 'increase', 'industry', 'ink', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'iron', 'jelly', 'join', 'journey', 'judge', 'jump', 'kick', 'kiss', 'knowledge', 'land', 'language', 'laugh', 'law', 'lead', 'learning', 'leather', 'letter', 'level', 'lift', 'light', 'limit', 'linen', 'liquid', 'list', 'look', 'loss', 'love', 'machine', 'man', 'manager', 'mark', 'market', 'mass', 'meal', 'measure', 'meat', 'meeting', 'memory', 'metal', 'middle', 'milk', 'mind', 'mine', 'minute', 'mist', 'money', 'month', 'morning', 'mother', 'motion', 'mountain', 'move', 'music', 'name', 'nation', 'need', 'news', 'night', 'noise', 'note', 'number', 'observation', 'offer', 'oil', 'operation', 'opinion', 'order', 'organization', 'ornament', 'owner', 'page', 'pain', 'paint', 'paper', 'part', 'paste', 'payment', 'peace', 'person', 'place', 'plant', 'play', 'pleasure', 'point', 'poison', 'polish', 'porter', 'position', 'powder', 'power', 'price', 'print', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 'pull', 'punishment', 'purpose', 'push', 'quality', 'question', 'rain', 'range', 'rate', 'ray', 'reaction', 'reading', 'reason', 'record', 'regret', 'relation', 'religion', 'representative', 'request', 'respect', 'rest', 'reward', 'rhythm', 'rice', 'river', 'road', 'roll', 'room', 'rub', 'rule', 'run', 'salt', 'sand', 'scale', 'science', 'sea', 'seat', 'secretary', 'selection', 'self', 'sense', 'servant', 'sex', 'shade', 'shake', 'shame', 'shock', 'side', 'sign', 'silk', 'silver', 'sister', 'size', 'sky', 'sleep', 'slip', 'slope',
                       'smash', 'smell', 'smile', 'smoke', 'sneeze', 'snow', 'soap', 'society', 'son', 'song', 'sort', 'sound', 'soup', 'space', 'stage', 'start', 'statement', 'steam', 'steel', 'step', 'stitch', 'stone', 'stop', 'story', 'stretch', 'structure', 'substance', 'sugar', 'suggestion', 'summer', 'support', 'surprise', 'swim', 'system', 'talk', 'taste', 'tax', 'teaching', 'tendency', 'test', 'theory', 'thing', 'thought', 'thunder', 'time', 'tin', 'top', 'touch', 'trade', 'transport', 'trick', 'trouble', 'turn', 'twist', 'unit', 'use', 'value', 'verse', 'vessel', 'view', 'voice', 'walk', 'war', 'wash', 'waste', 'water', 'wave', 'wax', 'way', 'weather', 'week', 'weight', 'wind', 'wine', 'winter', 'woman', 'wood', 'wool', 'word', 'work', 'wound', 'writing', 'year', 'angle', 'ant', 'apple', 'arch', 'arm', 'army', 'baby', 'bag', 'ball', 'band', 'basin', 'basket', 'bath', 'bed', 'bee', 'bell', 'berry', 'bird', 'blade', 'board', 'boat', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain', 'brake', 'branch', 'brick', 'bridge', 'brush', 'bucket', 'bulb', 'button', 'cake', 'camera', 'card', 'cart', 'carriage', 'cat', 'chain', 'cheese', 'chest', 'chin', 'church', 'circle', 'clock', 'cloud', 'coat', 'collar', 'comb', 'cord', 'cow', 'cup', 'curtain', 'cushion', 'dog', 'door', 'drain', 'drawer', 'dress', 'drop', 'ear', 'egg', 'engine', 'eye', 'face', 'farm', 'feather', 'finger', 'fish', 'flag', 'floor', 'fly', 'foot', 'fork', 'fowl', 'frame', 'garden', 'girl', 'glove', 'goat', 'gun', 'hair', 'hammer', 'hand', 'hat', 'head', 'heart', 'hook', 'horn', 'horse', 'hospital', 'house', 'island', 'jewel', 'kettle', 'key', 'knee', 'knife', 'knot', 'leaf', 'leg', 'library', 'line', 'lip', 'lock', 'map', 'match', 'monkey', 'moon', 'mouth', 'muscle', 'nail', 'neck', 'needle', 'nerve', 'net', 'nose', 'nut', 'office', 'orange', 'oven', 'parcel', 'pen', 'pencil', 'picture', 'pig', 'pin', 'pipe', 'plane', 'plate', 'plough', 'pocket', 'pot', 'potato', 'prison', 'pump', 'rail', 'rat', 'receipt', 'ring', 'rod', 'roof', 'root', 'sail', 'school', 'scissors', 'screw', 'seed', 'sheep', 'shelf', 'ship', 'shirt', 'shoe', 'skin', 'skirt', 'snake', 'sock', 'spade', 'sponge', 'spoon', 'spring', 'square', 'stamp', 'star', 'station', 'stem', 'stick', 'stocking', 'stomach', 'store', 'street', 'sun', 'table', 'tail', 'thread', 'throat', 'thumb', 'ticket', 'toe', 'tongue', 'tooth', 'town', 'train', 'tray', 'tree', 'trousers', 'umbrella', 'wall', 'watch', 'wheel', 'whip', 'whistle', 'window', 'wing', 'wire', 'worm', 'able', 'acid', 'angry', 'automatic', 'beautiful', 'black', 'boiling', 'bright', 'broken', 'brown', 'cheap', 'chemical', 'chief', 'clean', 'clear', 'common', 'complex', 'conscious', 'cut', 'deep', 'dependent', 'early', 'elastic', 'electric', 'equal', 'fat', 'fertile', 'first', 'fixed', 'flat', 'free', 'frequent', 'full', 'general', 'good', 'great', 'grey', 'hanging', 'happy', 'hard', 'healthy', 'high', 'hollow', 'important', 'kind', 'like', 'living', 'long', 'male', 'married', 'material', 'medical', 'military', 'natural', 'necessary', 'new', 'normal', 'open', 'parallel', 'past', 'physical', 'political', 'poor', 'possible', 'present', 'private', 'probable', 'quick', 'quiet', 'ready', 'red', 'regular', 'responsible', 'right', 'round', 'same', 'second', 'separate', 'serious', 'sharp', 'smooth', 'sticky', 'stiff', 'straight', 'strong', 'sudden', 'sweet', 'tall', 'thick', 'tight', 'tired', 'true', 'violent', 'waiting', 'warm', 'wet', 'wide', 'wise', 'yellow', 'young', 'awake', 'bad', 'bent', 'bitter', 'blue', 'certain', 'cold', 'complete', 'cruel', 'dark', 'dead', 'dear', 'delicate', 'different', 'dirty', 'dry', 'false', 'feeble', 'female', 'foolish', 'future', 'green', 'ill', 'last', 'late', 'left', 'loose', 'loud', 'low', 'mixed', 'narrow', 'old', 'opposite', 'public', 'rough', 'sad', 'safe', 'secret', 'short', 'shut', 'simple', 'slow', 'small', 'soft', 'solid', 'special', 'strange', 'thin', 'white', 'wrong']

def count_intersections(lst1, lst2):
    c1 = Counter(lst1)
    c2 = Counter(lst2)
    return { k: min(c1[k], c2[k]) for k in c1.keys() & c2.keys() }


def clean_text_input(text):

    basic_english = basic_english_words
  #length of string
    length = len(text)

  #number of characters
    char_count = textstat.char_count(text, ignore_spaces=True)
    letter_count = textstat.letter_count(text,  ignore_spaces=True)

  #tag each for in a sentence with part of speech, then swap all proper nouns with the word "noun".
    # tagged_sentence = nltk.tag.pos_tag(text.split())
    # text_nouns_removed = [word if tag != 'NNP' else 'noun' for word,tag in tagged_sentence]
    text_nouns_removed = text

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
    return [values]
