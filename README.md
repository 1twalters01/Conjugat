# Conjugat
This is a WIP language learning application meant to showcase my full stack programming - django for the back end, react for the website front end, kotlin for the android front end, and postgresql as the main database. Cassandra and Redis will be used to store time series data due to limitations of postgres.

## Note
This project was only just uploaded to github. I can provide the old versions on request. See the no DjangoREST Framework branch for something that visibly - the main branch doesn't have react added yet and I haven't converted all of the views into a form that works with the DjangoREST framework yet.

## Detail
The application tests the user's conjugation abilities by rendering forms that have a pre-determined verb and tense. The user will have to enter the correct answers for all of the subjects for the verb-tense combination. By serving new words/tenses periodically in a way that will adapt to the user, it will increase their active memory of words in that language.

The order the verbs and tenses will be generated in will be based off of the most common verbs and tenses that speakers of the language in question use, so that they will learn words most likely to appear first unlike many other applications. I think I will use Tensorflow to do this. The difference between users would come from:

1. How the system learns from the initial use to quickly get the user to the level they are at - we don't want them to have to go through literally every combination.
    - A similar optional "training" mode should be activated if the user has a long break from the website.
    - The user makes more than a certain level of mistakes
    - The user gets a higher percentage of answers correct than a certain threshold amount.

2. How the system reacts to mistakes - repeat mistakes should repeat themselves more often.
    - Some allowance may be made on accents depending on the frequency.

3. If the user chooses to flag a word to add it to a list that repeats more frequently.

The webapp will be fully fleshed out to give a more real feel including: login functionality, payment with 3 different payment processors (on live mode as this is just a practice project) for the stereotypical freemium model, a newsletter sign up, and a fully responsive design. More features will be added as they are thought of / suggested.

## What is finished
Everything except for the design, the test functionality, and the algorithm for choosing tenses is finished for the version that does not use DRF. Things that are finished are as follows:

### Language database creation - conjugat/verbs/models
Proper normalisation is critical when working with big databases. It can take your website from being unusable (25s+), even when the page is not accessing the ORM to working fast (<1s). Good indexing is also important. Proper management of primary keys had to be used in the web scraping to prevent data from going wrong. This is a read only database meaning I may consider using direct sql commands rather than the ORM depending on performance as the Django ORM is known to be quite slow for big databases.

### Web scraping - python/verbs and json directories
The highest level one can be in language learning is C2 on the CEFR standard. It is said commonly that the amount of words you need to know doubles to get to the next level, starting at 500 words for A1. Others say that the number is 10,000+. This means that 10,000 - 16,000 words are needed. Verbs make up [15.2% of English words](https://www.google.com/search?rlz=1C1ONGR_enGB1030GB1030&sxsrf=AJOqlzVCms3En5pgorVT4ZJ9L8YuYRqbQA:1675176090117&q=What+percentage+of+words+are+verbs+in+english&sa=X&ved=2ahUKEwjimKaehfL8AhUILMAKHRinCq4Q1QJ6BAgzEAE&biw=1137&bih=730&dpr=0.9). I thus need between 1520 and 2432 verbs. I am choosing 2000 verbs. I am assuming that the romance languages in question also use this many due to being unable to find data for the percentage of verbs in them. I got the list of the top 2000 most common words from reverso from links such as [this](https://conjugator.reverso.net/index-french-1-250.html).

Web scraping can be found in the python/verbs directory. I used pickle files to share data between the different sections of the web scraping due to the speed. I saved the seperate sections as either dictionaries or tuples so that the primary key - value pairs would be preserved. Each bit of code created a JSON file of a form that can be loaded by Django into the relevant databases. The tenses, subjects and auxiliaries were scraped for every single verb rather than just a few as I didn't know if there would be any irregularities for any of the verbs in a foreign language. Any duplicates were removed.

The main database was split up into the order one would learn them. Some verbs had an irregular amount of tenses so I used a check to see if the tense was found. If not then it ran a for loop until the tense was found. I could have done a search starting from the list index that had failed rather than a for loop as the fail case but didn't as it ran relatively fast. JSON was created and then loaded into the database.

### Account functionality - conjugat/account with 2FA being in conjugat/settings/totp
This is a fully fleshed out account system with: login and log out functionality that works for both username and email, password reset, registration with email verification and optional totp.

There is also google, twitter and facebook authentication using their APIs as an optional second choice for loging in which was added through use of social_django. I did not add apple authentication as you need to pay £99/year to access their API and use the functionality. A fake SSL is created for https requests using pyOpenSSL. This was required to get google, facebook and twitter authentication to work in testing.

Django-two-factor-auth forced me to use their login view and not my own html template so I created my own functionality. I had some trouble with integrating it with the login system due to not wanting to store a password in a session variable or use get instead of post but came up with a work around that saves the username to sessions, checks to see if totp is enabled, and then returns the relevant form that looked and worked really well.

Email verification makes use of the reset password token generator class based view that comes with django contrib auth, and creates the hash by using the user's pk, the timestamp and their active state. It thus gets invalidated once used once.

### Subscriptions - conjugat/subscription and conjugat/settings directories.
I am using paypal, stripe and coinbase for payment options due to their popularity. I made the design choice to have their success pages seperate here and NOT due to inability - I put their success pages all together in conjugat/settings in the premium view/template so that users could access this in a singular place.

We are moving towards a software as a service (Saas) world, and if you can't beat them join them. I thus used the subscriptions with a free trial for stripe and paypal. Coinbase commerce doesn't allow for subscriptions so functionality will have to be added to check if the date for subscription has expired. It also doesn't allow a free trial option so I put a nominal fee of 1p rather than just activate the subscription ~~because common psychology says that getting someone to input their detail will make them more likely to pay with real money next time~~ so that it is fair between all three payment providers. I will likely use a chronjob though may check whenever they go on the website (once per day) as it may have the potential of being slow if lots of users were to be added.

Requests is used with paypal to properly post to their api to access the user's subscription status. This lets them make changes. The stripe cli client is used for working in test mode on stripe.

Webhooks are used to ensure that my database is correct. Webhook urls had to be created, along with correct processing of the payloads sent. A json  with the success code 200 is to be sent back in the event of a success. No response is sent if it doesn't work as that is the signal for an internal error, although I may change this to an error code. An email is sent if the subscription trial is ending.

### General settings - conjugat/settings
This has common functionality - changing email, username and password, closing account, viewing premium subscription status, theme change and reseting progress on the account.

The qr code works well in light mode, however it didn't work at all in dark mode with the google authenticator app. A white border around the qr code was required for it to be scannable by the google authenticator app when in dark mode.

The theme change was made using a context processor. I could have used a session variable instead, but thought that users would rather their theme settings be associated to their account rather than their pc. I will use the session variable option for when users are not logged in.

### Newsletter
This simply gets the user to enter their email (or use the one that is tied to their account) and sends it to mailchimp so that they can receive marketing emails. I was going to use webhooks to sync a copy to the app but then decided not to as mailchimp host everything and my site doesn't need to store or check any data for this, unlike with the payment processors where I had to make sure everything was synchronised.

I connected to their API and send the data that gets input into my website over.


## To do
Finish designing the PC version
Finish designing the mobile site
Add sesion variable for the theme when not logged in.
Add functionality to unsubscribe user if subscription date has expired.
Create form functionality, along with verification for if it is correct or not
Algorithm to determine what verbs/tenses should be tested.
