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
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Presente', Tense_dict[0]['Indicativo Presente']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Participio Pasado', Tense_dict[0]['Participio Pasado']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito perfecto simple', Tense_dict[0]['Indicativo Pretérito perfecto simple']-1)
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito imperfecto', Tense_dict[0]['Indicativo Pretérito imperfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 200+math.floor(count*250/12), 200+math.floor((count+1)*250/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Gerundio', Tense_dict[0]['Gerundio']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito perfecto compuesto', Tense_dict[0]['Indicativo Pretérito perfecto compuesto']-1)
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*450/12), math.floor((count+1)*450/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Presente', Tense_dict[0]['Subjuntivo Presente']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 140+math.floor(count*310/12), 140+math.floor((count+1)*310/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Futuro', Tense_dict[0]['Indicativo Futuro']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*450/12), math.floor((count+1)*450/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Imperativo', Tense_dict[0]['Imperativo']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*350/12), math.floor((count+1)*350/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Condicional', Tense_dict[0]['Indicativo Condicional']-1)

    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*300/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Pretérito imperfecto', Tense_dict[0]['Subjuntivo Pretérito imperfecto']-1)
    
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*300/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito pluscuamperfecto', Tense_dict[0]['Indicativo Pretérito pluscuamperfecto']-1)
    
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), math.floor(count*300/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Futuro perfecto', Tense_dict[0]['Indicativo Futuro perfecto']-1)
    

# Convert the sentences to pks:
pk = 5313
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
for index, item in enumerate(languages):
    try:
        myfile = 'python/verbs/7. main/tuples/'+item+' B1.pkl'
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
        f = open('python/verbs/7. main/json/'+item+' B1.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()