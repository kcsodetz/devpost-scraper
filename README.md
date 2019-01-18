# Devpost User Info Scraper 

A web scraper that, given a valid Devpost username, displays the number of projects, hackathons, followers, and hackathons won on the command line.

## Usage

BeautifulSoup4 and requests are used as the main driver for scraping data. To install, simply run:

```sh
$ pip install -r requirements.txt

```


To use, run:

```sh
$ python3 dev-scraper.py [USER]

```

## Example

Since `noUsername` does not exist, a 404 error will be thrown, ending the execution of the program.

```sh
$ python3 -dev scraper.py noUsername

Getting Devpost info from https://www.devpost.com/noUsername...

[ERROR] 404 Error, cannot find username noUsername

```

A succesful call of `dev-scraper.py` would look like:

```sh
$ python3 dev-scraper.py kcsodetz

Getting Devpost info from https://www.devpost.com/kcsodetz...

Projects:       4
Hackathons:     5
Followers:      1
Wins:           1

```
