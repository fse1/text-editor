FROM python:3.7-buster

# Set the home directory to /texteditor
ENV HOME /texteditor

# cd into the home directory
WORKDIR /texteditor

# Copy all app files into the image
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Change Directory
WORKDIR /texteditor/text_editor_site

# Allow port 5000 to be accessed from outside the container
EXPOSE 5000

# Run the app
CMD python initialize_database.py && python manage.py runserver 0:5000
