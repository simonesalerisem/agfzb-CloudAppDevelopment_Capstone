# Use Python 3.11 as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

# Update the system and install netcat, which is useful for troubleshooting network issues
RUN apt-get update \
    && apt-get install -y netcat

# Set working directory in the container
ENV APP=/app
WORKDIR $APP

# Add the requirements.txt file to the container
COPY requirements.txt $APP

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Add the rest of the project files to the container
COPY . $APP

# Expose port 8000 for the application
EXPOSE 8000

# Make the entrypoint.sh file executable
RUN chmod +x /app/entrypoint.sh

# Use bash to run the entrypoint.sh script
ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi"]