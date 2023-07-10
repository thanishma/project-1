This is a restaurant management application. 

which has a docker image 
commands used for building and pushing the docker images
docker login -->provide the docker hub details 
docker build -t thanishma/restaurants-app .
docker run -p 8000:8000 thanishma/restaurants-app
docker push thanishma/restaurants-app
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5f37953-397e-49f9-a574-98b57150bf77/Untitled.png)

Also, deployed on kubernetes 
commands used for deploying on kubernetes -
minikube start
minikube addons enable ingress
kubectl apply -f restaurant-mgmt.yml
kubectl get pods 
kubectl get services
minikube service <service_name> --> you will get the webpage

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1564b55-8272-470c-9a3c-eb311188795e/Untitled.png)
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f52f368-c38e-49e1-9729-4aa61dab3f26/Untitled.png)
