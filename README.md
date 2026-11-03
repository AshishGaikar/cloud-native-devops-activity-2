# Cloud Native DevOps – Activity 2
## Jenkins CI/CD Pipeline with Terraform Infrastructure Provisioning

### 1. Project Overview

This project demonstrates the implementation of a **Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins**, **containerization using Docker**, **Kubernetes application deployment**, and **Infrastructure as Code (IaC) using Terraform**.

The project automates the process of retrieving application source code from GitHub, installing dependencies, building a Docker image, executing automated tests, and deploying the application to a Kubernetes cluster through a Jenkins pipeline.

Terraform is used to define cloud infrastructure on Amazon Web Services (AWS), including an EC2 instance and its security group.

The project was developed and executed using GitHub Codespaces.

### 2. Objectives

- Configure Jenkins to integrate with a GitHub repository.
- Automate source-code checkout, dependency installation, and application building.
- Create a Jenkins pipeline using a `Jenkinsfile`.
- Build and manage a Docker image for the Flask application.
- Execute automated application tests using Pytest.
- Deploy the application to a Kubernetes cluster using Jenkins.
- Configure Kubernetes Deployment and Service resources.
- Write Terraform configuration files to define AWS infrastructure.
- Validate Terraform configurations using `terraform init`, `terraform validate`, and `terraform plan`.
- Capture screenshots demonstrating the implementation and execution of the project.

### 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web application framework |
| Pytest | Automated application testing |
| Docker | Application containerization and Jenkins environment |
| Jenkins | CI/CD pipeline automation |
| Git and GitHub | Source code management |
| Kubernetes | Container orchestration |
| KIND | Local Kubernetes cluster |
| kubectl | Kubernetes cluster management |
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
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── .terraform.lock.hcl
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

### 6. Docker Containerization

Docker is used to package the Flask application into a container image.

The application Dockerfile defines the environment, dependencies, and startup command required to run the Flask application.

A separate custom Jenkins Docker image is used to provide the tools required by the CI/CD pipeline, including Python, Git, Docker CLI, Kubernetes CLI (`kubectl`), and KIND.

This allows Jenkins to build the application image, execute tests, and communicate with the Kubernetes cluster.

### 7. Jenkins CI/CD Pipeline

Jenkins was configured to retrieve the source code from the public GitHub repository and execute the pipeline defined in the `Jenkinsfile`.

Jenkins was run inside a Docker container using a custom Jenkins image.

The Jenkins environment was configured with access to the Docker daemon and the KIND Kubernetes cluster so that the pipeline could perform automated application deployment.

Jenkins dashboard:

```text
http://localhost:8080
```

When running inside GitHub Codespaces, use the forwarded port 8080 URL provided by Codespaces.

#### Jenkins Pipeline Stages

The Jenkins pipeline contains four stages:

**1. Checkout**

- Retrieves the application source code from the GitHub repository.
- Uses Jenkins Pipeline from SCM to access the `Jenkinsfile`.

**2. Build**

- Creates a Python virtual environment.
- Installs the required application and development dependencies.
- Checks Python syntax.
- Builds the Docker image for the Flask application.

**3. Test**

- Executes automated tests using Pytest.
- Checks the application endpoints.
- Confirms that the application passes its automated tests before deployment.

**4. Deploy**

- Loads the application Docker image into the KIND Kubernetes cluster.
- Applies the Kubernetes Deployment configuration.
- Applies the Kubernetes Service configuration.
- Waits for the Kubernetes Deployment rollout to complete.
- Displays the Kubernetes pods and services.

#### Pipeline Execution Result

The Jenkins pipeline was executed successfully, including the build, testing, and Kubernetes deployment stages.

The automated tests reported:

```text
2 passed
Finished: SUCCESS
```

The successful pipeline execution demonstrates the integration of GitHub, Docker, automated testing, Jenkins, and Kubernetes deployment.

### 8. Kubernetes Deployment

Kubernetes is used to deploy and manage the Flask application.

A local Kubernetes cluster was created using KIND (Kubernetes in Docker).

The cluster was named:

```text
activity2-cluster
```

The cluster was checked using:

```bash
kind get clusters
kubectl get nodes
```

The Kubernetes node reached the `Ready` status.

