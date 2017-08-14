## # PYTHON 2 # ##
import random, pickle
import nltk, gensim, pronouncing
from num2words import num2words

from nltk.corpus import wordnet as wn
from nltk.corpus import webtext

model = gensim.models.KeyedVectors.load_word2vec_format("C:\Users\KatieAmazing\Anaconda2\pretrained_model\GoogleNews-vectors-negative300.bin", binary=True)

def syn_to_word(part_of_speech):
    picked = str(random.choice(list(wn.all_synsets(part_of_speech))))
    return picked.split(".")[0].replace("_", " ")[8:]

def common(word):
    if " " in word:
        word = word.split(" ")[-1]
    for fileid in webtext.fileids():
        if word in webtext.raw(fileid):
            print(word + " succeeded!")
            return True
    print(word + " failed for being uncommon.")
    return False

def random_noun():
    word = syn_to_word("n")
    while not common(word):
        word = syn_to_word("n")
    return word

def random_verb():
    word = syn_to_word("v")
    while " " in word or not common(word):
        word = syn_to_word("v")
    return word

def rhyme(word):
    if " " in word:
        word = word.split(" ")[-1]
    l = pronouncing.rhymes(word)
    if not l:
        return word
    rhyme = random.choice(l)
    seen_rhymes = set()
    while not common(rhyme):
        if len(seen_rhymes) == l:
            return word
        seen_rhymes.add(rhyme)
        rhyme = random.choice(l)
    return rhyme

def similar(word):
    if " " in word:
        word = word.split(" ")[-1]
    picked = str(random.choice(model.most_similar(word, topn=10)))
    print("Picked " + picked)
    proc = picked.split(",")[0][3:-1]
    print(proc)
    return proc.replace("_", " ")


def youbelong(a=None):
    I_nouns = ["I'm on the", "I've got this", "I have all this", "I'm made out of", "I'm under the", "I am mostly", "I wonder about", "I'm in love with"]
    a = a or random_noun()
    b = random_noun()

    payload = "She " + random_verb() + "s " + a + ",\nI " + random_verb() + " " + b + ",\nShe's " + similar(a) + ",\n" + random.choice(I_nouns) + " " + rhyme(b) + "."

    return payload

def blankspace(a=None):
    a = a or random_noun()

    payload = \
        "Boys only want " + a + " if it's torture,\nDon't say I didn't, say I didn't " + random_verb() + " you."

    return payload

def feeling22():
    age = num2words(random.randrange(21, 100))
    a = rhyme(age.split("-")[-1])

    payload = \
        "I don't know about " + a + ",\nI'm feeling " + age + "!"

    return payload


tweets = []
tweets.append(blankspace())
tweets.append(youbelong())
tweets.append(feeling22())

for t in tweets:
    print("\n")
    print t

f = open("tstweets.pkl", "wb")
pickle.dump(tweets, f)
f.close()
