#create database
#CREATE DATABASE ShelfSyncDB;

#select database
USE ShelfSyncDB;

#create tables
/*CREATE TABLE resource (*/
/*	resource_id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
	title VARCHAR(50) NOT NULL,
	publisher VARCHAR(50),
	publication_year DATE
);

CREATE TABLE Books (
	isbn VARCHAR(50) PRIMARY KEY,
	resource_id INT NOT NULL,
	UNIQUE KEY (resource_id),
	author VARCHAR(50) NOT NULL,
	edition VARCHAR(50) NOT NULL,
	genre VARCHAR(20) NOT NULL,
	FOREIGN KEY (resource_id) REFERENCES resource(resource_id)
);

CREATE TABLE journals (
	journal_id INT AUTO_INCREMENT PRIMARY KEY,
	resource_id INT NOT NULL,
	UNIQUE KEY (resource_id),
	issue INT NOT NULL,
	volume INT NOT NULL,
	FOREIGN KEY (resource_id) REFERENCES resource(resource_id)
);

CREATE TABLE media (
	file_id INT AUTO_INCREMENT PRIMARY KEY,
	resource_id INT NOT NULL,
	UNIQUE KEY (resource_id),
	type VARCHAR(20) NOT NULL,
	FOREIGN KEY (resource_id) REFERENCES resource(resource_id)
);


CREATE TABLE employee (
	employee_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	position VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	phone VARCHAR(50) NOT NULL,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL

);

CREATE TABLE patrons (
	patron_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	address VARCHAR(100) NOT NULL,
	email VARCHAR(50) NOT NULL,
	phone VARCHAR(50) NOT NULL,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL
);


CREATE TABLE transactions (
	transaction_id INT AUTO_INCREMENT PRIMARY KEY,
	transaction_type VARCHAR(50) NOT NULL,
	transaction_date DATE NOT NULL,
	due_date DATE NOT NULL,
	patron_id INT NOT NULL,
	resource_id INT NOT NULL,
	employee_id INT NOT NULL,
	FOREIGN KEY (patron_id) REFERENCES patrons(patron_id),
	FOREIGN KEY (resource_id) REFERENCES resource(resource_id),
	FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);


/*ALTER TABLE employee add is_admin VARCHAR(5) NOT NULL DEFAULT 'No';*/

#test resulta
#INSERT INTO employee (name, position, email, phone, username, password)
#VALUES ('Admin', 'Library manager', 'admin.joe@shelfsync.co.za', '1223553354', 'Admin1', 'Admin123');

CREATE TABLE resources(
	isbn VARCHAR(50) PRIMARY KEY NOT NULL,
	UNIQUE KEY (ISBN),
	title VARCHAR(50) NOT NULL,
	authors VARCHAR(50) NOT NULL,
	publisher VARCHAR(50) NOT NULL,
	published_date DATE NOT NULL,
	description VARCHAR(200) NOT NULL,
	categories VARCHAR(50) NOT NULL,
	language VARCHAR(10) NOT NULL,
	url VARCHAR(100)
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


ALTER TABLE patrons
ADD credit INT,
ADD debit INT;

SHOW TABLES;