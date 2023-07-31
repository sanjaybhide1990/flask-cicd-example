/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    environment {
        DOCKERHUB_CREDENTIALS = credentials('jenkins-docker-user')
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t sanjaybhide1990/flask-jenkins-docker-app .'
            }
        }
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push sanjaybhide1990/flask-jenkins-docker-app'
            }
        }
        post {
            always {
                sh 'docker logout | true'
            }
        }
    }
}
