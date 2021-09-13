# Bluecoding Challenge

Simple URL shortener API.

## Setup

    pip install -r requirements.txt
    flask db upgrade  # Will create app.sqlite db in project root

## Usage
For the examples I'm using HTTPie command which is similar to cURL.

### Get Short URL

    http post localhost:5000 url="http://foo.com/"

    {
        "short-url": "a"
    }

### Redirect to Full URL

    # Will redirect to "http://foo.com/" with a 302 status code
    http get localhost:5000/a
