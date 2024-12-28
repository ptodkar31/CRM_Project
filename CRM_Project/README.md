CRM Project
A Customer Relationship Management (CRM) system built with Django, featuring:

JWT-based authentication.
CRUD APIs for managing customers, products, and orders.
Redis caching for frequently queried data.
Celery for background task handling.


Setup Instructions
Prerequisites
Python 3.11+
PostgreSQL
Redis


API Documentation
Endpoints
Authentication

Obtain token: POST /api/token/
Refresh token: POST /api/token/refresh/
Customers

List/Create: GET/POST /api/customers/
Retrieve/Update/Delete: GET/PUT/DELETE /api/customers/<id>/