import datetime

tech = {
    'imgs': [
        'css.png',
        'django.png',
        'express.png',
        'flask.png',
        'git.png',
        'html.png',
        'jquery.png',
        'js.png',
        'mongo.png',
        'mysql.png',
        'net_icon.png',
        'nodejs.png',
        'python.png',
        'reaact.png',
    ]
}

about_me = {
    'content': '<p>A bit about me, I grew up in Cashmere WA, the youngest of 3 children. When I was a child my family moved over to Indonesia to work as teachers at an international school there. Living there for 3 years layed some fundamentals of who I am today. For instance, my willingness to travel and explore the world as well as my intercultural understanding. After the 3 years in Indonesia my family moved back to the US.</p><p>Following High School I joined the US Navy and served my country for 5 years as a Logistic specialist. Doing 3 deployments in the persian gulf from 2008 to 2013. During my time in the Navy I reconnected with a friend from my childhood in Indonesia and after my time in the service I persued her and moved over to Indonesia for a second time. We got married shortly after and now have two amazing boys.</p><p>While in Indonesia for the second time I went to UPH (Universitas Pelita Harapan) and earned my teaching degree. After my schooling was over I taught 4th grade at SPH (Sekolah Pelita Harapan) for 3 years. Interesting fact: this was the same internation school my parents taught at 17 years earlier. While teaching has its own benefits I found that I was always learning new code to try and create different applications to assist me in whatever I was doing, whether that be for my job or for recreational purposes.</p><p>I eventually came to the conclusion that I wanted to have a career change and pursue software development as a full time job. This lead me to the Coding Dojo bootcamp and then to another bootcamp at University of Washington.</p>'
}

edu = {
    1: {
        'title': 'Coding Dojo',
        'start_date': datetime.datetime(2020, 7, 20),
        'end_date': datetime.datetime(2020, 10, 30),
        'present': False,
        'content': '''
        <h1>My Story</h1><p>I had a great time going to school at coding dojo. I started going to coding dojo after getting my degree as a teacher and working for a couple of years as a 4th grade teacher. While I was teaching I was writing my own small scripts and programs to help out in my teaching career. After a while I realized I enjoyed the coding that I was doing more than the teaching. Ergo my attendance at Coding Dojo. </p>
        <p>Even though I was going into Coding Dojo with some years of self taugh study behind me, Coding Dojo was tough. I was putting in about 65-70 hours a week and learning a lot. But because of the hard work I "black" belted in all three stacks that the program offered (python, MERN, C#). It was three months of intense work that was most enjoyable.</p>
        <p>I would recomend Coding Dojo to anybody who is serious about learning to code in a short amount of time. It really shows you an overview of the different types of technologies that are out there. And is a great way to jump start your way into a new career!</p>
        ''',
        'link': 'https://www.codingdojo.com/'
    },
    2: {
        'title': 'University of Washington',
        'start_date': datetime.datetime(2020, 12, 7),
        'end_date': datetime.datetime(2021, 3, 5),
        'present': False,
        'content': '''
            I attended University of Washington's Bootcamp after I already went to Coding
        ''',
        'link': 'http://www.washington.edu/',
    },
    3: {
        'title': 'Universitas Pelita Harapan',
        'start_date': datetime.datetime(2014, 7, 21),
        'end_date': datetime.datetime(2017, 5, 26),
        'present': False,
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum quaerat voluptates suscipit nisi vitae officiis, eaque hic veniam eligendi. Provident maiores beatae accusamus asperiores, sequi dolores dolorem repudiandae! Eos, facere!',
        'link': 'https://www.uph.edu/',
    },
    4: {
        'title': 'Corban University',
        'start_date': datetime.datetime(2014, 7, 21),
        'end_date': datetime.datetime(2017, 5, 26),
        'present': False,
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum quaerat voluptates suscipit nisi vitae officiis, eaque hic veniam eligendi. Provident maiores beatae accusamus asperiores, sequi dolores dolorem repudiandae! Eos, facere!',
        'link': 'https://www.corban.edu/',
    },
}

jobs = {
    1: {
        'title': 'Coding Dojo',
        'start_date': datetime.datetime(2020, 11, 1),
        'end_date': datetime.datetime(2021, 8, 1),
        'present': True,
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum quaerat voluptates suscipit nisi vitae officiis, eaque hic veniam eligendi. Provident maiores beatae accusamus asperiores, sequi dolores dolorem repudiandae! Eos, facere!',
        'link': 'https://www.codingdojo.com/',
    },
    2: {
        'title': 'Sekolah Peleta Harapan',
        'start_date': datetime.datetime(2017, 7, 21),
        'end_date': datetime.datetime(2020, 5, 26),
        'present': False,
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum quaerat voluptates suscipit nisi vitae officiis, eaque hic veniam eligendi. Provident maiores beatae accusamus asperiores, sequi dolores dolorem repudiandae! Eos, facere!',
        'link': 'https://sph.edu/',
    },
    3: {
        'title': 'US Navy',
        'start_date': datetime.datetime(2008, 12, 10),
        'end_date': datetime.datetime(2013, 12, 10),
        'present': False,
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum quaerat voluptates suscipit nisi vitae officiis, eaque hic veniam eligendi. Provident maiores beatae accusamus asperiores, sequi dolores dolorem repudiandae! Eos, facere!',
        'link': 'https://www.navy.mil/',
    },
}

