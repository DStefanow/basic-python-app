FROM python:3

# Set the working directory for the application
WORKDIR /usr/src/app

# Copy and install all needed python modules
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code of the application
COPY src/ .

# Set needed environmental variable
# Expose the flask application to the whole world
ENV FLASK_RUN_HOST=0.0.0.0

# Expose working port for Flask application
EXPOSE 5000

# Start command to launch the application
CMD ["python3", "-m", "flask", "--app", "connector", "run"]
