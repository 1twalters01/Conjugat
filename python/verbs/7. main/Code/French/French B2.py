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
    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 450+math.floor(count*450/12), 450+math.floor((count+1)*450/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Indicatif Présent', Tense_dict[3]['Indicatif Présent']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 450+math.floor(count*450/12), 450+math.floor((count+1)*450/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Participe Passé', Tense_dict[3]['Participe Passé']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 450+math.floor(count*450/12), 450+math.floor((count+1)*450/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Indicatif Passé composé', Tense_dict[3]['Indicatif Passé composé']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 450+math.floor(count*450/12), 450+math.floor((count+1)*450/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Indicatif Futur', Tense_dict[3]['Indicatif Futur']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 450+math.floor(count*450/12), 450+math.floor((count+1)*450/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Indicatif Imparfait', Tense_dict[3]['Indicatif Imparfait']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 350+math.floor(count*550/12), 350+math.floor((count+1)*550/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Conditionnel Present', Tense_dict[3]['Conditionnel Present']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 300+math.floor(count*600/12), 300+math.floor((count+1)*600/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Subjonctif Present', Tense_dict[3]['Subjonctif Present']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 300+math.floor(count*600/12), 300+math.floor((count+1)*600/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Imperatif Present', Tense_dict[3]['Imperatif Present']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), 300+math.floor(count*600/12), 300+math.floor((count+1)*600/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Indicatif Plus-Que-Parfait', Tense_dict[3]['Indicatif Plus-Que-Parfait']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), math.floor(count*700/12), math.floor((count+1)*700/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Conditionnel Passé première forme', Tense_dict[3]['Conditionnel Passé première forme']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), math.floor(count*700/12), math.floor((count+1)*700/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Subjonctif Passé', Tense_dict[3]['Subjonctif Passé']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), math.floor(count*600/12), math.floor((count+1)*600/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Imperatif Passé', Tense_dict[3]['Imperatif Passé']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), math.floor(count*600/12), math.floor((count+1)*300/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Participe Présent', Tense_dict[3]['Participe Présent']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), math.floor(count*600/12), math.floor((count+1)*600/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Participe Passé Composé', Tense_dict[3]['Participe Passé Composé']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), math.floor(count*500/12), math.floor((count+1)*500/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Indicatif Passé Simple', Tense_dict[3]['Indicatif Passé Simple']-1)

    urls = get_urls('French', languages['French']-1, [[]]*len(languages), math.floor(count*700/12), math.floor((count+1)*700/12))
    sentences = get_sentences(languages['French']-1, sentences, urls, 'Indicatif Future Anterieur', Tense_dict[3]['Indicatif Future Anterieur']-1)


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
for index, item in enumerate(languages):
    try:
        myfile = 'python/verbs/7. main/tuples/'+item+' B2.pkl'
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
        f = open('python/verbs/7. main/json/'+item+' B2.json', 'w+', encoding="utf-8")
        f.write(json[index])
        f.close()