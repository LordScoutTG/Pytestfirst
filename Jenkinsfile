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
                sh '''python -m venv env \n $ sudo pip3 install -r requirements.txt \n sbase install chromedriver latest \n pytest --alluredir=allure_results ./tests'''
            }
        }
    }
}