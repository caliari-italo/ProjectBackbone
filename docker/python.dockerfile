FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r /app/requirements.txt