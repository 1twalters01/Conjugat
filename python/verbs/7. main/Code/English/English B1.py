from populate import get_languages_from_file, get_Tense_dictionary, get_Subject_dictionary, get_Auxiliary_dictionary, get_Conjugate_dictionary, get_urls, get_sentences, create_json
import pickle
import math

# Load the dictionaries
my_file = 'python/verbs/1. languages/languages.pkl'
languages = get_languages_from_file(my_file)

Tense_dict = get_Tense_dictionary(languages)
Subject_dict = get_Subject_dictionary(languages)
Auxiliary_dict = get_Auxiliary_dictionary(languages)
Conjugate_dict = get_Conjugate_dictionary(languages)


# Get the sentences
sentences = [[]]*len(languages)
for count in range(12):
    urls = get_urls('English', languages['English']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Indicative Present', Tense_dict[4]['Indicative Present']-1)

    urls = get_urls('English', languages['English']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Participle Past', Tense_dict[4]['Participle Past']-1)

    urls = get_urls('English', languages['English']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Indicative Preterite', Tense_dict[4]['Indicative Preterite']-1)
    
    urls = get_urls('English', languages['English']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Indicative Future', Tense_dict[4]['Indicative Future']-1)
    
    urls = get_urls('English', languages['English']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Indicative Present perfect', Tense_dict[4]['Indicative Present perfect']-1)

    urls = get_urls('English', languages['English']-1, [[]]*len(languages), math.floor(count*350/12), math.floor((count+1)*350/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Participle Present', Tense_dict[4]['Participle Present']-1)
    
    urls = get_urls('English', languages['English']-1, [[]]*len(languages), math.floor(count*300/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Indicative Present continuous', Tense_dict[4]['Indicative Present continuous']-1)

    urls = get_urls('English', languages['English']-1, [[]]*len(languages), math.floor(count*300/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['English']-1, sentences, urls, 'Imperative', Tense_dict[4]['Imperative']-1)


# Convert the sentences to pks:
pk = 3600
for index in range(len(tuple(languages))):
    for rank, sentence in enumerate(sentences[index]):
        print(sentence)
        pk +=1
        tense = Tense_dict[index][sentence[0]]
        subject = Subject_dict[index][sentence[1]]
        auxiliary = Auxiliary_dict[index][sentence[2]]
        conjugate = Conjugate_dict[index][sentence[3]]
        sentences[index][rank] = (pk, rank+1, tense, subject, auxiliary, conjugate)


# Save the tuple in a pickle file as separate languages
for index, item in enumerate(languages):
    if sentences[index]:
        with open('python/verbs/7. main/tuples/'+item+' B1.pkl', 'wb') as f:
            pickle.dump(sentences[index], f)


# Read the tuple to ensure it is correct
sentences = [()]*len(languages)
try:
    myfile = 'python/verbs/7. main/tuples/'+'English'+' B1.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                sentences[4] = pickle.load(openfile)
            except EOFError:
                break
except:
    sentences[index] = []
print(sentences)


# Create the JSON file
json = ['''''']*len(sentences)
json = create_json(sentences, json)


# Save the JSON file
for index, item in enumerate(languages):
    if sentences[index]:
        f = open('python/verbs/7. main/json/'+item+' B1.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()