pipeline {
  agent any
  stages {
    stage('git pull') {
      steps {
        // https://github.com/kyeahi/Walker will replace by sed command before RUN
        git url: 'https://github.com/kyeahi/Walker.git', branch: 'main'
      }
    }
    stage('k8s deploy'){
      steps {
        kubernetesDeploy(kubeconfigId: 'kubeconfig',
                         configs: '*.yaml')
      }
    }    
  }
}
