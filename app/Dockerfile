FROM python:3.9-slim
WORKDIR /app
COPY server.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "server.py"]

