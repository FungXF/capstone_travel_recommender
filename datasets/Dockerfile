# Use the official lightweight Python image from
# https://hub.docker.com/_/python
FROM python:3.8-slim 

# Copy all the files needed for the app to work
COPY inference.py .
COPY requirements.txt .
COPY att_canada_ratesen.pkl .
COPY attractions.pkl .

# Install all the necessary libraries
RUN pip install -r requirements.txt

# Run the API!
CMD python inference.py
