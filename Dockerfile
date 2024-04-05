# Use a relevant Python base image (e.g., python:3.10)
FROM python:3.12.2

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your project code
COPY . .

# Expose the port Gunicorn will listen on (usually 8000)
EXPOSE 8000

# Command to run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]

# Replace "your_project" with the actual name of your Django project
# Replace "your_project.wsgi:application" with the appropriate WSGI entry point
