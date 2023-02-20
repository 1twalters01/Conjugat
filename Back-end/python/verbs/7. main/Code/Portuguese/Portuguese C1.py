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
for count in range(40):
    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Presente', Tense_dict[1]['Indicativo Presente']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Perfeito', Tense_dict[1]['Indicativo Pretérito Perfeito']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Imperfeito', Tense_dict[1]['Indicativo Pretérito Imperfeito']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Participio', Tense_dict[1]['Participio']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Futuro do Presente Simples', Tense_dict[1]['Indicativo Futuro do Presente Simples']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Condicional Futuro do Pretérito Simples', Tense_dict[1]['Condicional Futuro do Pretérito Simples']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Conjuntivo / Subjuntivo Presente', Tense_dict[1]['Conjuntivo / Subjuntivo Presente']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Imperativo', Tense_dict[1]['Imperativo']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Imperativo Negativo', Tense_dict[1]['Imperativo Negativo']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Conjuntivo / Subjuntivo Pretérito Perfeito', Tense_dict[1]['Conjuntivo / Subjuntivo Pretérito Perfeito']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 900+math.floor(count*700/40), 900+math.floor((count+1)*700/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Gerundio', Tense_dict[1]['Gerundio']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 700+math.floor(count*900/40), 700+math.floor((count+1)*900/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Conjuntivo / Subjuntivo Pretérito Imperfeito', Tense_dict[1]['Conjuntivo / Subjuntivo Pretérito Imperfeito']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 700+math.floor(count*900/40), 700+math.floor((count+1)*900/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Mais-que-Perfeito', Tense_dict[1]['Indicativo Pretérito Mais-que-Perfeito']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 600+math.floor(count*1000/40), 600+math.floor((count+1)*1000/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Conjuntivo / Subjuntivo Futuro', Tense_dict[1]['Conjuntivo / Subjuntivo Futuro']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 600+math.floor(count*1000/40), 600+math.floor((count+1)*1000/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Perfeito Composto', Tense_dict[1]['Indicativo Pretérito Perfeito Composto']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 600+math.floor(count*1000/40), 600+math.floor((count+1)*1000/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Futuro do Presente Composto', Tense_dict[1]['Indicativo Futuro do Presente Composto']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), math.floor(count*1300/40), math.floor((count+1)*1300/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Conjuntivo / Subjuntivo Futuro Composto', Tense_dict[1]['Conjuntivo / Subjuntivo Futuro Composto']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), math.floor(count*1300/40), math.floor((count+1)*1300/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Mais-que-Perfeito Composto', Tense_dict[1]['Indicativo Pretérito Mais-que-Perfeito Composto']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), math.floor(count*1100/40), math.floor((count+1)*1100/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Conjuntivo / Subjuntivo Pretérito Mais-que-Perfeito Composto', Tense_dict[1]['Conjuntivo / Subjuntivo Pretérito Mais-que-Perfeito Composto']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), math.floor(count*1100/40), math.floor((count+1)*1100/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Condicional Futuro do Pretérito Composto', Tense_dict[1]['Condicional Futuro do Pretérito Composto']-1)

    urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), math.floor(count*1100/40), math.floor((count+1)*1100/40))
    sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Mais-que-Perfeito Anterior', Tense_dict[1]['Indicativo Pretérito Mais-que-Perfeito Anterior']-1)





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
        with open('python/verbs/7. main/tuples/'+item+' A1.pkl', 'wb') as f:
            pickle.dump(sentences[index], f)


# Read the tuple to ensure it is correct
sentences = [()]*len(languages)
try:
    myfile = 'python/verbs/7. main/tuples/'+item+' A1.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                sentences[1] = pickle.load(openfile)
            except EOFError:
                break
except:
    sentences[1] = []
print(sentences)


# Create the JSON file
json = ['''''']*len(sentences)
json = create_json(sentences, json)


# Save the JSON file
for index, item in enumerate(languages):
    if sentences[index]:
        f = open('python/verbs/7. main/json/'+item+' A1.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()