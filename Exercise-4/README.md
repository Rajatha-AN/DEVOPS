# Exercise 4 — Docker Networking with Multiple Containers

## Objective

Understand Docker networking concepts and configure a multi-container application using a custom Docker bridge network.

## Scenario

The application consists of three containers:

- **Flask** — Python REST API
- **MySQL** — Database container
- **Redis** — Cache container

All containers communicate through the custom Docker bridge network `my-bridge-net`.

## Technologies Used

- Docker Desktop
- Python
- Flask 2.0.1
- MySQL
- Redis
- Docker Bridge Networking

## Files

```text
Exercise-4/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
1. Create the Bridge Network
docker network create --driver bridge my-bridge-net

The custom bridge network my-bridge-net was created successfully.

2. Verify the Network
docker network ls

The network appeared with:

NAME            DRIVER    SCOPE
my-bridge-net   bridge    local
3. Build the Flask Image
docker build --no-cache -t flask-api .

The Flask image was built successfully.

4. Launch the Containers

Redis:

docker run -d --name redis --net=my-bridge-net redis:latest

MySQL:

docker run -d --name mysql --net=my-bridge-net \
  -e MYSQL_ROOT_PASSWORD=root \
  mysql:latest

Flask:

docker run -d --name flask \
  --network=my-bridge-net \
  -p 5001:5001 \
  flask-api

The MySQL container required MYSQL_ROOT_PASSWORD because the MySQL image does not initialize without a password configuration.

5. Test the Flask API
/about
curl http://localhost:5001/about

Output:

{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
/redis
curl http://localhost:5001/redis

Output:

{
  "message": "Hello from Flask to Redis!",
  "status": "success"
}
6. Verify Container Networking

The Flask container was connected to the same custom bridge network as MySQL and Redis.

Docker DNS resolution was verified from the Flask container using Python:

docker exec flask python -c "import socket; print(socket.gethostbyname('mysql'))"

Result:

172.18.0.4

Redis:

docker exec flask python -c "import socket; print(socket.gethostbyname('redis'))"

Result:

172.18.0.2

This confirms that the Flask container could resolve the MySQL and Redis containers by their Docker container names.

The network inspection also showed the containers attached to my-bridge-net:

redis  172.18.0.2/16
mysql  172.18.0.4/16
flask  172.18.0.3/16

Note: The exercise uses ping for connectivity testing, but the Flask container did not contain the ping executable. Docker DNS/network connectivity was therefore verified using Python's socket.gethostbyname() instead.

7. Cleanup

After completing the networking tests, the containers were stopped and removed:

docker stop mysql redis flask
docker rm mysql redis flask

The custom network was then removed:

docker network rm my-bridge-net
Result

The multi-container Docker networking exercise was successfully completed. Flask, MySQL, and Redis were connected through a custom Docker bridge network, and container-to-container DNS resolution was verified successfully.
