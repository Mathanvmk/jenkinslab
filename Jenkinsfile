
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out successfully'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python test.py'
            }
        }

        stage('Build') {
            steps {
                echo 'Build completed successfully!'
            }
        }
    }

    post {
        success {
            echo 'Jenkins Auto Build Successful!'
        }
        failure {
            echo 'Jenkins Build Failed!'
        }
    }
}
