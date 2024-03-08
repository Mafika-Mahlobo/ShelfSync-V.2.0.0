# ShelfSync

This is a web-based library management system built using Flask, HTML, CSS, Bootstrap, jQuery, and Python.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#Usage)


## Description
The Library Management System is designed to help librarians manage library resources, including books, patrons, borrowing records, and more. It provides an intuitive interface for adding, updating, and deleting books, managing patron information, and tracking borrowing history.

## Features
- Add, edit, and delete books from the library inventory
- Manage patron information and borrowing records
- Search for books by title, author, or ISBN
- Track borrowing history and due dates
- Admin dashboard for managing library resources

## Dependencies
- Flask: Web framework for Python
- Bootstrap: Front-end framework for building responsive web designs
- jQuery: JavaScript library for simplifying HTML DOM traversal and manipulation
- Other Python libraries as listed in requirements.txt

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Mafika-Mahlobo/ShelfSync-Portfolio-project.git
   ```
   Navigate to the project directory:
   ```bash
   cd ShelfSync
   ```
   Install the dependencies:
   ```bash
        pip install -r requirements.txt
   ```

## Usage
- Go to 'Tools' and run Create_database.sql file:
```bash
 mysql -u {your usernme} -p < Create_database.sql
```
- Go to app/config.py and insert your database credentials.
- Start the Flask server:
```bash
  python3 main.py
  ```
- Open your web browser and navigate to http://localhost:5000 to access the Library Management System.



