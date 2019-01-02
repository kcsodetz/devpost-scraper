# Devpost Scraper 

A web scraper that, given a valid Devpost username, the number of projects that user has, hackathons attended, followers on Devpost, and hackathons won are displayed in the command line.

## Usage

To use, run:

```sh
$ python3 scraper.py [USER]

```

## Example

Since `nousername` does not exist, a 404 error will be thrown, ending the execution of the program.

```sh
$ python3 scraper.py no_username

[ERROR] 404 Error, cannot find username nousername

```

A succesful call of `scraper.py` would look like:

```sh
$ python3 scraper.py kcsodetz

Getting Devpost info from https://www.devpost.com/kcsodetz...

Projects:       4
Hackathons:     5
Followers:      1
Wins:           1

```
