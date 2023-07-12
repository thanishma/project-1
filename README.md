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

![image](https://github.com/thanishma/project-1/assets/73327713/c24ee440-45a1-4f1f-b881-ac098a0933f9)

Deploying application using ELK-STACK via kubernetes-

Commands used- 

kubectl apply -f elk-stack.yml -n elk-stack

kubectl apply -f restaurant-mgmt.yml -n elk-stack

Kubectl get services/pods/deployments -n elk-stack -->to get the objects

minikube service restaurant-mgmt -n elk-stack

![image](https://github.com/thanishma/project-1/assets/73327713/36d478bd-d98f-4a6e-814e-68fb7c01acd9)

![image](https://github.com/thanishma/project-1/assets/73327713/bf919ae5-65d5-4d20-8182-ac966bac7cb9)

![image](https://github.com/thanishma/project-1/assets/73327713/a4bb5f24-1e89-4add-b52c-dcf329446208)

minikube service kibana -n elk-stack --> for getting the kibana 

![image](https://github.com/thanishma/project-1/assets/73327713/eba1ee43-3b61-4e4a-9196-9d4713877cb9)

![image](https://github.com/thanishma/project-1/assets/73327713/3fcd1f8c-9afd-4ca3-a1c3-7daddb3a24fa)


