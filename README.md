# Sample Python Dockerized App Using Flask

## Build and Run Docker Image

Use the below command to build the docker image.

- `docker build --rm -t duplo-python-app`

Use the following command to run the image.

- `docker run -p 8082:8082 duplo-python-app`

## Push Docker Image to Docker Hub

- `docker login`
- `docker tag duplo-python-app:latest tahirstamboli/duplo-python-app:v1.0`
- `docker push tahirstamboli/duplo-python-app:v1.0`
