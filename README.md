# Spark-platform
This project aim to setup a `BIG DATA` processing platform using Apache Spark as the bid data processing tool. This platform has different components that form the entire platform. The end goal is to have a platform that automatically run our big data workloads at a specific time.

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
- Spark
  - This directory contains all Spark Application
- .github
  - This directory contains the following
    - Github Action workflow that automatically validate and deploy our flows to a running Kestra instance whenever there is any changes.
    - Github Action Wworkflow that automatically validate and push our spark application to Amazon s3 whenever there is any changes.

![Excalidraw Diagram](Excalidraw.png)


For each group, you are to create a VPC, 


In your repository, you would use GitHub as well for CI/CD TO pick python file/spark application from your local and deploy to the cloud (AWS S3)

You will use Step Functions to:
1.	Fetch the python file (which should have now been uploaded in s3).
2.	To create an EMR cluster  
3.	Run Step
4.	Terminate the cluster, after running the application


## TO USE THE CD

- Run `brew install ngrok`
- Run `ngrok http http://0.0.0.0:8080 --host-header=rewrite`
  - Copy the new URL into your action

##   CONSIDERATIONS USING THE CD
- Make sure your namespace is aligned
