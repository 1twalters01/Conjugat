# Conjugat
This is a WIP language learning application meant to precisely test django coding fundamentals and their supersets - vanilla html, css and js (or compiled from scss and ts) with postgres as the main database. Cassandra and Redis will be used to store time series data due to limitations of postgres.

The application tests the user's conjugation abilities by rendering forms that have a pre-determined verb and tense. The user will have to enter the correct answers for all of the subjects for the verb-tense combination. By serving new words/tenses periodically in a way that will adapt to the user, it will increase their active memory of words in that language.

The order the verbs and tenses will be generated in will be based off of the most common verbs and tenses that speakers of the language in question use, so that they will learn words most likely to appear first unlike many other applications. The difference between users would come from:

1. How the system learns from the initial use to quickly get the user to the level they are at - we don't want them to have to go through literally every combination.
    - A similar optional "training" mode should be activated if the user has a long break from the website.
    - The user makes more than a certain level of mistakes
    - The user gets a higher percentage of answers correct than a certain threshold amount.

2. How the system reacts to mistakes - repeat mistakes should repeat themselves more often.
    - Some allowance may be made on accents depending on the frequency.

3. If the user chooses to flag a word to add it to a list that repeats more frequently.

The webapp will be fully fleshed out to give a more real feel including: login functionality, payment with 3 different payment processors (on live mode as this is just a practice project) for the stereotypical freemium model, a newsletter sign up, and a fully responsive design. More features will be added as they are thought of / suggested.

## What is finished
Everything except for the design, the test functionality and the algorithm for choosing tenses is finished. Things that are finished are as follows:

### Language database creation - conjugat/verbs/models
Proper normalisation is critical when working with big databases. It can take your website from being unusable (25s+), even when the page is not accessing the ORM to working fast (<1s). Good indexing is also important. Proper management of primary keys had to be used in the web scraping to prevent data from going wrong. This is a read only database meaning I may consider using direct sql commands rather than the ORM depending on performance as the Django ORM is known to be quite slow for big databases.

### Web scraping - python/verbs and json directories
The highest level one can be in language learning is C2 on the CEFR standard. It is said commonly that the amount of words you need to know doubles to get to the next level, starting at 500 words for A1. Others say that the number is 10,000+. This means that 10,000 - 16,000 words are needed. Verbs make up [15.2% of English words](https://www.google.com/search?rlz=1C1ONGR_enGB1030GB1030&sxsrf=AJOqlzVCms3En5pgorVT4ZJ9L8YuYRqbQA:1675176090117&q=What+percentage+of+words+are+verbs+in+english&sa=X&ved=2ahUKEwjimKaehfL8AhUILMAKHRinCq4Q1QJ6BAgzEAE&biw=1137&bih=730&dpr=0.9). I thus need between 1520 and 2432 verbs. I am choosing 2000 verbs. I am assuming that the romance languages in question also use this many due to being unable to find data for the percentage of verbs in them. I got the list of the top 2000 most common words from reverso from links such as [this](https://conjugator.reverso.net/index-french-1-250.html).

Web scraping can be found in the python/verbs directory. I used pickle files to share data between the different sections of the web scraping due to the speed. I saved the seperate sections as either dictionaries or tuples so that the primary key - value pairs would be preserved. Each bit of code created a JSON file of a form that can be loaded by Django into the relevant databases. The tenses, subjects and auxiliaries were scraped for every single verb rather than just a few as I didn't know if there would be any irregularities for any of the verbs in a foreign language. Any duplicates were removed.

The main database was split up into the order one would learn them. Some verbs had an irregular amount of tenses so I used a check to see if the tense was found. If not then it ran a for loop until the tense was found. I could have done a search starting from the list index that had failed rather than a for loop as the fail case but didn't as it ran relatively fast. JSON was created and then loaded into the database.

### Account functionality - conjugat/account with 2FA being in conjugat/settings/totp
This is a fully fleshed out account system with: login and log out functionality that works for both username and email, password reset, registration with email verification and optional totp.#

Django-two-factor-auth forced me to use their login view and not my own html template so I created my own functionality. I had some trouble with integrating it with the login system due to not wanting to store a password in a session variable or get but came up with a work around that looked and worked really well.

There is also google, twitter and facebook authentication as an optional second choice for loging in which was added through use of social_django. I did not add apple authentication as you need to pay £99/year to use the functionality.

### Subscriptions
### General settings
A white border around the qr code was required for it to be scannable by the google authenticator app.
### Newsletter

## To do

## Web scraping

##