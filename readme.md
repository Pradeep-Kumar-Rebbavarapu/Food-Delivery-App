# Food Delivery App

This is a Django-based food delivery web application.

## Running the App Locally

### Using Docker

1. Pull the Docker image:
    ```bash
    docker pull pradeepkumar11519/food-delivery-app:latest
    ```

2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 pradeepkumar11519/food-delivery-app:latest
    ```

3. Navigate to [localhost:8000](http://localhost:8000) in your web browser.

### Using GitHub

1. Clone the repository:
    ```bash
    git clone https://github.com/Pradeep-Kumar-Rebbavarapu/Food-Delivery-App
    ```

2. Set up a virtual environment:
    - On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    - On Linux:
        ```bash
        virtualenv venv
        source venv/bin/activate
        ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

## Deployment Process

The server is deployed on [render.com](https://render.com).

Visit the deployed site [here](https://food-delivery-app-2aew.onrender.com/).

## Documentation

You can find the documentation on [Docs](https://docs.google.com/document/d/1e-aci8T2bA035bsGjLjrUBU-KFk0NopubWWptAHwuJI/edit?usp=sharing).

## API calls

You can find the description of api calls on [Description](https://food-delivery-app-2aew.onrender.com/redoc/).

## The django admin panel

A New Verison of the Admin Panel on [Description](https://food-delivery-app-2aew.onrender.com/admin/).

## Credential For The Admin Panel

Access the development / local admin panel with the following credentials:
- **Username**: admin
- **Password**: admin

Access the deployed / production admin panel [here](https://food-delivery-app-2aew.onrender.com/admin/) with the following credentials:
- **Username**: user123
- **Password**: Gangsta@user123