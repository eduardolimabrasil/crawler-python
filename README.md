# crawler-python

This is a crawler of IBovespa, Nasdaq and the current dollar value in relation to the real.

This application was developed with these tools:
* Python 3.7
* Docker
* SQLAlchemy as an ORM to manage the SQLite database
* Cron to Schedule tasks
* Beautifulsoup4
* Pandas

## How to use

The application runs on Linux Docker or in your local machine.

### Local Machine

If you want to run in your machine, you need to install the requirements with this command
`pip install -r requirements.txt`

Has 4 arguments to run, use these commands for it:
1. `python Main ibovespa` - Fist Crawler
1. `python Main nasdaq` - Second Crawler
1. `python Main usd_brl` - Third Crawler
1. `python Main` - Without argument, needs the 2 and 3 executed first. 
    This execution make a output file inside `data` folder with Nasdaq data converted to Real (BRL)
 
### Docker

The execution with docker contains a **Cron** associated. 
This means that it will run 4 runs every 2 minutes simultaneously, one for each argument.

To execute the application with docker, use this commands:
```
> docker build . -t crawlers
> docker run crawlers
```
 
## Database
 
In the first run, the database file for SQLite called `crawler.db` will be created.

## Settings

There is a settings file (`settings.py`) with all the project's configuration.

If you want to change the schedule used when running the docker, use the `crontab` file.
