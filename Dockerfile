FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY server.py .

# Expose the default port
EXPOSE 8000

# Default command: Run with SSE transport on port 8000
# Users can override this to use stdio or other transports/ports
ENTRYPOINT ["python", "server.py"]
CMD ["--transport", "sse", "--port", "8000", "--host", "0.0.0.0"]
