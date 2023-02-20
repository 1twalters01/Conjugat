from populate import get_languages_from_file, get_Tense_dictionary, get_Subject_dictionary, get_Auxiliary_dictionary, get_Conjugate_dictionary, get_urls, get_sentences, create_json
import pickle
import math

# Load the dictionaries
my_file = 'python/verbs/1. languages/languages.pkl'
languages = get_languages_from_file(my_file)

# Tense_dict = get_Tense_dictionary(languages)
# Subject_dict = get_Subject_dictionary(languages)
# Auxiliary_dict = get_Auxiliary_dictionary(languages)
# Conjugate_dict = get_Conjugate_dictionary(languages)


# # Get the sentences
# sentences = [[]]*len(languages)
# for count in range(8):
#     urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 80+math.floor(count*120/8), 80+math.floor((count+1)*120/8))
#     sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Presente', Tense_dict[2]['Indicativo Presente']-1)

#     urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 55+math.floor(count*145/8), 55+math.floor((count+1)*145/8))
#     sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Participio Passato', Tense_dict[2]['Participio Passato']-1)

#     urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), 55+math.floor(count*145/8), 55+math.floor((count+1)*145/8))
#     sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Passato prossimo', Tense_dict[2]['Indicativo Passato prossimo']-1)

#     urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*140/8), math.floor((count+1)*140/8))
#     sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Imperfetto', Tense_dict[2]['Indicativo Imperfetto']-1)

#     urls = get_urls('Italian', languages['Italian']-1, [[]]*len(languages), math.floor(count*140/8), math.floor((count+1)*140/8))
#     sentences = get_sentences(languages['Italian']-1, sentences, urls, 'Indicativo Futuro semplice', Tense_dict[2]['Indicativo Futuro semplice']-1)


# # Convert the sentences to pks:
# pk = 870
# for index in range(len(tuple(languages))):
#     for rank, sentence in enumerate(sentences[index]):
#         print(sentence)
#         pk +=1
#         tense = Tense_dict[index][sentence[0]]
#         subject = Subject_dict[index][sentence[1]]
#         auxiliary = Auxiliary_dict[index][sentence[2]]
#         conjugate = Conjugate_dict[index][sentence[3]]
#         sentences[index][rank] = (pk, rank+1, tense, subject, auxiliary, conjugate)


# # Save the tuple in a pickle file as separate languages
# for index, item in enumerate(languages):
#     if sentences[index]:
#         with open('python/verbs/7. main/tuples/'+item+' A2.pkl', 'wb') as f:
#             pickle.dump(sentences[index], f)


# Read the tuple to ensure it is correct
sentences = [()]*len(languages)
try:
    myfile = 'python/verbs/7. main/tuples/'+'Italian'+' A2.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                sentences[2] = pickle.load(openfile)
            except EOFError:
                break
except:
    sentences[2] = []


# Create the JSON file
json = ['''''']*len(sentences)
json = create_json(sentences, json)


# Save the JSON file
for index, item in enumerate(languages):
    if sentences[index]:
        f = open('python/verbs/7. main/json/'+item+' A2.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()