#!/bin/bash

if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker and run this script again."
    exit 1
fi

MYSQL_ROOT_PASSWORD="root"
CONTAINER_NAME="mysql-container"
SAMPLE_DATA_SQL="mysqlsampledatabase.sql"

docker pull mysql:latest
docker run -d --name $CONTAINER_NAME -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD mysql:latest

echo "Waiting for MySQL container to start..."
sleep 20

echo "Copy sample DB to container"
docker cp $SAMPLE_DATA_SQL $CONTAINER_NAME:/tmp/$SAMPLE_DATA_SQL
sleep 5

echo "Load sample data into MySQL container"
docker exec -i mysql-container sh -c "mysql -u root -p$MYSQL_ROOT_PASSWORD -e 'source /tmp/mysqlsampledatabase.sql'" 
sleep 5

pip3 install -r requirements.txt