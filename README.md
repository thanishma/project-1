This is a restaurant management application. 

which has a docker image 

commands used for building and pushing the docker images

docker login -->provide the docker hub details 

docker build -t thanishma/restaurants-app .

docker run -p 8000:8000 thanishma/restaurants-app

docker push thanishma/restaurants-app




Also, deployed on kubernetes 

commands used for deploying on kubernetes -

minikube start

minikube addons enable ingress

kubectl apply -f restaurant-mgmt.yml

kubectl get pods 

kubectl get services

minikube service <service_name> --> you will get the webpage

