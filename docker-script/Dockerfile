FROM python
WORKDIR /app

# Install packages and dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Install websites.txt file
COPY websites.txt /app/

COPY traffic_simul.py /app/

CMD ["python3", "./traffic_simul.py"]
