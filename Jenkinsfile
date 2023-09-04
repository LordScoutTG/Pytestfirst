pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.11.5-alpine3.18'
                }
            }
            steps {
                sh 'python -m venv env'
                sh 'pip install -r requirements.txt --user'
                sh 'sbase install chromedriver latest'
                sh 'pytest --alluredir=allure_results ./tests'
            }
        }
    }
}