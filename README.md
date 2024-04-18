# ShelfSync

This is a web-based library management system built using Flask, HTML, CSS, Bootstrap, jQuery, and Python.

## Table of Contents
- [Description](#description)
- [Introduction](#Introduction)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#Usage)
- [Cotribution](#Contributions)


## Description
The Library Management System is designed to help librarians manage library resources, including books, patrons, borrowing records, and more. It provides an intuitive interface for adding, updating, and deleting books, managing patron information, and tracking borrowing history.

## Introduction
For more information about the project, visit [ShelfSync Website](http://Malfika.pythonanywhere.com), read the final project blog article [here](https://www.linkedin.com/posts/mafika-mahlobo-719a9a164_activity-7176371068792619008-qNjJ?utm_source=share&utm_medium=member_desktop), and connect with the author on [LinkedIn](https://www.linkedin.com/in/mafika-mahlobo-719a9a164/).

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
- default account credentials
- - username: admin@shelfsync.co.za
  - password: admin
- Go to app/config.py and insert your database credentials.
- Start the Flask server:
```bash
  python3 main.py
  ```
- Open your web browser and navigate to http://localhost:5000 to access the Library Management System.

## Contributions

- If you're interested in contributing to ShelfSync, follow these steps

1. **Fork** the repository by clicking the "Fork" button on the top right corner of this page.
2. **Clone** your forked repository to your local machine:
   ```bash
   git clone https://github.com/your-username/ShelfSync.git
   ```
3. Create a new branch
4. Make changes, stage commits and push.
5. Visit the original repository on GitHub and click "New pull request"
