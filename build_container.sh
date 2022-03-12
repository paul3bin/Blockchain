#!/bin/bash
target=blockchain

docker stop $target
docker rm -f $target
docker build -t $target .
docker run -d --restart=unless-stopped -p 5000:5000 --name=$target $target
docker logs -f $target