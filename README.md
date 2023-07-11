This is a restaurant management application. 

which has a docker image 

commands used for building and pushing the docker images

docker login -->provide the docker hub details 

docker build -t thanishma/restaurants-app .

docker run -p 8000:8000 thanishma/restaurants-app

docker push thanishma/restaurants-app

![image](https://github.com/thanishma/project-1/assets/73327713/c3b8af30-af4c-4104-b382-8ff9d4e08d65)


Also, deployed on kubernetes 

commands used for deploying on kubernetes -

minikube start

minikube addons enable ingress

kubectl apply -f restaurant-mgmt.yml

kubectl get pods 

kubectl get services

minikube service <service_name> --> you will get the webpage

![image](https://github.com/thanishma/project-1/assets/73327713/163df788-709e-4fb7-af00-c82288fae59a)


![image](https://github.com/thanishma/project-1/assets/73327713/bba86086-734a-40ef-85c9-475fd788672d)

![image](https://github.com/thanishma/project-1/assets/73327713/7a311721-e459-4f08-9d40-416e6b0e5a74)


