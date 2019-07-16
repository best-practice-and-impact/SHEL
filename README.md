# Stakeholder Engagement Log

The project has been setup.

## Tasks
- [x] admin user - Jack
- [x] bootstrap - Josh
- [x] TABLE for the data
- [x] Heroku deployment
- [ ] Advanced table functions, filters, DELETE JS
- [x] email verification, password reset - AE, JS
- [x] calendar for SHEL form JH
- [ ] error handling
- [ ] Analytics
- [ ] Finish webform  AE, JS
- [x] Team updates form homepage JH, JS
- [ ] TESTING!!!! Everyone [Unit testing](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers)
- [ ] Download data!

## First- webform
* date - datetime
* stakeholder name - string
* role - drop down
* organisation - drop down
* discussion points - string
* bpi member - dictionaries
* Stance on Quality - drop down
* bpi contact

1. template.
2. route
3. model (database)
4. flaskform


## To delete databases
db.reflect()
db.drop_all()


## Created admin user
username = admin
password = 123 or admin

Jack - Checking I am working on the correct branch

Jack - Checked that the changes run on another computer

## Notes while working:

- The index page will not load if the Post table is empty. This is because of the negative indexing used to return the last two items from the table. To get this to work I have manually added two posts to the table in the python terminal.

## Email verification setup:
To enable email verification the following environmental variables need to be created in the terminal and exported:
 - $ export MAIL_SERVER=smtp.googlemail.com
 - $ export MAIL_PORT=587
 - $ export MAIL_USE_TLS=1
 - $ export MAIL_USERNAME=<your-gmail-username> (this can be any gmail email address)
 - $ export MAIL_PASSWORD=<your-gmail-password> (this is the password for the account)

(As the Password is then an environmental variable it will not be written in the config file.)
