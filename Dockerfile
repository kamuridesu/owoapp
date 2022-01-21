FROM python:3
RUN pip3 install flask
COPY . .
CMD ["python", "generator.py"]