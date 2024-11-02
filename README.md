# Iac Terraform and Databricks

## Table of Contents
- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [License](#license)

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

![System Architecture](https://github.com/rodrigofjorge77/IaC-Databricks/blob/main/assets/DatabricksArchitecture.gif)

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
    git clone https://github.com/rodrigofjorge77/IaC-Databricks.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Terraform
    ```
3. Run Docker Compose
    ```bash
    docker build -t databricks-terraform-image .
    docker run -dit --name databricks -v ./IaC:/iac databricks-terraform-image /bin/bash
    ```

## License

This project is licensed under the MIT License

