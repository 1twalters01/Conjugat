from bs4 import BeautifulSoup
import http.client
import pickle
import re
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


#2. Turn the dictionary of languages into a list of urls
word_list_urls = [[]]*len(tuple_languages)
for index, item in enumerate(tuple_languages):
    for n in range(8):
        word_list_urls[index] = word_list_urls[index] + ["https://conjugator.reverso.net/index-"+item.lower() + "-" + str(250*(n)+1) + "-" + str(250*(n+1)) + ".html"]


#3. Scrape all of the words from these urls and turn it into a list
http.client._MAXHEADERS = 1000
bases = [[]]*len(tuple_languages)
for i in range(len(tuple_languages)):
    for x in range(len(word_list_urls[i])):
        soup = BeautifulSoup(requests.get(word_list_urls[i][x]).text, 'lxml')
        divs = soup.find_all('div', class_ = 'index-content')
        for tag in divs:
            lis = tag.find_all("li")
            for l in lis:
                bases[i] = bases[i] + [re.compile(r'<[^>]+>').sub('', str(l)).strip()]


#4. Create and save the files for the word list from the languages chosen
textfiles = ["python/verbs/2. romance base/word lists/"+x+" wordlist.txt" for x in languages]
f = [open(x, 'w+', encoding="utf-8") for x in textfiles]

for n in range(len(tuple_languages)):
    f[n].write('\n'.join(bases[n]))

for x in range(len(f)):
    f[x].close()


#5. Turn the tenses into a tuple
pk = 1
Tuple_Base = [()]*len(bases)
for n in range(len(languages)):
    for rank, base in enumerate(bases[n]):
        Tuple_Base[n] = Tuple_Base[n] + ((pk, rank, base, languages[tuple_languages[n]]),)
        pk += 1


#6. Create and save tuple for the main file
for index, item in enumerate(languages):
    with open('python/verbs/2. romance base/tuples/'+item+' Tenses.pkl', 'wb') as f:
        pickle.dump(Tuple_Base[index], f)


#7. Read the tuple to ensure it is correct
Tuple_Base = [[]]*len(languages)
for index, item in enumerate(languages):
    myfile = 'python/verbs/2. romance base/tuples/'+item+' Tenses.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                Tuple_Base[index] = pickle.load(openfile)
            except EOFError:
                break
print(Tuple_Base)


#5. Create the JSON file
json = ['''''']*len(tuple_languages)
for n in range(len(tuple_languages)):
    no_of_bases = len(Tuple_Base[n])
    
    for i in range(no_of_bases):
        json[n] = json[n]+'''
    {
    "model": "verbs.romancebase",
    "pk": '''+str(Tuple_Base[n][i][0])+''',
    "fields": {
        "rank": '''+str(Tuple_Base[n][i][1])+''',
        "language": "'''+str(languages[tuple_languages[n]])+'''",
        "base": "'''+Tuple_Base[n][i][2]+'''"
    }
    },'''

    json[n] = json[n].rstrip(',')
    json[n] = '''['''+json[n]+'''
    ]'''


#6. Save the JSON files
jsonfiles = ["python/verbs/2. romance base/json/"+x+" bases.json" for x in languages]
f = [open(x, 'w+', encoding="utf-8") for x in jsonfiles]

for n in range(len(tuple_languages)):
    f[n].write(json[n])

for x in range(len(f)):
    f[x].close()