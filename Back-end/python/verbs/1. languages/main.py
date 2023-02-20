import pickle

#1. Enter the languages to be considered
languages = ['Spanish', 'Portuguese', 'Italian', 'French', 'English']


#2. Turn them into a dictionary
dictionary = {}
for index, item in enumerate(languages):
    dictionary.update({item:index+1})


#3. Save the dictionary as a pickle file so it can be read by other python files
with open('python/verbs/1. languages/languages.pkl', 'wb') as f:
    pickle.dump(dictionary, f)


#4. Read the dictionary to ensure it is correct
myfile = 'python/verbs/1. languages/languages.pkl'
with (open(myfile, "rb")) as openfile:
    while True:
        try:
            objects = pickle.load(openfile)
        except EOFError:
            break
print(objects)


#5. Create a json file that can be read by django
objects = tuple(objects.items())
json = ''''''
for i in range(len(objects)):
    json = json+'''
{
  "model": "verbs.language",
  "pk": '''+str(objects[i][1])+''',
  "fields": {
    "language": "'''+str(objects[i][0])+'''"
  }
},'''

json = json.rstrip(',')
json = '''['''+json+'''
]'''


#6. write to json file
jsonfile = "python/verbs/1. languages/languages.json"
f = open(jsonfile, 'w+', encoding="utf-8") 
f.write(json)
f.close()