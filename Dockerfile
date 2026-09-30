FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY riprap_stone_size_calculator.py app.py ./
EXPOSE 7860
CMD ["python", "app.py"]
