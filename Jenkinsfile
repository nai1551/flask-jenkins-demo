pipeline {

    agent {
        label 'worker-agent'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out application source code...'

                checkout scm
            }
        }

        stage('Verify Worker') {
            steps {
                echo 'Checking Jenkins worker...'

                sh '''
                    echo "Hostname:"
                    hostname

                    echo "User:"
                    whoami

                    echo "Working Directory:"
                    pwd
                '''
            }
        }

        stage('Verify Python') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    rm -rf venv
                    python3 -m venv venv

                    . venv/bin/activate

                    python --version
                    pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    . venv/bin/activate

                    python -c "from app import app; print('Flask application import: OK')"
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    . venv/bin/activate

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
                    echo "Application is running on port 5000"

                    echo "Server IP addresses:"
                    hostname -I

                    echo "Application URL:"
                    echo "http://$(hostname -I | awk '{print $1}'):5000"
                '''
            }
        }
    }

    post {

        success {
            echo '===================================='
            echo 'DEPLOYMENT SUCCESSFUL!'
            echo 'Flask application is running.'
            echo '===================================='
        }

        failure {
            echo '===================================='
            echo 'PIPELINE FAILED!'
            echo 'Check the stage logs.'
            echo '===================================='
        }
    }
}
