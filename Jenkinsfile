pipeline {
    agent any

    environment {
        IMAGE_NAME = 'cloud-native-app:1.0'
        CLUSTER_NAME = 'activity2-cluster'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing application dependencies and building Docker image'

                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements-dev.txt
                    python3 -m compileall -q app.py

                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated Python tests'

                sh '''
                    .venv/bin/python -m pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Loading Docker image into KIND'

                sh '''
                    kind load docker-image ${IMAGE_NAME} --name ${CLUSTER_NAME}

                    kubectl apply -f kubernetes/deployment.yaml
                    kubectl apply -f kubernetes/service.yaml

                    kubectl rollout status deployment/cloud-native-deployment --timeout=180s
                    kubectl get pods
                    kubectl get services
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Checkout, build, tests and Kubernetes deployment completed!'
        }

        failure {
            echo 'FAILURE: Check the Jenkins console output.'
        }
    }
}