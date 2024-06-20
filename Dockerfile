
FROM python:3.10

WORKDIR /usr/src/app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

# Run migrations before starting the server
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Create superuser for admin interface
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Command to start the server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]
