#create database
#CREATE DATABASE ShelfSyncDB

#select database
USE ShelfSyncDB

#Books table
/*CREATE TABLE Books (
	resource_id int AUTO_INCREMENT PRIMARY KEY,
	tile VARCHAR(50) NOT NULL,
	author VARCHAR(50) NOT NULL,
	isbn VARCHAR(15) NOT NULL,
	publication_year DATE NOT NULL,
	edition VARCHAR(50) NOT NULL,
	genre VARCHAR(50)
);*/

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

CREATE TABLE journals (
	
);




SHOW TABLES;