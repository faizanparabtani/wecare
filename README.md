# WeCare - Healthcare Providers and Seekers Platform

## Overview

WeCare is a web application built using Django that connects healthcare providers with individuals seeking medical assistance. The platform allows users to register as healthcare providers or patients, facilitating easy access to medical services.

## Features

- **User Authentication:** Secure login and registration system.
- **Role-Based Access:** Users can register as healthcare providers or seekers.
- **Profile Management:** Providers can manage their profiles, including specialties and availability.
- **Appointment Booking:** Seekers can schedule appointments with healthcare providers.
- **Search and Filters:** Find providers based on specialization, location, and availability.
- **Reviews and Ratings:** Seekers can leave feedback for providers.

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL / SQLite
- **Authentication:** Django Authentication System

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.10
- Django
- Virtualenv (optional but recommended)

### Steps

```sh
# Clone the repository
git clone https://github.com/faizanparabtani/wecare.git
cd wecare

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Open the application in your browser:
# http://127.0.0.1:8000/
