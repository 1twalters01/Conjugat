from bs4 import BeautifulSoup
import pickle
import re
import requests
import time


#1. Retrieve the languages in the language dictionary
myfile = 'python/verbs/1. languages/languages.pkl'
with (open(myfile, "rb")) as openfile:
    while True:
        try:
            languages = pickle.load(openfile)
        except EOFError:
            break
tuple_languages = tuple(languages)


#2. Get a list of verbs from the data in the text files
textfiles = ["python/verbs/2. romance base/word lists/"+x+" wordlist.txt" for x in languages]
f = [open(x, 'r', encoding="utf-8") for x in textfiles]
g = [open(x, 'r', encoding="utf-8") for x in textfiles]
verblist = [[]]*len(tuple_languages)

for integer, item in enumerate(f):
    # verblist[integer] = item.read().split('\n')[0:10]
    verblist[integer] = item.read().split('\n')[0:len(g[integer].readlines())]


#3. Get a url for each verb
urls = [[]]*len(tuple_languages)
noOfVerbs = int(len(verblist))
for n in range(len(languages)):
    for l in range(len(verblist[n])):
        urls[n] = urls[n] + ["https://conjugator.reverso.net/conjugation-" +tuple_languages[n]+ "-verb-" + verblist[n][l] + ".html"]


#4. Load the base tuple and turn it into a dictionary of the base and pk:
Tuple_Base = [[]]*len(languages)
for index, item in enumerate(languages):
    myfile = 'python/verbs/2. romance base/tuples/'+item+' Tenses.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                Tuple_Base[index] = pickle.load(openfile)
            except EOFError:
                break

dict_base = [{}, {},{},{},{}]
for index, language in enumerate(languages):
    for n in range(len(Tuple_Base[index])):
        dict_base[index].update({Tuple_Base[index][n][2]:Tuple_Base[index][n][0]})


#4. Get a list for the Conjugates
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

conj_dict = {}
conjugates = [[]]*len(tuple_languages)
for n in range(len(languages)):
    start = time.time()
    for k in range(len(urls[n])):
        print(urls[n][k], k)
        soup = BeautifulSoup(requests.get(urls[n][k]).text, 'lxml')
        results = soup.find_all('div', {'mobile-title': True})
        for i in range(len(results)):
            subjectholder = []
            itags = re.findall(r'<li>(.+?)</li>', str(results[i]))
            for j in range(len(itags)):
                onlyConjugates = keepConjugations(itags[j])
                subjectholder.append((onlyConjugates, dict_base[n][Tuple_Base[n][k][2]]))


                conj_dict.update({onlyConjugates:dict_base[n][Tuple_Base[n][k][2]]})
            conjugates[n] = conjugates[n] + subjectholder
        conjugates[n] = list(unique(conjugates[n]))
    end = time.time()
    print(end-start)
   

#5. Turn the conjugates into a tuple
pk = 1
Tuple_Conjugates = [()]*len(conjugates)
for n in range(len(languages)):
    for index, conjugate in enumerate(conjugates[n]):
        Tuple_Conjugates[n] = Tuple_Conjugates[n] + ((conjugate[0], conjugate[1], pk, languages[tuple_languages[n]]),)
        pk +=1


#6. Save the tuple in a pickle file as separate languages
for index, item in enumerate(languages):
    with open('python/verbs/6. Conjugates/tuples/'+item+' Conjugates.pkl', 'wb') as f:
        pickle.dump(Tuple_Conjugates[index], f)


#7. Read the tuple to ensure it is correct
Tuple_Conjugates = [()]*len(languages)
for index, item in enumerate(languages):
    myfile = 'python/verbs/6. Conjugates/tuples/'+item+' Conjugates.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                Tuple_Conjugates[index] = pickle.load(openfile)
            except EOFError:
                break


#8. Create the JSON file
json = ['''''']*len(tuple_languages)
for n in range(len(tuple_languages)):
    no_of_bases = len(Tuple_Conjugates[n])
    for i in range(no_of_bases):
        print(100*i/no_of_bases, '%')
        json[n] = json[n]+'''
    {
    "model": "verbs.romanceconjugation",
    "pk": '''+str(Tuple_Conjugates[n][i][2])+''',
    "fields": {
        "base": "'''+str(Tuple_Conjugates[n][i][1])+'''",
        "conjugation": "'''+Tuple_Conjugates[n][i][0]+'''"
    }
    },'''

    json[n] = json[n].rstrip(',')
    json[n] = '''['''+json[n]+'''
    ]'''
    print('done')


#9. Save the JSON file
jsonfiles = ["python/verbs/6. Conjugates/json/"+x+" Conjugates.json" for x in languages]
f = [open(x, 'w+', encoding="utf-8") for x in jsonfiles]

for n in range(len(tuple_languages)):
    f[n].write(json[n])

for x in range(len(f)):
    f[x].close()