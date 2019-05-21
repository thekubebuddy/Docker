iversion: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: smartbuddy/hello-flask:1.0
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "4000:80"
    networks:
      - webnet
networks:
  webnet:

