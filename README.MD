# Tivents: Event Management Platform

## Overview

Tivents is a web-based event management platform that allows users to create, manage, and participate in events. Users can browse upcoming events, book tickets, and manage their events, including creating, editing, and deleting them. The platform also supports user authentication, password resets, and dark mode functionality.

This project is built with **Django** as the backend framework and uses plain **CSS** and **JavaScript** for styling and interactivity. It is designed to be user-friendly, lightweight, and easily deployable.

---

## Features

1. **Event Management**
   - Create events with details like name, category, date, time, location, description, and tickets.
   - Edit existing events (only the fields you update are saved).
   - Delete events.

2. **Ticket Management**
   - Add multiple ticket types to events, each with a name, price, and quantity.

3. **User Authentication**
   - Register, login, and logout functionality.
   - Password reset feature.

4. **Dark Mode**
   - Automatically detects the user's system theme preference.
   - Saves the dark mode preference using cookies.

5. **Responsive Design**
   - Optimized for mobile and desktop devices.

6. **Dynamic Tables**
   - Displays user events with the ability to delete or edit entries dynamically.

---

## Getting Started

### Prerequisites

1. Python 3.8 or higher.
2. Django 4.x or higher.
3. A PostgreSQL database (or SQLite for local development).
4. Git for version control.

---

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/paulmbui20/eventsBooking-django
   cd eventsBooking
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**
   - Rename the `env.example` file to `.env`.
   - Update `.env` with your database credentials and secret key.

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. Open the site in your browser at `http://127.0.0.1:8000`.

---

## Deploying to Production

### Steps for Deployment

1. **Set Up a Live Server**
   - Use a cloud service like **Heroku**, **AWS**, or **DigitalOcean**.
   - Install dependencies like Python, Gunicorn, and PostgreSQL.

2. **Install and Configure Gunicorn**
   ```bash
   pip install gunicorn
   ```

3. **Set Up Static Files**
   ```bash
   python manage.py collectstatic
   ```

4. **Update Environment Variables**
   - Add your `.env` variables to the production server environment.

5. **Run Gunicorn**
   ```bash
   gunicorn projectname.wsgi:application
   ```

6. **Set Up a Reverse Proxy (e.g., Nginx)**
   - Configure Nginx to serve your Django application and handle static files.

---

## Usage

1. **Events page**: View the latest events or browse categories.
2. **Register/Login**: Sign up or log in to manage your events.
3. **Manage Events**:
   - Add, edit, or delete events from the "My Events" section.
   - Attach tickets to events with specific details.
4. **Dark Mode**: Toggle dark mode in the navbar; the site will remember your choice.

---

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## Contact

For support or inquiries, please reach out to **paulmbui20@gmail.com**.