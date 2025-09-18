# AWS-RAG-CICD

A Retrieval-Augmented Generation (RAG) chatbot project using Docker, Ollama (or GROQ), vector embeddings and deployed on AWS via CI/CD pipelines.

---

## Architecture

- The application uses embeddings + vector store to support document retrieval.  
- The LLM (Ollama or GROQ) is used to generate responses based on prompt + retrieved context.  
- CI/CD pipeline builds Docker image → pushes to AWS ECR → deploys/run on AWS EC2.  
- Secrets and configuration via GitHub Actions secrets/env vars.

---

## Prerequisites

- AWS account with IAM permissions for ECR, EC2.  
- ECR repository created.  
- EC2 instance ready to pull & run the Docker image.  
- (Optional) Ollama hosted endpoint / GROQ API key.  
- Docker

---
