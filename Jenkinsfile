pipeline {
    agent any
    environment{
        registry = "sanjaybhide1990/flask-docker-app:v2"
        registryCredential = 'jenkins-docker-user'
    }

    stages {
        stage('Checkout'){
            steps{
                echo 'Checkout'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing'
            }
        }
        stage('Build'){
            steps{
                echo 'Build'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploy'
            }
        }
    }
}