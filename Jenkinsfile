pipeline {
  agent any
  node('builder') {
        stage('Checkout') {
             checkout scm   // gitlab으로부터 소스 다운
        }
        stage('Docker build') {
          steps {
            sh '''
            sudo apt install docker
            docker build -t kube4team/test-django-jk .
            docker push kube4team/test-django-jk:1.0
            '''
          }
        }
        stage('deploy kubernetes'){
          steps {
            sh '''
            kubectl create deployment test-django-pod --image=kube4team/test-django-jk:1.0
            kubectl expose deployment test-django-pod --type=LoadBalancer --name=test-django-pod-svc --port=8000
            '''
          }
        }   
    }
}
