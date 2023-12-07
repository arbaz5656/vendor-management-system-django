# Vendor Management System

This project is a Vendor Management System implemented using Django and Django REST Framework. It includes features for managing vendor profiles, tracking purchase orders, and calculating vendor performance metrics.

## Table of Contents

- [Introduction](#introduction)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Run the Test Suite](#run-the-test-suite)
- [Contributors](#contributors)
- [License](#license)
  
## Introduction
The Vendor Management System includes the following key features:

1. **Vendor Profile Management:**
   - Create, update, retrieve, and delete vendor profiles.
   - Store essential information such as name, contact details, address, and a unique vendor code.

2. **Purchase Order Tracking:**
   - Track purchase orders with details like PO number, vendor reference, order date, items, quantity, and status.
   - Create, update, retrieve, and delete purchase orders.

3. **Vendor Performance Evaluation:**
   - Calculate performance metrics for vendors, including on-time delivery rate, quality rating average, response time, and fulfillment rate.
   - Historical performance data for trend analysis.

## Setup Instructions

Follow these steps to set up and run the Vendor Management System locally.

1. **Clone the Repository**

```bash
   - git clone https://github.com/your-username/vendor-management-system.git
       cd vendor-management-system

2. **Install Dependencies**
```bash
   Make sure you have Python and pip installed. Then, install the project dependencies.

  - pip install -r requirements.txt

3. **Apply Migrations**
   Apply the database migrations to set up the initial database schema.

   - python manage.py makemigrations
   - python manage.py migrate

4. **Create a Superuser**
   Create a superuser account to access the Django admin interface.

  - python manage.py createsuperuser
    Follow the prompts to set up your superuser account.

5. **Run the Development Server**
   Start the Django development server.
  - python manage.py runserver

6. **Access the Home page** 
   Visit http://127.0.0.1:8000 in your web browser.

7. **Access the Admin Interface (Optional)**
   Visit http://127.0.0.1:8000/admin/ in your web browser and log in with the superuser credentials.

## API Endpoints

lakaoaaxuix


























## API Endpoints

If you're open to contributions, explain how others can contribute to your project.

## Run the Test Suite

Include information about the license of your project.

## Contributors
aisjuqsjqnwonowqn

## License

