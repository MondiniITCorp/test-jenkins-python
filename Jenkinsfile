pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'pip3 install python-docx reportlab'
        sh 'python3 hello.py'
      }
    }
  }
}