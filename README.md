# Dockerized Python web application

**Prompt:
Develop a demonstration project utilizing Terraform to deploy a basic application (any basic CRUD application) on either Google Cloud Platform (GCP) or Amazon Web Services (AWS). This project should include network configuration and utilize a secret management tool alongside Docker and Kubernetes.**

This setup allows your Flask application to run on AWS EKS,
pulling credentials securely from AWS Secrets Manager

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


