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
for count in range(25):
    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 450+math.floor(count*450/25), 450+math.floor((count+1)*450/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Presente', Tense_dict[2]['Indicativo Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 450+math.floor(count*450/25), 450+math.floor((count+1)*450/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Participio Passato', Tense_dict[2]['Participio Passato']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 450+math.floor(count*450/25), 450+math.floor((count+1)*450/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Passato prossimo', Tense_dict[2]['Indicativo Passato prossimo']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 450+math.floor(count*450/25), 450+math.floor((count+1)*450/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Imperfetto', Tense_dict[2]['Indicativo Imperfetto']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 450+math.floor(count*450/25), 450+math.floor((count+1)*450/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Futuro semplice', Tense_dict[2]['Indicativo Futuro semplice']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 350+math.floor(count*550/25), 350+math.floor((count+1)*550/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Condizionale Presente', Tense_dict[2]['Condizionale Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 300+math.floor(count*600/25), 300+math.floor((count+1)*600/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Congiuntivo Presente', Tense_dict[2]['Congiuntivo Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 300+math.floor(count*600/25), 300+math.floor((count+1)*600/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Imperativo Presente', Tense_dict[2]['Imperativo Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*700/25), math.floor((count+1)*700/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Trapassato prossimo', Tense_dict[2]['Indicativo Trapassato prossimo']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*700/25), math.floor((count+1)*310/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Gerundio Presente', Tense_dict[2]['Gerundio Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*700/25), math.floor((count+1)*700/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Participio Presente', Tense_dict[2]['Participio Presente']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*600/25), math.floor((count+1)*600/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Condizionale Passato', Tense_dict[2]['Condizionale Passato']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*600/25), math.floor((count+1)*600/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Gerundio Passato', Tense_dict[2]['Gerundio Passato']-1)

    urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*600/25), math.floor((count+1)*600/25))
    sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Congiuntivo Passato', Tense_dict[2]['Congiuntivo Passato']-1)


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
        with open('python/verbs/7. main/tuples/'+item+' B2.pkl', 'wb') as f:
            pickle.dump(sentences[index], f)


# Read the tuple to ensure it is correct
sentences = [()]*len(languages)
try:
    myfile = 'python/verbs/7. main/tuples/'+'Italian'+' B2.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                sentences[2] = pickle.load(openfile)
            except EOFError:
                break
except:
    sentences[2] = []
print(sentences)


# Create the JSON file
json = ['''''']*len(sentences)
json = create_json(sentences, json)


# Save the JSON file
for index, item in enumerate(languages):
    if sentences[index]:
        f = open('python/verbs/7. main/json/'+item+' B2.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()