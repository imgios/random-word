# 🎲 Random Word API

Random-word is a basic API that provides a word generated randomly with letters, numbers and special chars. I did it to learn Python and Flask.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to execute the API, you need:
- [Python 3.7](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [venv](https://docs.python.org/3/library/venv.html)

### Installing

First of all, clone the repository:
```
$ git clone https://github.com/imgios/random-word.git
$ cd random-word
```
Then, create a new virtualenv and activate it:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
Now that you have a virtual environment created and activated, you can go ahead and install dependencies:
```
$ pip3 install -r requirements.txt
```
That's it, now you're ready to start the API:
```
$ python3 app.py
```

<p align="center">
  <img width="492" height="376" src="https://github.com/imgios/random-word/blob/master/.github/installing.png?raw=true">
  <br/><sub><i>API startup.</i></sub>
</p>

## Deployment

Add additional notes about how to deploy this on a live system.

| Endpoint | Method | Parameters | Description | Example
| --- | :---: | --- | --- | --- |
| `/api/word` | `GET` | `length` indicates how much long the word should be in a range between 8 and 128. | Return a JSON object with two attributes: `status` and `content`. If `status` equal `OK`, then `content` will contains the word generated. Otherwise, status will be `ERROR` and `content` will contains information about the error. | `/api/word?length=8` |

## Built With

* [Python 3.7](https://www.python.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* Love 🎈
