```groovy
pipeline {

    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out flask-jenkins-demo...'
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh '''
                    echo "===== Python ====="
                    python3 --version

                    echo "===== Pip ====="
                    pip3 --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "===== Creating Virtual Environment ====="

                    rm -rf venv
                    python3 -m venv venv

                    . venv/bin/activate

                    echo "===== Python inside venv ====="
                    python --version

                    echo "===== Pip inside venv ====="
                    pip --version

                    echo "===== Installing Dependencies ====="
                    pip install --upgrade pip

                    pip install -r requirements.txt

                    echo "===== Installing Pytest ====="
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate

                    echo "===== Running Tests ====="

                    python -m pytest -v
                '''
            }
        }

        stage('Test Application Import') {
            steps {
                sh '''
                    . venv/bin/activate

                    echo "===== Testing Flask Application ====="

                    python -c "from app import app; print('Flask application import: OK')"
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    . venv/bin/activate

                    echo "===== Starting Flask Application ====="

                    pkill -f "python app.py" || true

                    nohup python app.py > flask.log 2>&1 &

                    sleep 5

                    echo "===== Flask Log ====="
                    cat flask.log

                    echo "===== Health Check ====="

                    curl http://localhost:5000/health
                '''
            }
        }

        stage('Show Application') {
            steps {
                sh '''
                    echo "===================================="
                    echo "Flask Application is Running"
                    echo "===================================="

                    echo "Server IP:"
                    hostname -I

                    echo "Port:"
                    echo "5000"

                    echo "Application URL:"
                    echo "http://$(hostname -I | awk '{print $1}'):5000"

                    echo "Health URL:"
                    echo "http://$(hostname -I | awk '{print $1}'):5000/health"
                '''
            }
        }
    }

    post {

        success {
            echo '===================================='
            echo 'PIPELINE SUCCESSFUL!'
            echo 'Flask application deployed.'
            echo '===================================='
        }

        failure {
            echo '===================================='
            echo 'PIPELINE FAILED!'
            echo 'Check the failed stage.'
            echo '===================================='
        }
    }
}
```
