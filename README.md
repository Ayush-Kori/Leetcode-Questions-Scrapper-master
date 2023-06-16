# Search Engine with TF-IDF Implementation
This project is a search engine that allows users to search for questions based on keywords. It utilizes the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm to rank and retrieve relevant documents. The backend of the project is developed using Flask, a Python web framework.

## Installation
To run the search engine locally, follow these steps:

* Install Python: Make sure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

* Install Flask: Open a terminal or command prompt and run the following command to install Flask:

pip install flask
* Install Flask-WTF: Flask-WTF is used for form handling in Flask applications. Install it by running the following command:

pip install flask-wtf
Download the project: Clone or download the project from the repository.

* Run the application: Navigate to the project directory in the terminal or command prompt and execute the following command:


python app.py
* Access the application: Open a web browser and enter the following URL:

http://localhost:5000

## Usage
* Enter Keywords: On the search page of the application, enter the keywords related to the question you want to search for.

* Submit the Query: Click on the "Search" button to submit your query.

* View Results: The search engine will retrieve the top 10 relevant links based on the TF-IDF algorithm and display them on the results page.

* Click on a Result: You can click on any of the links to navigate to the corresponding webpage and view the full content.

## Project Structure
The project has the following structure:

app.py: This file contains the Flask application and handles the routing and logic for the search engine.
templates/: This directory contains the HTML templates used to render the webpages.
index.html: The main search page template.
results.html: The template to display the search results.
static/: This directory contains the static files, such as CSS stylesheets and JavaScript files.
Dependencies
The project relies on the following dependencies:

Flask: A micro web framework for Python.
Flask-WTF: An extension for Flask that integrates WTForms, a flexible form handling library.
You can find the full list of dependencies in the requirements.txt file included with the project.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please submit an issue or create a pull request on the project repository.

## License
This project is licensed under the MIT License. Feel free to modify and use the code for your own purposes.