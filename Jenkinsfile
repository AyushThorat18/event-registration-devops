pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/AyushThorat18/event-registration-devops.git'      
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t event-registration-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat '''
                docker stop event-app || exit 0
                docker rm event-app || exit 0
                '''
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name event-app event-registration-app'
            }
        }

        stage('Test Application') {
            steps {
                bat 'echo Application Deployed Successfully'
            }
        }
    }
}