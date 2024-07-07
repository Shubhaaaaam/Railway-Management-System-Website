# Railway-Management-System-Website

This project is a web application for booking railway tickets, checking PNR status, and checking in for trips. Let's break down its key components and functionality:

1. Setup and Configuration
Imports: The project uses Flask for the web framework, Flask-Login for user session management, and MySQL for database operations.
Database Connection: Connects to a MySQL database named "railway" with specified credentials.
Flask App Initialization: Initializes the Flask application and sets a secret key for session management.


3. Routes and Functions
Home Route (/)
Purpose: Displays the home page with options to book tickets, check PNR, or check-in.
Methods: GET and POST


Functionality: Depending on the button clicked, it redirects to the appropriate page.
Login Route (/login)
Purpose: Handles user login.
Methods: GET and POST
Functionality: Validates user credentials against the info table in the database. On successful login, it redirects to the booking page.
Book Tickets Route (/booktickets)
Purpose: Searches for trains between specified departure and destination.
Methods: GET and POST
Functionality: Queries the trains table for available trains and displays them.
Trains Route (/trains)
Purpose: Displays available trains for booking.
Methods: GET and POST
Functionality: Shows the booking form pre-filled with selected train details.
Book It Route (/bookit)
Purpose: Handles the actual booking of tickets.
Methods: GET and POST
Functionality:
Generates a random PNR.
Inserts passenger details into the passenger table.
Updates seat availability in the trains table.
Displays the ticket details.
PNR Route (/pnr)
Purpose: Checks PNR status.
Methods: GET and POST
Functionality: Verifies Aadhar number for the given PNR and displays ticket details.
Check-in Route (/checkin)
Purpose: Handles check-in process.
Methods: GET and POST
Functionality: Verifies contact number for the given PNR and displays the check-in confirmation page.
Check Route (/check)
Purpose: Confirms or cancels the check-in.
Methods: GET and POST
Functionality: Updates the checkin status of the passenger based on the action taken.
Check-in Done Route (/checkindone)
Purpose: Displays the check-in done page.
Methods: GET and POST
Functionality: Simply renders the check-in done template.


Templates
home.html: Home page with options to book, check PNR, or check-in.
login.html: Login form.
book.html: Search for trains form.
trains.html: Displays available trains.
bookit.html: Booking form.
showticket.html: Displays booked ticket details.
pnr.html: Form to check PNR status.
accessible.html: Displays PNR details.
accessdenied.html: Access denied page.
checkin.html: Check-in form.
confirmation.html: Check-in confirmation page.
checkindone.html: Check-in done page.


Summary
Database Operations: The application interacts with the MySQL database to fetch train details, book tickets, update seat availability, check PNR status, and manage check-in.
User Authentication: Basic user login is implemented.
Ticket Booking: Users can book tickets by selecting a train and providing passenger details.
PNR Status: Users can check the status of their bookings using their PNR and Aadhar number.
Check-in: Users can check-in for their journey by verifying their contact number.

Saving the files:
Create a new folder on your computer and name it something like "Railway Ticket Management System".
Save Files
Place all the relevant files related to the Railway Ticket Management System inside this folder and all the web pages in a folder named templates.

Setting up MySQL Database:
Install MySQL if you haven't already. You can download it from the official website: https://dev.mysql.com/downloads/installer/
Launch MySQL and open a connection.
Create a Database
Define the structure of your database by creating tables.
