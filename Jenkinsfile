pipeline {

    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                echo '===== Checking out Flask project ====='
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

                    echo "===== Upgrading pip ====="
                    pip install --upgrade pip

                    echo "===== Installing Project Dependencies ====="
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
                    echo "===== Deploying Flask Application ====="

                    sudo systemctl restart flask-app

                    echo "===== Checking Flask Service ====="

                    sudo systemctl is-active flask-app

                    echo "===== Waiting for Application ====="

                    sleep 3

                    echo "===== Health Check ====="

                    curl -f http://localhost:5000/health

                    echo ""
                    echo "===== Deployment Successful ====="
                '''
            }
        }

        stage('Show Application') {
            steps {
                sh '''
                    echo "========================================"
                    echo "Flask Application is Running"
                    echo "========================================"

                    echo "Worker Hostname:"
                    hostname

                    echo "Worker IP:"
                    hostname -I

                    echo "Application Port:"
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
            echo '''
========================================
PIPELINE SUCCESSFUL!
Flask application deployed successfully.
========================================
'''
        }

        failure {
            echo '''
========================================
PIPELINE FAILED!
Check the failed stage.
========================================
'''
        }
    }
}
