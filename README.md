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


## Web scraping
