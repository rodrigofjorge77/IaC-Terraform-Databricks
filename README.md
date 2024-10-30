# Iac Terrafrom and Databricks

## Table of Contents
- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [License](#license)
- [MyLinks](#my-links)

## Overview
Infrastructure as Code (IaC) with Terraform, combined with distributed data processing on Databricks, 
offers a scalable, efficient, and automated approach to manage and analyze data. By leveraging Terraform, 
infrastructure deployments become repeatable and consistent, minimizing the risks of human error and 
ensuring faster, reliable configurations. 
Integrating this with Databricks’ powerful processing capabilities allows for robust data transformations 
and analyses at scale, particularly beneficial for handling large datasets and optimizing workflows in cloud environments.

In this architecture, raw sales data is initially uploaded by users to an AWS S3 bucket, providing a centralized 
location for storage. From here, a PySpark script is executed on a Databricks cluster hosted in the AWS cloud. T
his script performs several critical processing steps: first, it eliminates duplicate records to ensure data integrity. 
It then fills in any empty columns to handle missing values. Following data cleaning, the script performs aggregations 
by various dimensions, such as product, region, and sales method, creating valuable insights from the data. 
Finally, the processed results are saved back into another S3 bucket, where they are readily accessible 
for downstream analysis or reporting.

## System Architecture

![System Architecture](https://github.com/rodrigofjorge77/IaC-Databricks/blob/main/assets/architecture.png)

#### The project is designed with the following components:

- **Data Source**: File nike_dt_s3.csv got from https://www.kaggle.com/
- **AWS S3**: Used for storage files
- **Databricks**: Responsible for distributed processing

## Technologies

- Docker
- Terraform
- PySpark

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/SidiahmedHABIB/e2e-data-engineering.git
    ```

2. Navigate to the project directory:
    ```bash
    cd e2e-data-engineering
    ```
3. Install packages:
    ```bash
    pip install airflow
    pip install kafka-python
    pip install spark pyspark
    pip install cassandra-driver
    ```
4. Run Docker Compose to spin up the services:
    ```bash
    docker-compose up
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## My Links
[![FaceBook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/habib.sidiahmed.5)   [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sidi-ahmed-habib-18163220a/)
