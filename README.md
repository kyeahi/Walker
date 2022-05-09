# Walker 🚶‍♂️🚶‍♀️

## Project Goal
🔹 사람의 걷는 움직임은 각 관절간의 유기적인 연결에 의해 구현됩니다. 이를 세부적으로 각각 모델링하여 구현하기는 거의 불가능하며, 많은 연산량을 필요로 합니다. 해당 프로젝트는 실제 사람의 걷는 영상으로부터 OpenPose 알고리즘을 통해 관절의 움직임을 프레임단위로 추적하고, Unity 환경에서의 모방학습을 거쳐 실제 사람의 거동과 유사한 움직임을 보이는 Walker를 구현하는 것을 목표로 합니다. <br>

🔹 또한, 데이터 플랫폼을 구축하여 모델 학습환경을 분산시켜 더 많은 데이터를 학습시킵니다. 해당 데이터를 시각화 툴을 사용하여 어떠한 데이터가 사용되었는지 등을 상세하게 나타내고자 합니다.<br>
<br>
<p align="center">
<img src="https://user-images.githubusercontent.com/50973139/167372946-186e3669-2fed-4c68-83f9-3f4142b85cef.gif"  width="500" height="300" alt="unity Walker ML-Agent Example"/>
<br>Unity Walker ML-Agent Example</br>
<br></br>
<img src="https://github.com/CMU-Perceptual-Computing-Lab/openpose/raw/master/.github/media/dance_foot.gif" width="500" height="300" alt="OpenPose Example"/>
<br>OpenPose Example</br>
</p>

## Required Skills
<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>

### ● Unity + ML Agent
관절별 움직임을 모방학습 시키기 위한 모델 생성, 영상의 데이터 기반으로 관절 point를 매칭시켜 모방학습 수행 <br>
### ● Pytorch
걷는 움직임 구현에 필요한 관절별 각도, 위치 등 출력을 위한 적합한 모델 설계<br>
### ● Kubernetes
AI의 강화학습과 대용량의 영상 데이터 전처리를 위한 전반적인 분산 데이터 처리 관리<br>
### ● Mysql
SQL 형태로 AI 학습에 사용될 영상, Frame, 관절 point 데이터 관리 및 저장<br>
### ● Jenkins + Github
테스트 환경에 Git 기반 자동 배포, 실행 (추후 서버 환경에 배포)<br>


## Blueprint
