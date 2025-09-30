# Use official Python base image
FROM python:3.13.5-bookworm

# Set working directory
WORKDIR /app

# Copy dependencies file first (for caching)
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the application
COPY . .

# Expose the app port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
