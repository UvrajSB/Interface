FROM python:3.11

WORKDIR /app

# Install application dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application source code.
COPY GUI/main.css .
COPY main.py .

CMD ["taipy", "run", "--no-debug", "--no-reloader", "main.py", "-H", "0.0.0.0", "-P", "5000"]
