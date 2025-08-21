CREATE DATABASE IF NOT EXISTS ShelfSyncV2;

USE ShelfSyncV2;

CREATE TABLE Libraries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    logo_url VARCHAR(500),
    coordinates VARCHAR(500),
    UNIQUE KEY (name, description(500))
);


CREATE TABLE Library_hours (
    library_id INT NOT NULL,
    days_of_week VARCHAR(100),
    open_time TIME,
    close_time TIME,
    PRIMARY KEY (library_id, days_of_week),
    FOREIGN KEY (library_id) REFERENCES Libraries(id)
);

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    library_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role INT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (library_id) REFERENCES Libraries(id),
    UNIQUE KEY (library_id, email)
);

CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    library_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) NOT NULL UNIQUE,
    category VARCHAR(100) NOT NULL,
    total_copies INT NOT NULL,
    available_copies INT NOT NULL
);

CREATE TABLE Book_authors (
    book_id INT NOT NULL,
    author VARCHAR(255) NOT NULL,
    PRIMARY KEY (book_id, author),
    FOREIGN KEY (book_id) REFERENCES Books(id)
);

CREATE TABLE Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    library_id INT NOT NULL,
    borrowed_at DATETIME NOT NULL,
    due_date DATETIME NOT NULL,
    returned_at DATETIME,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id), 
    FOREIGN KEY (book_id) REFERENCES Books(id),
    FOREIGN KEY (library_id) REFERENCES Libraries(id)
);

CREATE TABLE Fines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    loan_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT FALSE,
    issued_at DATETIME,
    paid_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(id), FOREIGN KEY (loan_id) REFERENCES Loans(id)
);

