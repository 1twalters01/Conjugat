from populate import get_languages_from_file, get_Tense_dictionary, get_Subject_dictionary, get_Auxiliary_dictionary, get_Conjugate_dictionary, get_urls, get_sentences, create_json
import pickle
import math
import time

# Load the dictionaries
my_file = 'python/verbs/1. languages/languages.pkl'
languages = get_languages_from_file(my_file)

Tense_dict = get_Tense_dictionary(languages)
Subject_dict = get_Subject_dictionary(languages)
Auxiliary_dict = get_Auxiliary_dictionary(languages)
Conjugate_dict = get_Conjugate_dictionary(languages)


# Get the sentences
sentences = [[]]*len(languages)

for count in range(30):
    start = time.time()
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Presente', Tense_dict[0]['Indicativo Presente']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Participio Pasado', Tense_dict[0]['Participio Pasado']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito perfecto simple', Tense_dict[0]['Indicativo Pretérito perfecto simple']-1)
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito imperfecto', Tense_dict[0]['Indicativo Pretérito imperfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Gerundio', Tense_dict[0]['Gerundio']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito perfecto compuesto', Tense_dict[0]['Indicativo Pretérito perfecto compuesto']-1)
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Presente', Tense_dict[0]['Subjuntivo Presente']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Futuro', Tense_dict[0]['Indicativo Futuro']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Gerundio compuesto', Tense_dict[0]['Gerundio compuesto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Imperativo', Tense_dict[0]['Imperativo']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 700+math.floor(count*900/30)-1, 700+math.floor((count+1)*900/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Pretérito imperfecto', Tense_dict[0]['Subjuntivo Pretérito imperfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Condicional', Tense_dict[0]['Indicativo Condicional']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 600+math.floor(count*1000/30)-1, 1600+math.floor((count+1)*1000/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Pretérito imperfecto (2)', Tense_dict[0]['Subjuntivo Pretérito imperfecto (2)']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 700+math.floor(count*900/30)-1, 700+math.floor((count+1)*900/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito pluscuamperfecto', Tense_dict[0]['Indicativo Pretérito pluscuamperfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 600+math.floor(count*1000/30)-1, 600+math.floor((count+1)*1000/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Pretérito pluscuamperfecto', Tense_dict[0]['Subjuntivo Pretérito pluscuamperfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Pretérito pluscuamperfecto (2)', Tense_dict[0]['Subjuntivo Pretérito pluscuamperfecto (2)']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Infinitivo compuesto', Tense_dict[0]['Infinitivo compuesto']-1)
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1300+math.floor(count*700/30)-1, 1300+math.floor((count+1)*700/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Pretérito perfecto', Tense_dict[0]['Subjuntivo Pretérito perfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1600+math.floor(count*400/30)-1, 1600+math.floor((count+1)*400/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Futuro perfecto', Tense_dict[0]['Indicativo Futuro perfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1100+math.floor(count*900/30)-1, 1100+math.floor((count+1)*900/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Futuro', Tense_dict[0]['Subjuntivo Futuro']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 1300+math.floor(count*700/30)-1, 1300+math.floor((count+1)*700/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Condicional perfecto', Tense_dict[0]['Indicativo Condicional perfecto']-1)

    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 900+math.floor(count*1100/30)-1, 900+math.floor((count+1)*1100/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Indicativo Pretérito anterior', Tense_dict[0]['Indicativo Pretérito anterior']-1)
    
    urls = get_urls('Spanish', languages['Spanish']-1, [[]]*len(languages), 900+math.floor(count*1100/30)-1, 900+math.floor((count+1)*1100/30)-1)
    sentences = get_sentences(languages['Spanish']-1, sentences, urls, 'Subjuntivo Futuro perfecto', Tense_dict[0]['Subjuntivo Futuro perfecto']-1)
    end = time.time()
    print(end-start)
    print((end-start)*((40-count)/60), 'minutes remaining')


# Convert the sentences to pks:
pk = 173335
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
        with open('python/verbs/7. main/tuples/'+item+' C2.pkl', 'wb') as f:
            pickle.dump(sentences[index], f)


# Read the tuple to ensure it is correct
sentences = [()]*len(languages)
for index, item in enumerate(languages):
    try:
        myfile = 'python/verbs/7. main/tuples/'+item+' C2.pkl'
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
        f = open('python/verbs/7. main/json/'+item+' C2.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()