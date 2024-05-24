# Django-assignment# Vendor Management System

A Vendor Management System built using Django and Django REST Framework. This system handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Features

1. **Vendor Profile Management**
   - Create, retrieve, update, and delete vendor profiles.
   - Vendor profiles include essential information and performance metrics.

2. **Purchase Order Tracking**
   - Create, retrieve, update, and delete purchase orders.
   - Purchase orders include details such as items ordered, quantity, status, and dates.

3. **Vendor Performance Evaluation**
   - Calculate and retrieve performance metrics for vendors.
   - Metrics include on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/vendor_management.git
    cd vendor_management
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser to access the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://127.0.0.1:8000/`.

## Additional Information

- **Efficient Calculation:** The logic for calculating metrics is optimized to handle large datasets without significant performance issues.
- **Data Integrity:** Includes checks to handle scenarios like missing data points or division by zero in calculations.
- **Real-time Updates:** Uses Django signals to trigger metric updates in real-time when related PO data is modified.

## License

This project is licensed under the MIT License.
