Vendor Management System


Table of contents

Introduction

Roadmap

Features

API References

Tech Stack

Installation

Deployment

Screenshots

Author/Company

FAQ

Support

Introduction
The Vendor Management System, developed using Django, is a web application designed for streamlined vendor relationship management.

It encompasses functionalities for managing vendor profiles, tracking purchase orders, and evaluating vendor performance.

Users can create, update, and delete vendor profiles, monitor purchase orders, and assess vendor performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.



Roadmap
Start and Plan: Understand the project scope and set up the basic structure.

Vendor Setup: Create a system to manage vendor information and test it.

Purchase Order Management: Develop purchase order forms and check their functionality.

Performance Evaluation: Add a scoring system for vendors and calculate scores dynamically.

Historical Tracking: Include a history feature to track vendor performance over time.

Testing Phase: Conduct thorough testing, find and fix bugs.

Deployment: Put the system online for use.

Maintenance: Keep an eye on the system, fix issues, and assist users.


Features
User/Admin can add or remove vendors
Vendors can see the list of different members
Admin can give the perfect calculations for performance
Easy to use
API endpoints can be checked using Django ORM
No need of any tools is needed for API endpoints checking.
API Reference
Vendor Profile Management:
  POST /api/vendors/: Create a new vendor.
  GET /api/vendors/: List all vendors.
  GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
  PUT /api/vendors/{vendor_id}/: Update a vendor's details.
  DELETE /api/vendors/{vendor_id}/: Delete a vendor.
Purchase Order Tracking:
  POST /api/purchase_orders/: Create a purchase order.
  GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
  GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
  PUT /api/purchase_orders/{po_id}/: Update a purchase order.
  DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
Historical Performance:
  GET /api/vendors/{vendor_id}/performance
Tech Stack
Stack: Python, Django, dbsqlite3

Server: localhost:8000

Installation
python -m venv venv

source venv/Scripts/activate

pip install django

pip install djangorestframework

pip install -r requirements.txt

python manage.py makemigrations 

python manage.py migrate

python manage.py createsuperuser 

python manage.py runserver

http://localhost:8000/vendors/  --for vendor list

http://localhost:8000/admin  --for admin
Deployment
To deploy this project on git

 ($ pip freeze > requirements.txt)  ### It will freeze all the requirements in one txt file ###

 ($ git init)   ### It will initialize the folder as a local Git repository ###

 ($ git status)   ### This command to check if there are any changes to your Django code that need to be pushed to git ###

 ($ git add -A)   ### The -A flag is for all. It is used for adding all the commits to a repository ###

 ($ git commit -m "initial commit") ### It is for passing the message to repository ###

  ### Create A New Github Repository ###
  - Click the ‘+’ dropdown at the top right corner of your GitHub dashboard and click on the ‘New Repository’ option.
  - Type the name of the Repository. It is best practice to give it the same name as that of your Django project.
  - Give a description of the project if you wish to do so.
  - Choose if it is going to be a Private or Public directory.
  - The next step ‘Initialize your project with:’ is optional, skip it if you wish to.
  ### Click the ‘Create Reposity’ button ###

 ($ git remote add origin https://github.com/bhush-n/vendor_management.git)  ### It will add a new remote origin ###

 ($ git branch -M main)  ### It is used to shift to the main branch from master ###

 ($ git push -u origin main)  ### It will push your code the remote repository which you have added recently ###

