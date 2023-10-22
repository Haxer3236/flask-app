# image with python
FROM python:3.9
# Working Directory for the app
WORKDIR . app/
# Copy the code 
COPY app.py .
# install required liabaries
RUN pip install flask
# Run the application
CMD ["python","app.py"]
