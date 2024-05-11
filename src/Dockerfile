FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY get_embedding_function.py /app/

RUN python /app/get_embedding_function.py

COPY populate_database.py /app/

# RUN python /app/populate_database.py

COPY query_data.py /app/
COPY templates/ /app/templates
COPY api.py /app/
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENTRYPOINT [ "./entrypoint.sh" ]