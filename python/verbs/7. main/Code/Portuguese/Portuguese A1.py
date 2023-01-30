from populate import get_languages_from_file, get_Tense_dictionary, get_Subject_dictionary, get_Auxiliary_dictionary, get_Conjugate_dictionary, get_urls, get_sentences, create_json
import pickle

# Load the dictionaries
my_file = 'python/verbs/1. languages/languages.pkl'
languages = get_languages_from_file(my_file)

Tense_dict = get_Tense_dictionary(languages)
Subject_dict = get_Subject_dictionary(languages)
Auxiliary_dict = get_Auxiliary_dictionary(languages)
Conjugate_dict = get_Conjugate_dictionary(languages)


# Get the sentences
sentences = [[]]*len(languages)

urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 0, 35)
sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Presente', Tense_dict[1]['Indicativo Presente']-1)

# urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 0, 30)
# sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Perfeito', Tense_dict[1]['Indicativo Pretérito Perfeito']-1)

# urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 0, 30)
# sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Imperfeito', Tense_dict[1]['Indicativo Pretérito Imperfeito']-1)

# urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 35, 80)
# sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Presente', Tense_dict[1]['Indicativo Presente']-1)

# urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 30, 55)
# sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Perfeito', Tense_dict[1]['Indicativo Pretérito Perfeito']-1)

# urls = get_urls('Portuguese', languages['Portuguese']-1, [[]]*len(languages), 30, 55)
# sentences = get_sentences(languages['Portuguese']-1, sentences, urls, 'Indicativo Pretérito Imperfeito', Tense_dict[1]['Indicativo Pretérito Imperfeito']-1)



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