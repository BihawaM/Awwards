# Awwards

## Description
this is a web app where it allows a user to post a project he/she has created and get it reviewed by his/her peers.

## Author
### [BihawaM](https://github.com/BihawaM)



## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/BihawaM/Awwards.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd Awwards
```

##### 2. Create a virtual environment
 Install `Virtualenv`

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```gallery```
   ```prettier
   # create database gallery
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python manage.py makemigrations gallery
```


then run the command below;

 ```bash
 python manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    python3 manage.py runserver

### Running Tests
>To run tests;

    python manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
As a user, I would like to:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects
* View projects overall score
* View my profile page


## Bugs
There are no known bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2020 BihawaM

## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
> Send me an [email](bihawam271@gmail.com) to collaborate on the project.

