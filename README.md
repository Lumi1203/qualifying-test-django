Qualifying Test Django Application

Live Application URL:

https://qualifying-test-django.onrender.com

https://qualifying-test-django.onrender.com

https://qualifying-test-django.onrender.com


Project Overview

The Qualifying Test Application is a Django-based web application designed to manage exam questions, 
examiners, and candidate assessments. The system supports examiner role-based permissions, question bank management, 
user authentication, profile management, and deployment on Render with PostgreSQL.



Key Features

User authentication (register, login, logout)
Custom user roles (Examiner & Superuser)
Examiner-specific Question Bank
Role-based access control
PostgreSQL database (Render-hosted)
Static file handling with Whitenoise
Media storage with Cloudinary
Production-ready deployment on Render


!!!Only users with the “Examiner” role can access the Question Bank!!!


Examiner
Can view all questions in the Question Bank
Can create, edit, and delete only the questions they added
Can see the name of the examiner who added each question



Creating an Examiner Account

To create an Examiner account:
Navigate to the registration page
Select Examiner as the role
Enter any 6-digit number in the Examiner ID field
Example: 123456
Complete registration and log in
Once logged in as an examiner, you will have access to the Question Bank.




Hosting & Infrastructure

Platform: Render Web Service
Database: Render PostgreSQL
Static Files: Whitenoise
Media Storage: Cloudinary