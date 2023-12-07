
# Vendor Management System

## Table of contents

[Introduction](https://github.com/arbaz5656/vendor-management-system-django#introduction)

[Installation](https://github.com/arbaz5656/vendor-management-system-django#installation)

[API References](https://github.com/arbaz5656/vendor-management-system-django#api-reference)

[Screenshots](https://github.com/arbaz5656/vendor-management-system-django#screenshots)

[Assignment-By](https://github.com/arbaz5656/vendor-management-system-django#assignement-by)

[Support](https://github.com/arbaz5656/vendor-management-system-django#support)

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


## Installation

```bash
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

```


## API Reference
   Test API Endpoints
Vendor List: http://127.0.0.1:8000/api/vendors/
Purchase Order List: http://127.0.0.1:8000/api/purchase_orders/

#### Vendor Profile Management:
```http
● POST /api/vendors/: Create a new vendor.
● GET /api/vendors/: List all vendors.
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendors/{vendor_id}/: Delete a vendor.```


#### Purchase Order Tracking:

```http
● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by
  vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.```


#### Historical Performance:

```http
 ● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
   metrics.
```

## Deployment

To deploy this project on git

```bash
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


```


## Screenshots

__Simple HTML page for Vendor List__\

![Vendor List](Vendor_list.png)

__Vendor List API Endpoint__

![Vendor List API endpoint](vendor_list_endpoint.png)

__Purchase Order API Endpoint__

![Purchase Order API endpoint](purchaseorder_endpoint.png)

__Historical Performance API Endpoint__

![Historical Performance API endpoint](Historical_Performance_endpoint.png)

## ASSIGNEMENT BY

This project is assisgned by the following company:

- [FATMUG, Delhi, India](https://www.linkedin.com/company/fatmug-designs/)



## FAQ

#### 1) I am getting the problem in database migration?

First of all check all your databases if the db file has been created or not.
Still if the problem pursuits, go to migration files and delete all the migrations files without __init__.py.
Remigrate the database and it should be solved now.

__How to check the database__

 Run the following commands in bash.
- python manage.py dbshell
- .table

___

#### 2) Api endpoints are not visible on cmd, What should I do?

Api endpoints can only be checked by the tools like __POSTMAN__ or you can check it using __DJANGO_ORM__.

For using Django-ORM, You have to register for the admin in project using
 - python manage.py createsuperuser

Then you have to create the admin pages for all the API endpoints models in admin.py file.

After successfully completing all this steps, You can now check your endpoints without any error.

___
#### 3) I am unable to load the localhost server on web?

If your server is not running by following IP: http://127.0.0.1:8000/vendors/ or http://localhost:8000/vendors/, It might happen beacause of unproper url paths. 

Recheck your urls.py in app if it correctly given or not.

___

#### 4) I have successfully installed djangorestframework but still it is giving error for it is not defined, what should i do?

It might happen almost because of only one mistake you do, Which is not installing the appname or library name in __INSTALLED APP__ setting present in settings.py file of main project.

___

```http
- If you have more questions you can drop a mail on :
```
bhushanch45@gmail.com
___
## Support

For support, email bhushanch45@gmail.com

