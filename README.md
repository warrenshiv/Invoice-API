# Invoice Management System

This Invoice Management System is built using Django and Django Rest Framework (DRF). It provides a RESTful API to manage invoices and their corresponding details.

## Features

- **CRUD Operations**: Create, read, update, and delete invoices and invoice details.
- **RESTful API**: A clean REST interface for managing invoices.
- **Nested Resources**: Manage invoice details directly within invoice requests.

## Technologies

- Python 3.10.12
- Django 4.2.7
- Django Rest Framework 3.14.0

## Setup

Follow these steps to get your development environment set up:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/warrenshiv/Invoice-API.git
    cd Invoice-API
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

    The API will be available at [http://localhost:8000/invoices/](http://localhost:8000/invoices/).

## Usage

Here are some examples of how you can interact with the API:

- **Create an Invoice**:

    ```bash
    curl -X POST http://localhost:8000/invoices/ -H "Content-Type: application/json" -d '{
        "date": "2024-04-17",
        "customer_name": "Jane Doe",
        "details": [
            {
                "description": "Service",
                "quantity": 5,
                "unit_price": 50.00,
                "price": 250.00
            }
        ]
    }'
    ```

- **Retrieve an Invoice**:

    ```bash
    curl -X GET http://localhost:8000/invoices/1/  # Assuming '1' is the ID of the invoice
    ```

- **Update an Invoice**:

    ```bash
    curl -X PUT http://localhost:8000/invoices/1/ -H "Content-Type: application/json" -d '{
        "date": "2024-04-18",
        "customer_name": "John Doe Updated",
        "details": [
            {
                "id": 1,  # Assuming '1' is the ID of the existing invoice detail
                "description": "Updated Service",
                "quantity": 10,
                "unit_price": 55.00,
                "price": 550.00
            }
        ]
    }'
    ```

- **Delete an Invoice**:

    ```bash
    curl -X DELETE http://localhost:8000/invoices/1/
    ```

- **List all Invoices**:

    ```bash
    curl -X GET http://localhost:8000/invoices/
    ```

## Testing

To run the tests, use the following command:

```bash
python manage.py test
