# Online-Library-System

A simple library system

## Prerequisites

- Python 3.10
- Django 5.1.1 or higher
- Pip (Python package installer)
- Virtualenv (optional, but recommended)

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/s3dawyXD/Online-Library-System.git
   cd Online-Library-System
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate   # For macOS/Linux
   env\Scripts\activate
   ```
3. **install dependencies:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Set up environment variables:**

- Create a `.env` file in the project root and set `DATABASE_URL`
  example: `DATABASE_URL=postgres://postgres:password@localhost:5432/db`

5. **Apply database migrations:**

   ```bash
   python manage.py migrate

   ```

6. **load initial data: (Optional)**

   ```bash
   python manage.py loaddata initial_data.json

   ```

7. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser

   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### Docker

or you can build it using docker
`    docker compose up --build
   `

## Endpoint Documentation

All endpoint Can be find
`http://localhost:8000/swagger`
