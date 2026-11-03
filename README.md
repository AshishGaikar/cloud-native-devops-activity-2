# Cloud Native DevOps – Activity 2
## Jenkins CI/CD Pipeline with Terraform Infrastructure Provisioning

### 1. Project Overview

This project demonstrates the implementation of a **Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins** and **Infrastructure as Code (IaC) using Terraform**.

The project automates the process of retrieving application source code from GitHub, installing dependencies, building the application, and executing automated tests through a Jenkins pipeline.

Terraform is used to define cloud infrastructure on Amazon Web Services (AWS), including an EC2 instance and its security group.

### 2. Objectives

- Configure Jenkins to integrate with a GitHub repository.
- Automate application checkout, dependency installation, and testing.
- Create a Jenkins pipeline using a `Jenkinsfile`.
- Write Terraform configuration files to define AWS infrastructure.
- Validate Terraform configurations using `terraform init`, `terraform validate`, and `terraform plan`.
- Capture screenshots demonstrating successful execution.

### 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web application framework |
| Pytest | Automated application testing |
| Docker | Running Jenkins in a container |
| Jenkins | CI/CD pipeline automation |
| Git and GitHub | Source code management |
| Terraform | Infrastructure as Code |
| AWS EC2 | Cloud infrastructure target |
| GitHub Codespaces | Development environment |

### 4. Project Structure

```text
cloud-native-devops-activity-2/
│
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── Dockerfile.jenkins
├── Jenkinsfile
├── .gitignore
│
├── tests/
│   └── test_app.py
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── .terraform.lock.hcl
│
│
├── screenshots/
│
└── README.md
```

### 5. Application and Automated Testing

The project contains a Python Flask application with the following endpoints:

- `/` – Displays the application welcome message.
- `/health` – Returns the application health status.

Pytest is used to execute automated tests for these endpoints.

**Run the tests locally:**

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

**Test result:**

```text
2 passed
```

Both automated tests completed successfully.

### 6. Jenkins CI/CD Pipeline

Jenkins was configured to retrieve the source code from the public GitHub repository and execute the pipeline defined in the `Jenkinsfile`.

Jenkins was run using Docker with a custom image based on the official Jenkins LTS image. Python, pip, and Git were installed in the custom image to support the pipeline.

**Build the Jenkins Docker image:**

```bash
docker build -f Dockerfile.jenkins -t cloud-native-jenkins:1.0 .
```

**Run the Jenkins container:**

```bash
docker run -d \
  --name jenkins-server \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  cloud-native-jenkins:1.0
```

Open Jenkins at:

```text
http://localhost:8080
```

When running inside GitHub Codespaces, use the forwarded port 8080 URL provided by Codespaces.

#### Jenkins Pipeline Stages

The pipeline contains the following stages:

1. **Checkout:** Retrieves the application source code from GitHub.
2. **Build:** Creates a Python virtual environment, installs dependencies, and checks Python syntax.
3. **Test:** Runs automated tests using Pytest.

A post-build section displays success or failure messages depending on the pipeline result.

**Pipeline Execution Result:**

```text
2 passed
Finished: SUCCESS
```

The Jenkins pipeline executed successfully, and both automated tests passed.

### 7. Terraform Infrastructure Provisioning

Terraform was used to define AWS infrastructure through configuration files.

The infrastructure configuration includes:

- An AWS provider configured for the `ap-south-1` region.
- The default AWS VPC.
- An Amazon Linux 2023 AMI data source.
- An EC2 instance using the `t3.micro` instance type.
- A security group allowing inbound HTTP traffic on port 80.
- An output configuration for the instance ID, public IP, and website URL.

#### Terraform Files

| File | Description |
|---|---|
| `main.tf` | Defines AWS provider, data sources, security group, and EC2 instance |
| `variables.tf` | Defines region, instance type, and project name |
| `outputs.tf` | Defines infrastructure output values |
| `.terraform.lock.hcl` | Locks the selected Terraform provider version |

#### Terraform Commands

Navigate to the Terraform directory:

```bash
cd terraform
```

Initialize Terraform:

```bash
terraform init
```

Validate the configuration:

```bash
terraform validate
```

Format the configuration:

```bash
terraform fmt
```

Generate the infrastructure execution plan:

```bash
terraform plan
```

#### Terraform Validation Results

- `terraform init` completed successfully.
- `terraform validate` completed successfully.
- `terraform plan` completed successfully.

The Terraform plan reported:

```text
Plan: 2 to add, 0 to change, 0 to destroy.
```

This plan identified two resources to be created: an EC2 instance and a security group.

**Note:** The successful Terraform plan validates the proposed infrastructure changes. It does not mean that the AWS resources were actually created. Actual provisioning requires running `terraform apply` with valid AWS credentials and appropriate permissions.

### 8. Understanding CI/CD and Infrastructure as Code

#### Continuous Integration and Continuous Deployment (CI/CD)

CI/CD is a development approach that automates software integration, building, and testing.

In this project, Jenkins retrieves the source code from GitHub, installs the required dependencies, checks the application, and runs automated tests. This reduces manual effort and helps identify errors early.

#### Infrastructure as Code (IaC)

Infrastructure as Code is the practice of defining and managing infrastructure using configuration files instead of creating resources manually.

Terraform implements IaC in this project by defining AWS infrastructure in `.tf` files. This makes infrastructure easier to validate, reproduce, and manage.

### 9. Screenshots and Execution Evidence

The `screenshots/` directory contains evidence of the project implementation and execution.

| Screenshot | Evidence |
|---|---|
| `01-automated-tests.png` | Successful execution of Python tests |
| `02-jenkins-docker-image.png` | Jenkins Docker image build |
| `03-jenkins-container.png` | Jenkins container running |
| `04-jenkins-dashboard.png` | Jenkins dashboard |
| `05-github-repository.png` | GitHub repository |
| `06-jenkinsfile.png` | Jenkins pipeline configuration |
| `07-jenkins-build-logs.png` | Jenkins build logs |
| `08-jenkins-pipeline-success.png` | Successful Jenkins pipeline execution |
| `09-terraform-init.png` | Terraform initialization |
| `10-terraform-validate.png` | Terraform validation |
| `11-terraform-plan-part1.png` | Terraform plan details |
| `12-terraform-plan-part2.png` | Terraform plan details |
| `13-terraform-plan-summary.png` | Terraform plan summary |

### 10. Conclusion

This activity successfully demonstrates the implementation of a Jenkins CI/CD pipeline integrated with GitHub and automated Python testing.

It also demonstrates Infrastructure as Code using Terraform to define AWS cloud infrastructure and validate the proposed deployment plan.

The Jenkins pipeline completed successfully, both automated tests passed, and Terraform initialization, validation, and planning were completed successfully.

This project provides practical experience with CI/CD automation, Docker, GitHub integration, automated testing, Terraform, and cloud infrastructure management.

### 11. Repository

**GitHub Repository:**  
https://github.com/AshishGaikar/cloud-native-devops-activity-2

Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username.
