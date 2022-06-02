pipeline {
  agent any
  stages {
    stage('git scm update') {
      steps {
        git url: 'https://github.com/kyeahi/Walker/tree/main/Django.git', branch: 'main''          
      }          
    }
    stage('docker build and push') {
      steps {
        sh '''
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
