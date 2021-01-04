# Create an image based on python 3.7
FROM python:3.7
# Create the needed directories
RUN mkdir /api
RUN mkdir /api/assets
RUN mkdir /api/assets/img
# Copy source code & requirements to the api folder
COPY api.py /api/api.py
COPY requirements.txt /api/requirements.txt
# Select the work directory
WORKDIR /api
# Install required packages
RUN pip install -r requirements.txt
# Launch the python command
CMD ["python", "api.py"]

# docker run -p 5000:5000 -t challenge-flask
# docker build . -t challenge-flask