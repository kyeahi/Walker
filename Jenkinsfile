def DOCKER_IMAGE_NAME = "kube4team/test-django-jk"           
def DOCKER_IMAGE_TAGS = "1.0" 

podTemplate(label: 'builder',
            containers: [
                containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
                containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.19.16', command: 'cat', ttyEnabled: true)
            ],
            volumes: [
                hostPathVolume(mountPath: '/home/jenkins/config', hostPath: '/home/k8s/django'),
                hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
            ]) {
    node('builder') {
        stage('Checkout') {
            checkout scm
        }
        stage('Docker build') {
            container('docker') {
                withCredentials([usernamePassword(
                    credentialsId: '87f23b01-e4f1-496d-9071-00f1441d99a0',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD')]) {
                        
                        sh "ls -al /home/jenkins/config/"
                        sh "cp /home/jenkins/config/.env ./.env"
                        sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAGS} ."
                        sh "docker login -u ${USERNAME} -p ${PASSWORD}"
                        sh "docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAGS}"
                    
                    }
            }
        }
        stage('Run kubectl') {
            container('kubectl') {
                withCredentials([usernamePassword(
                    credentialsId: '87f23b01-e4f1-496d-9071-00f1441d99a0',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD')]) {
                            
                        sh "echo ${DATE}"
                        sh "sed -i.bak 's#DATE_STRING#${DATE}#' ./deployment.yaml"
                        sh "kubectl apply -f ./deployment.yaml"
                            
                    }  
            }
        }
    }
}
