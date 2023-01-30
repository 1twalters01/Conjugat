from bs4 import BeautifulSoup
import pickle
import requests

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
verblist = [[]]*len(tuple_languages)

for integer, item in enumerate(f):
    verblist[integer] = item.read().split('\n')[0]


#3. Get a url for each verb
urls = [[]]*len(tuple_languages)
noOfVerbs = int(len(verblist))
for n in range(len(languages)):
    urls[n] = "https://conjugator.reverso.net/conjugation-" +tuple_languages[n]+ "-verb-" + verblist[n] + ".html"


#4. Get a list for the tenses.
Tenses = [[]]*len(tuple_languages)
for n in range(len(languages)):
    url = urls[n]

    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    results = soup.find_all('div', {'mobile-title': True})
    Tenses[n] = [s['mobile-title'] if s is not None else None for s in results]
    Tenses[n] = [j.strip() for j in Tenses[n]]


#5. Turn the tenses into a tuple
pk = 1
Tuple_Tenses = [()]*len(Tenses)
for n in range(len(languages)):
    for index, tense in enumerate(Tenses[n]):
        Tuple_Tenses[n] = Tuple_Tenses[n] + ((pk,tense, languages[tuple_languages[n]]),)
        pk += 1


#6. Save the tuple in a pickle file as separate languages
for index, item in enumerate(languages):
    with open('python/verbs/3. Tenses/tuples/'+item+' Tenses.pkl', 'wb') as f:
        pickle.dump(Tuple_Tenses[index], f)


#7. Read the tuple to ensure it is correct
Tuple_Tenses = [[]]*len(languages)
for index, item in enumerate(languages):
    myfile = 'python/verbs/3. Tenses/tuples/'+item+' Tenses.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                Tuple_Tenses[index] = pickle.load(openfile)
            except EOFError:
                break
print(Tuple_Tenses)


#8. Create the JSON file
json = ['''''']*len(tuple_languages)
for n in range(len(tuple_languages)):
    no_of_bases = len(Tuple_Tenses[n])
    for i in range(no_of_bases):
        json[n] = json[n]+'''
    {
    "model": "verbs.romancetense",
    "pk": '''+str(Tuple_Tenses[n][i][0])+''',
    "fields": {
        "language": "'''+str(Tuple_Tenses[n][i][2])+'''",
        "tense": "'''+str(Tuple_Tenses[n][i][1])+'''"
    }
    },'''

    json[n] = json[n].rstrip(',')
    json[n] = '''['''+json[n]+'''
    ]'''


#9. Save the JSON file
jsonfiles = ["python/verbs/3. Tenses/json/"+x+" Tenses.json" for x in languages]
f = [open(x, 'w+', encoding="utf-8") for x in jsonfiles]

for n in range(len(tuple_languages)):
    f[n].write(json[n])

for x in range(len(f)):
    f[x].close()