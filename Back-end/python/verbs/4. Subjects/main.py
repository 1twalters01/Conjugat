from bs4 import BeautifulSoup
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


#4. Get a list for the Subjects
def keepSubjects(x):
    x = re.sub('<i class="verbtxt.*?</i>', '', x)
    x = re.sub('<i class="a.*?</i>', '', x)
    x = re.sub('<i class="p.*?</i>', '', x)
    x = re.sub('<i.*?>', '', x)
    x = re.sub('</i.*?>', '', x).rstrip()
    return x

def unique(seq):
    seen = set()
    for item in seq:
        if item not in seen:
            seen.add( item )
            yield item

subjects = [[]]*len(tuple_languages)
for n in range(len(languages)):
    for k in range(len(urls[n])):
        print(urls[n][k], k)
        soup = BeautifulSoup(requests.get(urls[n][k]).text, 'lxml')
        results = soup.find_all('div', {'mobile-title': True})
        for i in range(len(results)):
            subjectholder = []
            itags = re.findall(r'<li>(.+?)</li>', str(results[i]))
            for j in range(len(itags)):
                onlySubjects = keepSubjects(itags[j])
                subjectholder.append(onlySubjects)
            subjects[n] = subjects[n] + subjectholder
        subjects[n] = list(unique(subjects[n]))
    
#5. Turn the subjects into a tuple
pk = 1
Tuple_Subjects = [()]*len(subjects)
for n in range(len(languages)):
    for index, subject in enumerate(subjects[n]):
        Tuple_Subjects[n] = Tuple_Subjects[n] + ((subject,pk, languages[tuple_languages[n]]),)
        pk +=1


#6. Save the tuple in a pickle file as separate languages
for index, item in enumerate(languages):
    with open('python/verbs/4. Subjects/tuples/'+item+' Subjects.pkl', 'wb') as f:
        pickle.dump(Tuple_Subjects[index], f)


#7. Read the tuple to ensure it is correct
Tuple_Subjects = [()]*len(languages)
for index, item in enumerate(languages):
    myfile = 'python/verbs/4. Subjects/tuples/'+item+' Subjects.pkl'
    with (open(myfile, "rb")) as openfile:
        while True:
            try:
                Tuple_Subjects[index] = pickle.load(openfile)
            except EOFError:
                break
print(Tuple_Subjects)


#8. Create the JSON file
json = ['''''']*len(tuple_languages)
for n in range(len(tuple_languages)):
    no_of_bases = len(Tuple_Subjects[n])
    
    for i in range(no_of_bases):
        json[n] = json[n]+'''
    {
    "model": "verbs.romancesubject",
    "pk": '''+str(Tuple_Subjects[n][i][1])+''',
    "fields": {
        "language": "'''+str(Tuple_Subjects[n][i][2])+'''",
        "subject": "'''+Tuple_Subjects[n][i][0]+'''"
    }
    },'''

    json[n] = json[n].rstrip(',')
    json[n] = '''['''+json[n]+'''
    ]'''


#9. Save the JSON file
jsonfiles = ["python/verbs/4. Subjects/json/"+x+" Subjects.json" for x in languages]
f = [open(x, 'w+', encoding="utf-8") for x in jsonfiles]

for n in range(len(tuple_languages)):
    f[n].write(json[n])

for x in range(len(f)):
    f[x].close()