# Walker 🚶‍♂️🚶‍♀️ / 사람처럼 걷는 모델 학습하기 / MLOps
* 프로젝트 기간: 22/05/09 ~ 22/06/10
asdfasdf
## Project Goal
🔹 해당 프로젝트는 실제 사람의 걷는 영상으로부터 **OpenPose 알고리즘을 통해 관절의 움직임을 프레임단위로 추적**하고, **Unity 환경에서의 모방학습을 거쳐 실제 사람의 거동과 유사한 움직임을 보이는 Walker를 구현하는 것을 목표**로 합니다. <br>

🔹 사람의 걷는 움직임은 각 관절간의 유기적인 연결에 의해 구현됩니다. 이를 세부적으로 각각 모델링하여 구현하기는 거의 불가능하며, 많은 연산량을 필요로 합니다. 그렇기 때문에, 데이터 플랫폼을 구축하여 모델 학습환경을 분산시켜 더 많은 데이터를 학습합니다.  <br>

🔹 또한, 쿠버네티스 클러스터링을 통해 효과적으로 컨테이너를 관리합니다. 


<br>
<p align="center">
<img src="https://user-images.githubusercontent.com/50973139/167372946-186e3669-2fed-4c68-83f9-3f4142b85cef.gif"  width="500" height="300" alt="unity Walker ML-Agent Example"/>
<br>Unity Walker ML-Agent Example</br>
<br></br>
<img src="https://github.com/CMU-Perceptual-Computing-Lab/openpose/raw/master/.github/media/dance_foot.gif" width="500" height="300" alt="OpenPose Example"/>
<br>OpenPose Example</br>
</p>

## Required Skills

### Backend
* Django   
* Unity  

### DB  
* Hadoop  
* AWS S3  

### Frontend  
* Unity   
  
### ML  
* Openpose  
* Tensorflow  
* Pytorch  
* Unity  

### Platform  
* Docker  
* Kubernetes   
* Kafka  
* Spark  
* Helm  
* Prometheus  

### CI/CD  
* Github  
* Jenkins  
* Helm  
* Zookeeper  




## Blueprint
● 아키텍처

![Screenshot from 2022-05-31 12-02-24](https://user-images.githubusercontent.com/97927143/171084710-52db38dc-1f16-4e06-a49b-819abe16f4fe.png)

## Team members
|팀원|담당 파트|역할|
|------|---|---|
|김빛가람|플랫폼|Docker, Kubernetes 환경구축|
|김세진|플랫폼|Docker, Kubernetes 환경구축|
|김예빈|플랫폼|DB 관리, 데이터 송수신|
|안현동|백앤드 및 플랫폼|데이터 전처리, 데이터 파이프라인 구축|
|장서현|인공지능|-|



## Schedule
* [백앤드 개발일지](https://github.com/kyeahi/Walker/blob/main/%EB%B0%B1%EC%97%94%EB%93%9C_%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%80.md)<br>
* [플랫폼 개발일지](https://github.com/kyeahi/Walker/blob/main/%ED%94%8C%EB%9E%AB%ED%8F%BC_%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%80.md)
