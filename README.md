<img>

# VolunTutoring

Ace Tuition is a tuition agency that aims to bring tutees and tutors together. 
Looking to find a tutor to ride through your academic woes? No problem, Ace Tuition Services has tutors to cater to your subject needs.
Want to give tuition a try? Just sign up with us and we will get you started in not time! We offer competitive hourly rates for capable tutors.

This projects seeks to emulate a tuition agency website, where 
1. Potential students are able to register as a member. 
2. potential tutors can sign up as a tutor
3. The tuition agency administrator can perform CRUD of the students and tutor records
 
## UX

### User stories

* As a student, I am looking tuition services on various subjects
* As someone interested in giving tuition, I am looking to start off somewhere
* As an administrator, I am looking to manage the student and tutor profiles database

### Wireframes and Diagrams

* [Wireframes](https://#)
* [ER Diagrams](https://#)
 
## Features

This site is primarily split into 3 parts: 
* Request a Tutor
* Tutor Registration
* Browse Tutors

### Request a Tutor

This page allows potential students to sign up with the agency. The potential student needs to provide the particulars and other details about the tuition services he or she requires

### Tutor Registration

This page caters to potential tutors, who will input their particulars and upload a photograph and certificate
 
### Browse tutor

Visitors can browse tutors and look at the tutor profile, so as to make a more well informed decision on the tutor they are going to engage. 


## Features Left to Implement
- TBC
- TBC...

## Technologies Used

1. [HTML](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
2. [CSS](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
3. [JavaScript](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. 
4. [Flask](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
5. [Python 3.8](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. 
6. [MongoDB](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. 
7. [Heroku](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
8. [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.



## Testing

Manual testing was done on all links and Pages. 

Test cases are as follows:
1. 
2. 
3. 

Request

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

Deployment
a. Setting up MySQL (ClearDB) with Heroku
Installing ClearDB in Git Bash using heroku addons:create cleardb:ignite
Datatables in the database were created using the create_datatables.py file written by the developer
Datasets were imported automatically from the csv file using import_datasets.py file written by the developer
b. Heroku Deployment
Sign up for an account at Heroku.
Download Heroku CLI at Heroku website.
Install the dowloaded Heroku CLI from Step 2.
Open up Git Bash terminal. Cd to the location that you have your project in. Then, in the Git Bash Terminal, login to Heroku by typing heroku login. A login page will be popped up to allow you to login to Heroku.
Open up another Git Bash terminal. Create a new app using heroku create <app_name>.
In Git Bash, check whether the new remotes has been successfully added using git remote -v.
In Git Bash, install gunicorn with the command git remote -v.
Create a file called Procfile. Add web gunicorn app:app and save it.
Create the requirements.txt file with pip3 freeze --local > requirements.txt.
In Git Bash, commit and push the project to GitHub and Heroku with the following:
git add .
git commit -m "<Commit Message>"
git push heroku master
In Heroku, set up your key and value pair needed for the project. For this project, the database url, MySQL username, database, host and password has been configured under the Settings Tab.
To open up the app hosted on Heroku, click on the "Open App" button at the very top page of the Heroku dashboard.
b. To run this web application on your local PC
Instructions Note: This web application was run on a Windows PC. The following command might be slightly different if run on a Mac PC.

Go to Cereal 101 github repository.

Click on the 'Clone or Download' button and then click 'Download ZIP' and extract the files to a location of your choice on your laptop / desktop. Else, you can clone the project by running the following command on your terminal: git clone https://github.com/<username>/<repository>

Create a virtual environment using the following command: python -m venv venv

Activate the virtual environment created using the following command: On Windows: venv\Scripts\activate

Install all the packages needed using the following command: pip install -r requirements.txt

Set the enviroment variables needed to run this web application. First, right click on My Computer. Then right click on Properties. On the left hand side of the menu bar, click on Advanced system settings. Under the System Variables section, click on the New button. In the pop up dialog box, key in the Variable Name and Variable Value field. The environment variables needed to be setup would be the database name, database host, database password and database username. Note: For the variable name, you are free to choose a variable name of your choice:

An example of the enviroment variables key values pair would be as follow: a. MYSQL_HOST(variable name) will be: us-cdbr-iron-east-02.cleardb.net (variable value) b. MYSQL_USER(variable name) will be: B80f8d428xxxxx(variable value) c. MYSQL_PASSWORD(variable name) will be: F48exxxx(variable value) d. MYSQL_DB will(variable name) be: heroku_58632fb6debxxxx(variable value)

Run the application using the following command: python app.py

To see the web application in action, go the the following link: http://127.0.0.1:8080


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- Idea was conceived from viewing the website of Nanyang Academics. Linke [here](https://www.nanyangacademics.com/)

### Media
- The photos used in this site were obtained from [Unplash]()

### Acknowledgements

- I received inspiration for this project from X