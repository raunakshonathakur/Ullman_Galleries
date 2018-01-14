# Ullman Galleries 
Ullman Galleries is a management tool for application entries. It provides an easy way to accept applications. Our main purpose for the system is to accept applications from artists that want to show their work in a Berea College Gallery Showing.
  

## Getting Started
The intial step of setting up a development environment is choosing the appropriate tool to complete the application setup.
This application requires you to have a linux environment specifically an Ubuntu.
However, if you are working out of a windows operating system during development we would recommend you use [cloud9](https://c9.io/)

### Cloud9 Setup Guide (Optional)
You can find the instruction to setting up c9 at https://docs.c9.io/docs/create-a-workspace. You should use python as the template.

### Starting up the Application

After you have accessed your environment, we have built some scripts into the system that will get the application up and running for you. 

1. ```python setup.py install```
2. ```. venv/bin/activate```
3. ```python scripts/ConfigureApp.py```
4. ```python app.py```s

>***Note***: If you working inside of your own linux environment you may need to change the port and host information inside of ```app.py`` the default is setup up for working inside of cloud9

## Built With

* [Flask](http://flask.pocoo.org/docs/0.11/)  - Python Based Web Framework Used
* [Jinja2](http://jinja.pocoo.org/docs/dev/) - HTML Templating Language for Python
* [Peewee](http://docs.peewee-orm.com/en/latest/index.html) - A small, expressive ORM used for database communications
* [SQLite](https://sqlite.org/) - SQL database engine

## Deploying on a Server
### Dependencies
1. [Apache2](https://help.ubuntu.com/lts/serverguide/httpd.html) - `sudo apt-get install apache2`
2. [Python-Pip](https://pip.pypa.io/en/stable/) - `sudo apt-get install python-pip`
3. [Virtualenv](https://virtualenv.pypa.io/en/stable) - `sudo apt install virtualenv`
4. [WSGI](http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/) - `sudo apt-get install libapache2-mod-wsgi`
5. [Flask](http://flask.pocoo.org/docs/0.11/) - `sudo pip install Flask`

### Additional Server Setup:
These tools will require additional steps by your server admin in order to get the application running. 

1. [WSGI & Apache2 Sites-Enabled](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#installing-mod-wsgi)
2. [Logrotate](https://docs.google.com/document/d/1xtV__kmA8p0uTg_4TtbzYYLtqX5eZGckotQSmAvuCVA/edit?usp=sharing)
3. Shibboleth (Optional)

## Contributing
Contributions of all kinds are welcome, not only in the form of code. We openly
embrace that the systems were built with the intention of teaching Berea College 
students how to develop software. Therefore, if you believe that you could help 
us with our structure or coding standards feel free to contribute in that manner,
or by helping other users or our students within the issue queue. 

Additionally if you think something is bad about our documentation the way it is,
please feel free to help us make it better. We are new to the world of Open Source
after all. 

We do ask that you review the [CONTRIBUTING.md](CONTRIBUTING.md) before submitting
any pull request. We look forward to adding you to our community.

## Versioning
The versioning scheme that we use is [SemVer](http://semver.org/).

## Authors
1. [Cody Myers](http://github.com/myersCody)


## License

## Acknowledgments
* [Berea College](https://www.berea.edu/) for providing us the opportunity to have a student software developers group.
* [Our Community](CONTRIBUTORS.md) 
