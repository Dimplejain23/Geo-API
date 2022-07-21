# Introduction 
This is a Python based Rest API web application for Spatial Data. This project includes CRUD operations for spatial data into Geodjango ORM. Also it includes celery implementation to run asynchronous job to download data of countries from datahub.io and upload it to PostGIS db at every 10 minutes interval. Two replicas of the application are created and load balancing is applied through nginx server.

# Built with
This section should list any major frameworks/libraries used as follows:

* [Geo-Django](https://docs.djangoproject.com/en/4.0/ref/contrib/gis/tutorial/)
* [Celery](https://docs.celeryq.dev/en/stable/index.html)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Flower](https://flower.readthedocs.io/en/latest/)
* [PostGIS](https://postgis.net/)
* [PGAdmin](https://www.pgadmin.org/)
* [Nginx](https://www.nginx.com/)

# Build and Test
The project uses docker-compose for deployment 

<!-- GETTING STARTED -->
## Getting Started
docker-compose.yml version 3.9 is used hence make sure you docker-compose is up-to-date

### Prerequisites

To install latest docker-compose on linux environment use
* docker-compose
  ```sh
  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  ```

### Build

To run the project use following steps

1. Build docker images and run docker containers
   ```sh
   sudo docker-compose up -d --build
   ```
   up parameter is to start container, -d is used to run the process in background (daemon mode) and --build is used to build the image if running it for the first time or changes made to dockerfile
   
2. To stop the container use
   ```sh
   sudo docker-compose down
   ```

### Test

To run unittest cases for Django run the following command

  ```sh
   docker exec -it geoapi sh -c "cd /code/geoapp/ && python manage.py test"
   ```
<!-- USAGE EXAMPLES -->
# Usage
Below are urls of the rest apis to test functionalities and view parameters for the api

1. Create Country
   [URL](http://localhost:1337/api/create/)
2. Get all Countries
   [URL](http://localhost:1337/api/fetchall/)
3. Get specific country
   [URL](http://localhost:1337/api/getcountry/)
4. Update Country details
   [URL](http://localhost:1337/api/update/)
5. Delete Country
   [URL](http://localhost:1337/api/delete/)
6. Search Country by String
   [URL](http://localhost:1337/api/search/)
7. Spatial intersection by Geometry
   [URL](http://localhost:1337/api/sgeomquery)
8. Spatial intersection by country name
   [URL](http://localhost:1337/api/squerybycountry)
   
<!-- USAGE EXAMPLES -->
# Troubleshoot
If you face the below issues please follow the steps to rectify
1. *standard_init_linux.go:228: exec user process caused: no such file or directory* error on docker windows.
   To solve it run the following command. Delete the repo and clone it again 
   ```sh
   git config --global core.autocrlf false
   ```
2. *permission denied to run .sh file*
   If you are running a linux based os please run the following commands to make all .sh files executable and then run docker-compose
   ```sh
   sudo chmod +x wait-for-it.sh
   sudo chmod +x startup_service.sh
   sudo chmod +x start_celery.sh
   ```