#### Kubernetes Configuration Files

**deployment.yaml**

The Deployment configuration defines:

- Application name: `cloud-native-deployment`
- Number of replicas: 2
- Container image: `cloud-native-app:1.0`
- Container port: 5000

The two replicas help demonstrate Kubernetes workload management.

**service.yaml**

The Service configuration exposes the application using:

- Service name: `cloud-native-service`
- Service type: `NodePort`
- Service port: 80
- Target container port: 5000
- NodePort: 30080

#### Kubernetes Deployment Commands

Apply the Deployment:

```bash
kubectl apply -f kubernetes/deployment.yaml
```

Apply the Service:

```bash
kubectl apply -f kubernetes/service.yaml
```

Check the Deployment:

```bash
kubectl get deployments
```

Check the pods:

```bash
kubectl get pods
```

Check the Service:

```bash
kubectl get services
```

#### Accessing the Application

The application was accessed using Kubernetes port forwarding.

```bash
kubectl port-forward service/cloud-native-service 8081:80 --address 0.0.0.0
```

The forwarded port was opened through the GitHub Codespaces Ports interface.

The application welcome page was accessed through the forwarded application port.

The health endpoint can also be checked at:

```text
/health
```

### 9. Terraform Infrastructure Provisioning

Terraform was used to define AWS infrastructure through configuration files.

The infrastructure configuration includes:

- An AWS provider configured for the `ap-south-1` region.
- The default AWS VPC.
- An Amazon Linux 2023 AMI data source.
- An EC2 instance using the `t3.micro` instance type.
- A security group allowing inbound HTTP traffic on port 80.
- Output configurations for the instance ID, public IP, and website URL.

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

### 10. Understanding CI/CD and Infrastructure as Code

#### Continuous Integration and Continuous Deployment (CI/CD)

CI/CD is a development approach that automates software integration, building, testing, and deployment.

In this project, Jenkins retrieves the source code from GitHub, installs the required dependencies, builds the Docker image, runs automated tests, and deploys the application to Kubernetes.

This reduces manual effort and helps identify errors before deployment.

#### Infrastructure as Code (IaC)

Infrastructure as Code is the practice of defining and managing infrastructure using configuration files instead of creating resources manually.

Terraform implements IaC in this project by defining AWS infrastructure in `.tf` files. This makes infrastructure easier to validate, reproduce, and manage.

### 11. Screenshots and Execution Evidence

The `screenshots/` directory contains evidence of the project implementation and execution.

#### Original Implementation Evidence

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

#### Additional Kubernetes and Deployment Evidence

| Screenshot | Evidence |
|---|---|
| `14-kubernetes-config-files.png` | Kubernetes configuration files |
| `15-kubernetes-cluster-ready.png` | KIND Kubernetes cluster successfully created and ready |
| `16-kubernetes-deployment-config.png` | Kubernetes Deployment configuration |
| `17-jenkins-image-with-kubernetes-tools.png` | Jenkins Docker image with Kubernetes deployment tools |
| `18-jenkins-kubernetes-connection.png` | Jenkins connectivity with the Kubernetes cluster |
| `19-Full-pipeline.png` | Complete Jenkins CI/CD pipeline |
| `21-forward-to-ports.png` | Application port forwarding configuration |
| `22-ports.png` | GitHub Codespaces forwarded ports |
| `23-Application.png` | Running Flask application accessed through the forwarded port |

### 12. Conclusion

This activity demonstrates the implementation of an automated CI/CD pipeline using Jenkins, integrated with GitHub, Docker, Python, and Kubernetes.

The Jenkins pipeline automates source-code checkout, application building, automated testing, and Kubernetes deployment.

The project also demonstrates Infrastructure as Code using Terraform to define AWS cloud infrastructure and validate the proposed infrastructure execution plan.

The Jenkins pipeline completed successfully, both automated tests passed, the Kubernetes deployment workflow was demonstrated, and Terraform initialization, validation, and planning were completed successfully.

This project provides practical experience with CI/CD automation, containerization, Kubernetes orchestration, automated testing, Terraform, and cloud infrastructure management.

### 13. Repository

**GitHub Repository:**

https://github.com/AshishGaikar/cloud-native-devops-activity-2
