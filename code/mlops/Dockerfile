FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Install necessary OS packages
RUN apt-get update && \
    apt-get install -y \
    git \
    libgl1-mesa-glx  

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run train_model.py when the container launches
CMD ["python", "./somnolence_detection.py"]