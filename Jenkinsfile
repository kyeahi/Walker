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
            app = docker.build("kube4team/test-django-jk:${env.BUILD_ID}")
            app.push()
            app.push('1.0')
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
