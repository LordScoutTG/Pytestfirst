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
                sh '''venv env -p python3
                        source env/bin/activate
                        pip3 install -r requirements.txt
                        sbase install chromedriver latest
                        pytest --alluredir=allure_results ./tests'''
            }
        }
    }
}