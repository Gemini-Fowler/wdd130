import random
#for the creativity portion, I added a bit of logic so that the code can use complex sentence structure(although, I still have to  get it to make the stories make more sense)
articles_singular = ["a", "one", "the"]
articles_plural = ["some", "many", "the"]

nouns_singular = ["man", "woman", "dog", "cat", "horse", "boar"]
nouns_plural = ["men", "women", "dogs", "cats", "horses", "boars"]

verbs_present_singular = ["eats", "sleeps", "walks", "thinks", "runs", "waits"]
verbs_present_plural = ["eat", "sleep", "walk", "think", "run", "wait"]

verbs_past_singular = ["ate", "slept", "walked", "thought", "ran", "waited"]
verbs_past_plural = ["ate", "slept", "walked", "thought", "ran", "waited"]

verbs_future = ["will eat", "will sleep", "will walk", "will think", "will run", "will wait"]

prepositions = ["on", "in", "under", "over", "beside", "with", "at"]
conjunctions = ["and", "but", "so", "because", "although", "while"]

def get_determiner(quantity):
    if quantity == 1:
        return random.choice(articles_singular)
    else:
        return random.choice(articles_plural)

def get_noun(quantity):
    if quantity == 1:
        return random.choice(nouns_singular)
    else:
        return random.choice(nouns_plural)

def get_verb(quantity, tense="present"):
    if tense == "present":
        if quantity == 1:
            return random.choice(verbs_present_singular)
        else:
            return random.choice(verbs_present_plural)
    elif tense == "past":
        if quantity == 1:
            return random.choice(verbs_past_singular)
        else:
            return random.choice(verbs_past_plural)
    elif tense == "future":
        return random.choice(verbs_future)

def get_preposition():
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def get_conjunction():
    return random.choice(conjunctions)

def make_complex_sentence(quantity, tense):
    determiner_1 = get_determiner(quantity)
    noun_1 = get_noun(quantity)
    verb_1 = get_verb(quantity, tense)
    prepositional_phrase_1 = get_prepositional_phrase(quantity)

    cap_determiner_1 = determiner_1.capitalize()
    sentence_1 = f"{cap_determiner_1} {noun_1} {verb_1} {prepositional_phrase_1}"

    if random.random() < 0.5:
        conjunction = get_conjunction()

        determiner_2 = get_determiner(quantity)
        noun_2 = get_noun(quantity)
        verb_2 = get_verb(quantity, tense)
        prepositional_phrase_2 = get_prepositional_phrase(quantity)

        sentence_2 = f"{determiner_2} {noun_2} {verb_2} {prepositional_phrase_2}"

        full_sentence = f"{sentence_1} {conjunction} {sentence_2}."
    else:
        full_sentence = f"{sentence_1}."

    return full_sentence

def main():
    sentence_a = make_complex_sentence(1, "past")
    print(sentence_a)

    sentence_b = make_complex_sentence(1, "present")
    print(sentence_b)

    sentence_c = make_complex_sentence(1, "future")
    print(sentence_c)

    sentence_d = make_complex_sentence(2, "past")
    print(sentence_d)

    sentence_e = make_complex_sentence(2, "present")
    print(sentence_e)

    sentence_f = make_complex_sentence(2, "future")
    print(sentence_f)

if __name__ == "__main__":
    main()
