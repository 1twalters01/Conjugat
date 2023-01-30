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
    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Presente', Tense_dict[2]['Indicativo Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Participio Passato', Tense_dict[2]['Participio Passato']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Passato prossimo', Tense_dict[2]['Indicativo Passato prossimo']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Imperfetto', Tense_dict[2]['Indicativo Imperfetto']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Futuro semplice', Tense_dict[2]['Indicativo Futuro semplice']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*350/12), math.floor((count+1)*350/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Condizionale Presente', Tense_dict[2]['Condizionale Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*300/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Congiuntivo Presente', Tense_dict[2]['Congiuntivo Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*300/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Imperativo Presente', Tense_dict[2]['Imperativo Presente']-1)


# Convert the sentences to pks:
pk = 0
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
    myfile = 'python/verbs/7. main/tuples/'+'Italian'+' B1.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                sentences[index] = pickle.load(openfile)
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
        f = open('python/verbs/7. main/json/'+item+' B1.json', 'w+', encoding="utf-12")
        f.write(json[index])
        f.close()