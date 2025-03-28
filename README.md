# Spark-platform
This project aim to setup a `BIG DATA` processing platform using Apache Spark as the big data processing tool. This platform has different components that form the entire platform. The end goal is to have a platform that automatically run our big data workloads at a specific time.

# Platform Tool Stacks
- Kubernetes
- Kestra Instance
- EMR Cluster
- Apache Spark
- AWS Resources
  - VPC
  - S3
  - IAM
  - SSM Parameter
- CI/CD (Github Action)

# Project Layout Summary
- Infrastructure
  - This directory contains all the cloud infrstaructure needed to enable the platform to be functional
    - IAM
      - Dedicated IAM User for Kestra Instance
      - Dedicated IAM Policy and IAM Role for the EMR Cluster
    - S3
      - Dedicated s3 buckets to be used for EMR Cluster logs, Spark Application code, Input dataset and Output datasets.
    - VPC
      - Dedicated network for EMR Cluster
- Kestra
  - This directory contains all flows that will be launched on the Kestra instance and different namespace.
  - The flow in this directory do 3 things
    - Create an EMR Cluster with Apache Spark running on it
    - Submit a Spark Application task to the EMR Cluster to run the job.
    - Terminate as soon as the Spark job is done.
- Spark
  - This directory contains all Spark Application
- .github
  - This directory contains the following
    - Github Action workflow that automatically validate and deploy our flows to a running Kestra instance whenever there is any changes.
    - Github Action Wworkflow that automatically validate and push our spark application to Amazon s3 whenever there is any changes.
    - NOTE
      - To be able to get the value for the server in the kestra.yaml, you need ngrok
        - Run `brew install ngrok` on your terminal for Mac user.
        - signup on `ngrok.com`
        - Run `ngrok config add-authtoken YourTokenFromTheWebsiteAfterSignUp` on your terminal.