projects = {
    1: {
        'title': 'Meets',
        'type': 'School Project',
        'content': 'It is hard to keep track of what everyone is doing and sometimes you would like to know with out having to be a burden to them. That is where "meets" comes into play. Meets is an application that allows you connect with the people you know while at the same time giving you your very own personal assistant (an AI we developed) that let you know the status of your connections (how they are doing, what was the last thing they did, etc). Your AI will pull the data from your connections to help you get the information you need to know, when you need to know it.',
        'technologies': [
            'Materializecss',
            'bcrypt',
            'MySQL',
            'Express',
            'Express-handlebars',
            'Nodejs',
            'JavaScript',
            'HTML',
            'CSS',
            'Dialog Flow',
        ],
        'imgs': [
            'img/meets/img1.png',
            'img/meets/img2.png',
            'img/meets/img3.png',
            'img/meets/img4.png',
            'img/meets/img5.png',
            'img/meets/img6.png',
        ],
        'github_link': 'https://github.com/Tbone8098/uw-Project-2',
        'site_link': 'https://uw-meets.herokuapp.com/'
    },
    2: {
        'title': 'Tazkr',
        'type': 'School Project',
        'content': 'Trello style project manager that is designed to help keep track of what tasks in a project are active and what tasks are completed, as well as where the tasks are in the process. It utilized Jquery UI in order to add visual effects when clicking, dragging and dropping an item into different columns. Tazker was developed on the Django framework in order to keep tasks modular and easy to manage. Designed with AJAX and JavaScript to perform quick and easy communications between the front-end and back-end. Implements a login and registration system that utilizes Bcrypt and displays client-side validations. Deployed on an AWS server',
        'technologies': [
            'Python',
            'Django',
            'Jquery UI',
            'AJAX',
            'Bcrypt',
            'JavaScript'
        ],
        'imgs': [
            'img/tazkr/img1.png',
            'img/tazkr/img2.png',
            'img/tazkr/img3.png',
            'img/tazkr/img4.png',
            'img/tazkr/img5.png',
        ],
        'github_link': 'https://github.com/Tbone8098/CodingDojo-Tazkr',
        'site_link': ''
    },
    3: {
        'title': 'Mood Tunes',
        'type': 'School Project',
        'content': 'Purely a front-end application that will take a user’s mood as well as the length of time the user has available and create a youtube based playlist of songs. Used Skeleton css framework CDN to organize the information on the HTML page. Utilized google sheets API, YouTube API, and unsplash API. Implemented localStorage to store and retrieve data pertinent for the application. Implements a login and registration system that utilizes Bcrypt and displays client-side validations. Deployed using github pages.',
        'technologies': [
            'HTML',
            'JavaScript',
            'CSS',
            'Skeleton CSS Framework',
            'Jquery',
        ],
        'imgs': [
            'img/mood_tunes/img1.png',
            'img/mood_tunes/img2.png',
            'img/mood_tunes/img3.png',
            'img/mood_tunes/img4.png',
            'img/mood_tunes/img5.png',
        ],
        'github_link': 'https://github.com/Tbone8098/uw-jagged-little-pill',
        'site_link': 'https://tbone8098.github.io/uw-jagged-little-pill/'
    },
    4: {
        'title': 'Kalxon Kitchen',
        'type': 'Free Lanced Job',
        'content': 'Developed to keep track of the orders that were being processed in a food court in Jakarta Indonesia. Used Skeleton css framework CDN to organize the information on the HTML page. Used the Python language with Django as a framework. Keeping things orderly and modular for future implementation. Utilized bcrypt when comparing and storing user passwords in a hash form. Implemented a login and registration page.',
        'technologies': [
            'JavaScript',
            'HTML',
            'CSS',
            'Skeleton CSS Framework',
            'Django',
            'Bcrypt',
            'Python',
        ],
        'imgs': [
            'img/klaxon_kitchen/img1.png',
            'img/klaxon_kitchen/img2.png',
            'img/klaxon_kitchen/img3.png',
            'img/klaxon_kitchen/img4.png',
            'img/klaxon_kitchen/img5.png',
        ],
        'github_link': 'https://github.com/Tbone8098/klaxon-kitchen-django',
        'site_link': ''
    },
}
