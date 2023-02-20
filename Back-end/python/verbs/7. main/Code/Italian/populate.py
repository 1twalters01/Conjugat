from bs4 import BeautifulSoup
import pickle
import re
import requests


def get_languages_from_file(myfile):
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                languages = pickle.load(openfile)
            except EOFError:
                break
    return languages


def get_Tense_dictionary(languages):
    Tuple_Tenses = [[]]*len(languages)
    for index, item in enumerate(languages):
        myfile = 'python/verbs/3. Tenses/tuples/'+item+' Tenses.pkl'
        with (open(myfile, "rb")) as openfile:
            while True:
                try:
                    Tuple_Tenses[index] = pickle.load(openfile)
                except EOFError:
                    break

    tense_dict = [{}, {}, {}, {}, {}]
    for index, language in enumerate(languages):
        for n in range(len(Tuple_Tenses[index])):
            tense_dict[index].update({Tuple_Tenses[index][n][1]:Tuple_Tenses[index][n][0]})
    return tense_dict


def get_Subject_dictionary(languages):
    Tuple_Subjects = [()]*len(languages)
    for index, item in enumerate(languages):
        myfile = 'python/verbs/4. Subjects/tuples/'+item+' Subjects.pkl'
        with (open(myfile, "rb")) as openfile:
            while True:
                try:
                    Tuple_Subjects[index] = pickle.load(openfile)
                except EOFError:
                    break

    subject_dict = [{}, {},{},{},{}]
    for index, language in enumerate(languages):
        for n in range(len(Tuple_Subjects[index])):
            subject_dict[index].update({Tuple_Subjects[index][n][0]:Tuple_Subjects[index][n][1]})
    return subject_dict


def get_Auxiliary_dictionary(languages):
    tuple_Auxiliaries = [()]*len(languages)
    for index, item in enumerate(languages):
        myfile = 'python/verbs/5. auxiliaries/tuples/'+item+' auxiliaries.pkl'
        with (open(myfile, "rb")) as openfile:
            while True:
                try:
                    tuple_Auxiliaries[index] = pickle.load(openfile)
                except EOFError:
                    break

    auxiliary_dict = [{}, {},{},{},{}]
    for index, language in enumerate(languages):
        for n in range(len(tuple_Auxiliaries[index])):
            auxiliary_dict[index].update({tuple_Auxiliaries[index][n][0]:tuple_Auxiliaries[index][n][1]})
    return auxiliary_dict


def get_Conjugate_dictionary(languages):
    Tuple_Conjugates = [()]*len(languages)
    for index, item in enumerate(languages):
        myfile = 'python/verbs/6. Conjugates/tuples/'+item+' Conjugates.pkl'
        with (open(myfile, "rb")) as openfile:
            while True:
                try:
                    Tuple_Conjugates[index] = pickle.load(openfile)
                except EOFError:
                    break

    conjugate_dict = [{}, {},{},{},{}]
    for index, language in enumerate(languages):
        for n in range(len(Tuple_Conjugates[index])):
            conjugate_dict[index].update({Tuple_Conjugates[index][n][0]:Tuple_Conjugates[index][n][2]})
    return conjugate_dict


def get_urls(language, pk, urls, start, end):
    textfiles = "python/verbs/2. romance base/word lists/"+language+" wordlist.txt"
    f = open(textfiles, 'r', encoding="utf-8")
    verb_list = f.read().split('\n')[start:end]
    for verb in range(len(verb_list)):
        urls[pk] = urls[pk] + ["https://conjugator.reverso.net/conjugation-" +language+ "-verb-" + verb_list[verb] + ".html"]
    return urls




def keepSubjects(x):
    x = re.sub('<i class="verbtxt.*?</i>', '', x)
    x = re.sub('<i class="a.*?</i>', '', x)
    x = re.sub('<i class="p.*?</i>', '', x)
    x = re.sub('<i.*?>', '', x)
    x = re.sub('</i.*?>', '', x).rstrip()
    return x
def keepAuxiliaries(x):
    x = re.sub('<i class="verbtxt.*?</i>', '', x)
    x = re.sub('<i class="graytxt.*?</i>', '', x)
    x = re.sub('<i.*?>', '', x)
    x = re.sub('</i.*?>', '', x).rstrip()
    return x
def keepConjugations(x):
    x = re.sub('<i class="a.*?</i>', '', x)
    x = re.sub('<i class="p.*?</i>', '', x)
    x = re.sub('<i class="graytxt.*?</i>', '', x)
    x = re.sub('<i.*?>', '', x)
    x = re.sub('</i.*?>', '', x).replace(" ", "")
    return x

def unique(seq):
    seen = set()
    for item in seq:
        if item not in seen:
            seen.add( item )
            yield item

def get_sentences(language_pk, sentences, urls, tense, tense_pk):
    for url in range(len(urls[language_pk])):
        
        soup = BeautifulSoup(requests.get(urls[language_pk][url]).text, 'lxml')
        results = soup.find_all('div', {'mobile-title': True})
        print(urls[language_pk][url], len(results))
        try:
            results_sorted = results[tense_pk]
        except:
            results_sorted = None
        subjectholder = []
        complete = False
        if results_sorted:
            current_tense = results_sorted['mobile-title'].strip()
            if str(current_tense) == tense:
                print(tense)
                complete = True
                itags = re.findall(r'<li>(.+?)</li>', str(results_sorted))
                for j in range(len(itags)):
                    onlySubjects = keepSubjects(itags[j])
                    onlyAuxiliaries = keepAuxiliaries(itags[j])
                    onlyConjugates = keepConjugations(itags[j])
                    subjectholder.append((tense, onlySubjects, onlyAuxiliaries, onlyConjugates))

                sentences[language_pk] = sentences[language_pk] + subjectholder
        if complete == False:
            for i in range(len(results)):
                current_tense = results[i]['mobile-title'].strip()
                if str(current_tense) == tense:
                    print(tense)
                    itags = re.findall(r'<li>(.+?)</li>', str(results[i]))
                    for j in range(len(itags)):
                        onlySubjects = keepSubjects(itags[j])
                        onlyAuxiliaries = keepAuxiliaries(itags[j])
                        onlyConjugates = keepConjugations(itags[j])
                        subjectholder.append((tense, onlySubjects, onlyAuxiliaries, onlyConjugates))

                    sentences[language_pk] = sentences[language_pk] + subjectholder
                sentences[language_pk] = list(unique(sentences[language_pk]))
    return sentences


def create_json(sentences, json):
    for n in range(len(sentences)):
        no_of_bases = len(sentences[n])
        for i in range(no_of_bases):
            print(100*i/no_of_bases, '%')
            json[n] = json[n]+'''
    {
    "model": "verbs.romancemain",
    "pk": '''+str(sentences[n][i][0])+''',
    "fields": {
        "rank": "'''+str(sentences[n][i][1])+'''",
        "tense": "'''+str(sentences[n][i][2])+'''",
        "subject": "'''+str(sentences[n][i][3])+'''",
        "auxiliary": "'''+str(sentences[n][i][4])+'''",
        "conjugation": "'''+str(sentences[n][i][5])+'''"
    }
    },'''

        json[n] = json[n].rstrip(',')
        json[n] = '''['''+json[n]+'''
        ]'''
    return json