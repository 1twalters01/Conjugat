# Conjugat
A WIP Restful Django/Rust application that will test the user's conjugation abilities. This is done by rendering forms with a set verb and tense on them. Users will have to enter the correct answers on the form and submit them.

![Conjugat main page](https://user-images.githubusercontent.com/115738254/230995339-83261924-0be6-4c96-8a15-e51868631ba3.png)


## What is complete
The following functionality is complete:
1. WebScraping - Everything except running everything
[Link](https://github.com/1twalters01/Conjugat/tree/main/Back-end/python/verbs)
* Webscrapped Reverso for all subjects, auxiliaries, and tenses for 5 languages. Got the desired 2000 bases for the bases, and all of the conjugations
* Got part way through scapping the sentence structure but recieved a 429 error
* Got a 429 Too many reque
2. Accounts - Everything
[Back-end](https://github.com/1twalters01/Conjugat/tree/main/Back-end/Conjugat-django/account)
[Front-end](https://github.com/1twalters01/Conjugat/tree/main/Front-end/Conjugat-react/src/pages/account)
* DjangoRest Knox is used for tokens
* Remember me functionality
* Optional email input on registration that sends verification email if filled in
* Functionality has been built for session authentication if I were to switch to it.
* 2FA and password reset built
3. Newsletter - Back-end is finished, Front-end is not
[Back-end](https://github.com/1twalters01/Conjugat/tree/main/Back-end/Conjugat-django/newsletter)
[Front-end](https://github.com/1twalters01/Conjugat/tree/main/Front-end/Conjugat-react/src/pages/newsletter)
* Finished other than styling the view when you are logged in
* Connects to mailchimp
* Uses webhooks to stay synchronised
4. Settings - Everything except the reset functionality
[Back-end](https://github.com/1twalters01/Conjugat/tree/main/Back-end/Conjugat-django/settings)
[Front-end](https://github.com/1twalters01/Conjugat/tree/main/Front-end/Conjugat-react/src/pages/settings)
* Change email, password and username for the user
* Close the account
* See/edit your subscription status
* Add/remove two factor authentication to your account
5. Subscriptions - Back-end is finished, Front-end is not
[Back-end](https://github.com/1twalters01/Conjugat/tree/main/Back-end/Conjugat-django/subscription)
[Front-end](https://github.com/1twalters01/Conjugat/tree/main/Front-end/Conjugat-react/src/pages/subscriptions)
* Stripe, paypal and coinbase-commerce subscription integration
* Webhooks for all three
* Free trial period
* Encryption for the subscription and client IDs
6. Test functionality - Initial back-end is finished, Front-end for the test is as well
[Back-end](https://github.com/1twalters01/Conjugat/tree/main/Back-end/Conjugat-django/verbs)
[Front-end](https://github.com/1twalters01/Conjugat/tree/main/Front-end/Conjugat-react/src/pages/verbs)
* Redis and Cassandra has been integrated
* Initial database structure has been designed

## Scope
I am starting with 5 languages - English, French, Italian, Portuguese, and Spanish in MVP 1. 

This will be made in the style of a SAAS business (the payment processors will be kept in demo mode). It will be worked on throughout my career as a developer. Storing the users' time series data can get computationally expensive as the data grows both with the number of users and the amount of information sent in. With time, more functionality than just verbs will be added.

Leads will be warmed up via a weekly newsletter. I want to improve my writing abilities, and this project is perfect for that. Mailchimp is used to send the emails, though I may make my own functionality later on.

Payments won't be taken, but a real subscription payment system was made to keep it in the style of a SAAS product. It currently takes Stripe, Paypal and Coinbase, though more options can be added if desired.


## How it works
By serving new words/tenses periodically in a way that will adapt to the user, their active memory of words in the chosen language will increase. Verbs and tenses will be released in order of what is the most common for speakers of the language in question. This way, they will learn words most likely to appear first. Many other applications do not do things in order of what is most likely to be seen, hence this app's creation.


## Raison d'etre
I love languages. I believe that learning multiple will pay dividends as the world continues to become more globalised. As such, I have started learning Spanish. Like many language learners who begin their journey, I was bombarded with Duolingo adverts. I downloaded their app and noticed that the experience was "interesting" to say the least.

![Duolingo sentence - edited](https://user-images.githubusercontent.com/115738254/230331794-e09a29e3-c6e7-4211-93da-ff307189621b.png)

Upon looking into things, it seemed that my suspicions of Duolingo's inefficiencies weren't just a hunch. Take their CRO, for example. [Bob Meese, Duolingo’s 42-year-old chief revenue officer, has been studying Duolingo Spanish for more than six months. In response to the question, “¿Hablas español?” he froze [SIC], then said [SIC], “Could you repeat that?”](https://www.forbes.com/sites/susanadams/2019/07/16/game-of-tongues-how-duolingo-built-a-700-million-business-with-its-addictive-language-learning-app/?sh=28079cb03463)
I don't want these results for myself, so I decided to start making my own language learning app.


## CERF specification
The highest level someone can be in language learning is C2 on the CEFR standard. It is commonly said that the amount of words you need to know doubles to get to the next level, starting at 500 words for A1. Others say that the number is 10,000+. Therefore, 10,000 - 16,000 words are needed. I read that verbs make up around 15% of all English words. I thus need between 1520 and 2432 verbs. I am choosing 2000 verbs. I am assuming that the romance languages I am using also use this many due to being unable to find data for the percentage of verbs in them.


## Initial model
New words will be added or removed from the user's vocabulary pool as decided by a Tensorflow model. The variance between when different users will learn new words will come from:
1. How the system learns from the initial uses to judge the user's level - we don't want them to go through everything.
A similar optional "training" mode should be activated if:
    - the user has a long break from the website.
    - The user makes more than a certain level of mistakes
    - The user gets a higher percentage of answers correct than a certain threshold amount.

2. How the system reacts to mistakes - repeatedly mistaken conjugations should repeat themselves more often.
    - Some allowance may be made for accents depending on the frequency.

3. If the user chooses to flag a word, add it to a list that repeats more frequently.


## Stack
### Overview
Back-end - Python, Django (REST Framework), BS4, Rust, PostgreSQL, Redis, Cassandra

Front-end (Website) - TypeScript, React, React-redux, Redux persist, SCSS

Front-end (Android) - Kotlin

Main external APIs - Stripe, Paypal, Coinbase commerce, MailChimp

### Back-end
#### Django
I want to use a relational database for the most part so there would be no problem using Django's inbuilt ORM. Things like Djongo can be questionable sometimes, so using Flask would make more sense. I also knew I wanted to add many different features, and Django's automatically built structure is helpful here. This is why I chose it over Flask.

Speed shouldn't be too much of an issue, as I will build much of the site in Rust. FastAPI thus won't be needed. PyO3 and Maturin will be used to interface the Rust code with the Python code. See an example of me doing this [here.](https://github.com/1twalters01/Challenges/tree/master/Project%20Euler/Problem%201%20-%20Multiples%20of%203%20or%205/Answers/PyO3) Fast API is also extremely lightweight, having similar drawbacks to Flask. DjangoREST framework will be used to expose the endpoints.

#### Rust
PyO3 and Maturin are used to integrate them with Python. This lets me have the flexibility of Python with the speed of a lower-level language like Rust. I will use it for computationally heavy functions. The plan is to prototype everything in Python and then remake said functions in Rust. It has a robust typing system which helps reduce mistakes.

#### PostgreSQL
I chose PostgreSQL over MySQL as it supports more data types such as timezone-aware timestamps. You can also add your own data types. I will need to store audio files of people speaking, hence the need for this.

#### Cassandra
The idea to use Cassandra and Redis was taken from a [netflix article](https://netflixtechblog.com/scaling-time-series-data-storage-part-i-ec2b6d44ba39)
I will use Cassandra to store time series data (the test results) as it is good at handling this. It has fast read times but slower write times which is alright as the application will be much heavier on the read side. Lots of data will be read (on loading the home page to view graphs, on seeing past tests, from the back-end when generating tests, etc.)

#### Redis
Writing will still be done a lot, (whenever the user completes a test), and I intend to use Redis to store the day's write operations. Since it is a cache, it cannot save too much data so I will store past data in Cassandra. I will either use a chron-job to schedule backups to Cassandra daily, or asynchronously write to both Redis and Cassandra.

### Front-end
#### React (TypeScript) + Redux
React was chosen because of its avant-garde, component-based feel. TypeScript was used as the typing system will detect many bugs that can get hidden when using regular JS. Many small reusable components mean that the look and feel of the site will be much more continuous throughout the entire application.

Redux will be used as the state management system over context due to the dev tools. I needed a state management system due to prop drilling while making the app.

#### SCSS
SCSS was chosen over CSS as it makes code more concise. I didn't use any of the many CSS in JS libraries as I didn't want to have a bloated code base - many styles are reusable between components in this app (e.g. for the form fields), and these libraries wouldn't let me do that.

### Design
I used the AI [Midjourney](https://www.midjourney.com/home/) to create the [initial look](https://user-images.githubusercontent.com/115738254/230511571-fe83ab75-4c28-4d2e-8eae-2ce2e0b10c52.png) of the landing page website. I then created a design based off of that in Figma[Image landing page Figma]. I used this as a guide to create other pages.

I then recreated them in HTML and CSS. I created versions of everything for: [Screens](https://user-images.githubusercontent.com/115738254/230515508-f97e7c83-9e33-48f2-ac1a-e178749ec27e.png), [Desktops](https://user-images.githubusercontent.com/115738254/230515649-ba309d1d-d2a3-4e77-a5e9-73b084cd357f.png), Laptops, [Tablets](https://user-images.githubusercontent.com/115738254/230515697-c0286c6a-ee3e-4121-b33d-b777dd6ced4f.png)
, and [Phones](https://user-images.githubusercontent.com/115738254/230515718-89b25980-3052-4110-a3b5-04c1721a9299.png).


## Todo
All functionality is finished except for:
* Making expired subscriptions automatically turn off
* The tensorflow functionality to choose verbs
* The reset account progress functionality
* Finishing the scss
* Graphs on the home page using chart.js
* Refactoring code in rust

More details are in the Todo file.
Once this is done I will get real api keys rather than test one and launch. 
