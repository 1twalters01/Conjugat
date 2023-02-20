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

for count in range(8):
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 80+count*15, 80+(count+1)*15)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Presente', Tense_dict[0]['Indicativo Presente']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 55+math.floor(count*18.125), 55+math.floor((count+1)*18.125))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Participio Pasado', Tense_dict[0]['Participio Pasado']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), count*25, (count+1)*25)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito perfecto simple', Tense_dict[0]['Indicativo Pretérito perfecto simple']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*17.5), math.floor((count+1)*17.5))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito imperfecto', Tense_dict[0]['Indicativo Pretérito imperfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), count*25, (count+1)*25)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Gerundio', Tense_dict[0]['Gerundio']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*17.5), math.floor((count+1)*17.5))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito perfecto compuesto', Tense_dict[0]['Indicativo Pretérito perfecto compuesto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*17.5), math.floor((count+1)*17.5))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Futuro', Tense_dict[0]['Indicativo Futuro']-1)





# Convert the sentences to pks:
pk = 534
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
        with open('python/verbs/7. main/tuples/'+item+' A2.pkl', 'wb') as f:
            pickle.dump(sentences[index], f)


# Read the tuple to ensure it is correct
sentences = [()]*len(languages)
for index, item in enumerate(languages):
    try:
        myfile = 'python/verbs/7. main/tuples/'+item+' A2.pkl'
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
        f = open('python/verbs/7. main/json/'+item+' A2.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()