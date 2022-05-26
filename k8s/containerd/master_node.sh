## CNI로 calico 를 사용

kubeadm init --token 123456.1234567890123456 --token-ttl 0 \
--apiserver-cert-extra-sans=192.168.56.100 \ --control-plane-endpoint=192.168.56.100:6443

# config for master node only 
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

# config for kubernetes's network 
curl https://docs.projectcalico.org/manifests/calico.yaml -O
kubectl apply -f calico.yaml
