#!/bin/bash

echo "Starting the db service ..."
docker-compose up -d db

echo "Pause to give the db time to initialize"
sleep 30

echo "db service started successfully"

echo "Creating ProXChat data volume..."
docker run --rm --network=proxchat_default -v "${PWD}/data:/data" -e DB_USERNAME=root -e DB_PASSWORD=mysql -e DB_HOST=db -e DB_NAME=process_data python:3.9 /bin/bash -c "pip install -r /data/requirements.txt && python /data/csv_to_db_docker.py"

echo "Data volume created successfully"

echo "Loading ProXChat docker images..."
docker load -i proxchat-backend.tar
docker load -i proxchat-frontend.tar

echo "Images loaded successfully"

echo "Building ProXChat docker-compose..."
docker-compose build

echo "Starting services..."
docker-compose up

echo "Finished successfully"
