def DOCKER_IMAGE_NAME = "kube4team/MLops-main"           // 생성하는 Docker image 이름
def DOCKER_IMAGE_TAGS = "0.2"       // 생성하는 Docker image 태그
def NAMESPACE = "default"
def VERSION = "${env.BUILD_NUMBER}"
def DATE = new Date();

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
             checkout scm   // gitlab으로부터 소스 다운
        }
        stage('Docker build') {
            container('docker') {
                withCredentials([usernamePassword(
                    credentialsId: 'docker_hub_auth',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD')]) {

                        sh "ls -al"
                        sh "ls -al /home/jenkins/config/"
                        sh "cp /home/jenkins/config/.env ./.env"
                        sh "ls -al"
                        sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAGS} ."
                        sh "docker login -u ${USERNAME} -p ${PASSWORD}"
                        sh "docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAGS}"
                }
            }
        }
        stage('Run kubectl') {
            container('kubectl') {
                withCredentials([usernamePassword(
                    credentialsId: 'docker_hub_auth',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD')]) {
                        /* namespace 존재여부 확인. 미존재시 namespace 생성 */
                        sh "kubectl get ns ${NAMESPACE}|| kubectl create ns ${NAMESPACE}"

                        /* secret 존재여부 확인. 미존재시 secret 생성 */
                        sh """
                            kubectl get secret my-secret -n ${NAMESPACE} || \
                            kubectl create secret docker-registry my-secret \
                            --docker-server=https://index.docker.io/v1/ \
                            --docker-username=${USERNAME} \
                            --docker-password=${PASSWORD} \
                            --docker-email=kube4team \
                            -n ${NAMESPACE}
                        """
                        /* k8s-deployment.yaml 의 env값을 수정해준다(DATE로). 배포시 수정을 해주지 않으면 변경된 내용이 정상 배포되지 않는다. */
                        /*sh "echo ${VERSION}"
                        sh "sed -i.bak 's#VERSION_STRING#${VERSION}#' ./k8s/k8s-deployment.yaml"*/
                        sh "echo ${DATE}"
                        sh "sed -i.bak 's#DATE_STRING#${DATE}#' ./verymarket-deployment.yaml"

                        /* yaml파일로 배포를 수행한다 */
                        sh "kubectl apply -f ./verymarket-deployment.yaml -n ${NAMESPACE}"
                        sh "kubectl apply -f ./verymarket-service.yaml -n ${NAMESPACE}"
                }
            }
        }
    }
}
