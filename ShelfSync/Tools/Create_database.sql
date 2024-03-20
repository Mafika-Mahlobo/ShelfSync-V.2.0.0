#create database
CREATE DATABASE ShelfSyncDB

#select database
USE ShelfSyncDB

#Create tables
CREATE TABLE employee (
	employee_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	position VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	phone VARCHAR(50) NOT NULL,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	is_admin INT,
);

CREATE TABLE patrons (
	patron_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	address VARCHAR(100) NOT NULL,
	email VARCHAR(50) NOT NULL,
	phone VARCHAR(50) NOT NULL,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	credit INT,
	debit INT
);


CREATE TABLE resources(
	isbn VARCHAR(50) PRIMARY KEY NOT NULL,
	UNIQUE KEY (ISBN),
	title VARCHAR(255),
	language VARCHAR(10) NOT NULL,
);



CREATE TABLE transactions(
	transaction_id INT(4) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
	isbn  VARCHAR(50) NOT NULL,
	employee_id INT NOT NULL,
	patron_id INT NOT NULL,
	transaction_type VARCHAR(12) NOT NULL,
	transaction_date DATE NOT NULL,
	due_date DATE NOT NULL,
	fee INT NOT NULL,
	FOREIGN KEY (isbn) REFERENCES resources(isbn),
	FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
	FOREIGN key (patron_id) REFERENCES patrons(patron_id)
);