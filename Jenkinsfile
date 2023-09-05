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
                sh '''python -m venv env
                        pip3 install -r requirements.txt --user
                        sbase install chromedriver latest
                        pytest --alluredir=allure_results ./tests'''
            }
        }
    }
}