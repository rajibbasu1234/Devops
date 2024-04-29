# Dockerized Python web application

**Prompt:
Develop a demonstration project utilizing Terraform to deploy a basic application (any basic CRUD application) on either Google Cloud Platform (GCP) or Amazon Web Services (AWS). This project should include network configuration and utilize a secret management tool alongside Docker and Kubernetes.**

This setup allows your Flask application to run on AWS EKS,
pulling credentials [db username/password] securely from AWS Secrets Manager and then
use these credentials to connect to DB. I havnt written implementation of how its connect 
to the DB in the python code : https://github.com/rajibbasu1234/Devops/blob/main/docker/app.py#L31


## Project / Folder Structure

![Alt text](images/folder.png?raw=true "Title")


1. terraform Configuration: Files to set up the AWS infrastructure.
2. kubernetes Configuration: YAML files for Kubernetes deployment.
3. docker / application Code: A simple CRUD application, containerized using Docker.

## Step 1: Set up your Terraform environment

### Requirements:
- Terraform installed on your machine.
- AWS CLI installed and configured.
- Kubernetes CLI (kubectl) installed.
- Docker installed.

To create a Dockerized Python web application that uses Amazon Secrets Manager
for sensitive data and is deployed on Amazon Elastic Kubernetes Service (EKS),
you'll need to integrate several components. Here's a step-by-step guide and code to help you achieve this.

## Apply Terraform configuration to create EKS cluster

```commandline
cd terraform
terraform init
terraform apply
```

Make sure you have the necessary IAM permissions to create 
and manage EKS resources, and that your AWS credentials 
are properly configured. Additionally, ensure that
your ~/.kube/config file is correctly configured to access
your Kubernetes cluster.

## Kubernetes Deployment on AWS EKS

You'll need to set up AWS EKS and create a deployment. 
This requires an EKS cluster and kubectl configured to interact with your cluster.

## Create a Kubernetes Secret for AWS credentials:

```
kubectl create secret generic aws-secret --from-literal=AWS_ACCESS_KEY_ID=xxx --from-literal=AWS_SECRET_ACCESS_KEY=yyy
```

## Build and Push Docker Image

```commandline
cd docker 
docker build -t my-flask-app . 
```

## quick note

1. container is running at port 5000 but mapped tp port 80
https://github.com/rajibbasu1234/Devops/blob/main/kubernetes/service.yaml#L7

2.The python application https://github.com/rajibbasu1234/Devops/blob/main/docker/app.py
needs  AWS credentials configured that have permission
to access Secrets Manager.This is passed during k8s deployment https://github.com/rajibbasu1234/Devops/blob/main/kubernetes/deployment.yaml#L21






## uploading this image to amazon ecr [optional]
```commandline
docker tag my-flask-app:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/my-flask-app:latest
docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/my-flask-app:latest
```

## Deploy on EKS

To deploy resources to a specific Amazon EKS (Elastic Kubernetes Service) cluster 
using Kubernetes manifests, you need to ensure that your kubectl configuration is 
set to target that cluster. 
Here's how you can deploy resources to a particular EKS cluster

**Update kubeconfig:** : Use the AWS CLI to update your kubeconfig file with the necessary 
authentication details for the specific EKS cluster:

```aws eks update-kubeconfig --name raj-eks-cluster```

Next create cluster

```commandline
cd kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

```

You can access the python application via

```
http://{external_ip_of_cluster}:80
```


