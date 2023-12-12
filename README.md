# search-_api

# Flask Search API

A simple Flask web application that provides a search API for fetching comments from a YouTube video.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Introduction

This Flask application exposes a REST API for searching comments from a YouTube video. It supports various search criteria, including author name, date range, like and reply count range, and search text within the comment.

## Features

- Search comments by author name.
- Search comments by date range.
- Search comments by like and reply count range.
- Search comments by a search string in the text field.

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd flask-search-api

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
The app will be accessible at http://127.0.0.1:5000/.

Usage
To use the search API, make HTTP GET requests to the /search endpoint with the appropriate query parameters. See the API Endpoints section for examples.

API Endpoints
Search Comments
Endpoint: /search
Method: GET
Parameters:
search_author: Search comments by author name.
at_from and at_to: Search comments within a date range.
like_from and like_to: Search comments within a like count range.
reply_from and reply_to: Search comments within a reply count range.
search_text: Search comments by a search string in the text field.
Example:

bash
Copy code
curl -X GET "http://127.0.0.1:5000/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&search_text=economic"
