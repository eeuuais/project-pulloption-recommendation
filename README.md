<h1 align="center"> AI기반 헬시 푸드 추천서비스 Pull-Option </h1>
<h5 align="center"> Created by : Soyeon Sohn<br>
Created at : 10/22/2022<br>
Updated at : 10/22/2022</h5>

![------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<img width="100%" src="https://github.com/eeuuais/proj_pulloption/assets/98333290/21384f46-1bef-4982-b672-b40b6638f544"/>

<p align="justify"> 
  
## 1. 프로젝트 개요

- 프로젝트명 : AI기반 헬시 푸드 추천서비스 <Pull-Option>
- 수행기간 : 2022년 10월 ~ 11월 (약 6주)
- 개인/팀 과제 여부 : 4인 팀 프로젝트
- 수행 역할 : 데이터 수집, 음식점 추천모델 제작, PPT제작

## 2. 프로젝트 소개

- 제안 배경
  - 프로젝트 시작 전 자체적으로 진행한 223명의 무작위 대상 앱 수요설문조사 결과, 응답자의 87% 이상이 건강을 위해 음식의 재료를 신경쓴다고 답변하였다. 건강한 식재료를 사용하는 식당을 추천해주는 앱 서비스를 제안하고자 한다.
- 프로젝트 목표
  - 해당 서비스의 사용자는 1) 식당 정보 제공으로 소상공인을 지원하려는 지자체, 2) 요식업 서비스 플랫폼 및 소상공인, 3) 원하는 식재료 옵션이 있는 식당을 찾고자 하는 고객으로 한다.
  - 기존 시장의 비슷한 앱서비스들과는 달리 까다로운 개인 건강진단, 유전자 검사 없이 개인 맞춤형 식당을 추천하고, 지금 사용자의 기분, 사용자가 좋아하는 식재료를 기반으로 식당을 추천해주는 큐레이션 제공하는 앱 서비스를 기획하는 것을 목표로 한다.
- 프로젝트 결과물 : 사용자의 셀카로 오늘의 기분에 따른 음식점 추천, 음식재료를 촬영하여 해당 재료를 사용한 건강한 식당을 추천해주는 모바일 앱 서비스 <PULL OPTION>. 서비스명은 ‘입맛 당기는 선택지’라는 의미이다.

## 3. 프로젝트 상세

- 진행방식 : 크게 식재료와 사람의 감정을 분류하는 이미지 분류 모델과, 식재료와 사람의 감정(기분)을 기반으로 음식점을 추천하는 추천 시스템 모델링으로 나누어 진행한다.

### 3-1. 이미지 분류 모델 :

- 데이터 수집 :
  1) Fruits and Vegetables Image Recognition Dataset, Kaggle
      - 총 50가지 과일, 채소류 jpg & jpeg image files
      - https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition

  2) Fruits and Vegetables Images, web crawling
       - '공포', '행복' 등 총 7가지 감정 표정 jpg & jpeg image files
       - https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition

- 데이터 전처리
    - tensorflow에서 인식 불가능한 알 수 없는 확장자 이미지 제거
    - image re-sizing, normalization : input image re-sizing, RGB value를 0~1사이로 정규화
    - image augmentation : 과적합으로 발생하는 generalization error를 줄이고자 이미지를 다각도로 복제

- 데이터 모델링
    - 자체적으로 제작하여 비교적 간단히 구성된 custom layer, 널리 알려져있는 AlexNet, VGGNet 총 3가지 알고리즘을 실험. Custom → AlexNet → VGGNet 순으로 layer가 깊은 특징을 가진다.
    - 결과적으로 비교적 심플하게 구성된 custom layer에서 과일 채소 & 표정 감정 이미지 분석 시 약 98% train accuracy 와 65% validation accuracy를 획득하였으며, 나머지 알고리즘에서는 좋은 결과를 얻지 못했다.
    - AlexNet과 VGGNet은 노트북으로 연산하기에 시간과 리소스가 많이 들어서 레이어를 다소 생략하였는데, 이 생략 부분에 의해 좋지 못한 결과를 얻었다.

- 데이터 모델링 결과
    - 스타푸르트 이미지 입력시 99.65%의 신뢰성으로 '스타푸르트’라는 예측 결과를 나타낸다. 
    - 공포에 떨고 있는 엑스맨 로건 캐릭터 이미지 입력 시, 100%의 신뢰성으로 '공포'라는 예측 결과를 나타낸다.

### 3-2. 추천 시스템 구현 :
- 아이템기반 협업 필터링 기법 사용. 추천 대상과 다른 아이템의 유사도를 측정하여 사용자가 선호하는 아이템에 대해 높게 평가한 사용자에게 추천 대상을 추천하는 기법

- 데이터 수집 : 아래 세 종류의 데이터를 수집하여 음식점 상호명, 분류카테고리, 법정동명, 위도, 경도, 네이버 별점, 리뷰 텍스트 등의 정보를 분석을 위한 파라미터로 구성.
  1) 공공데이터포털 : 소상공인시장진흥공단_상가(상권)정보
     - 음식점 리스트 정보
     - https://www.data.go.kr/data/15083033/fileData.do
    
  2) 농림수산식품교육문화정보원 레시피 재료정보 Open API
     - 레시피 재료정보 오픈 API
     - https://www.data.go.kr/data/15058981/openapi.do
    
  3) 네이버 플레이스 데이터 크롤링 (블로그 리뷰, 별점 데이터 등)
     - 알고리즘 정확도를 위해 사용자별 음식점 별점, 리뷰 등의 정보를 수집하기 위해 네이버 플레이스의 점별 평점, 방문자리뷰, 블로그리뷰 등의 정보를 크롤링
     - https://m.place.naver.com/restaurant/

- 데이터 전처리
    - 불필요 컬럼 제거 : 분류코드, 건물정보, 우편번호, 지번 등 본 분석에 불필요한 데이터값 제거
    - 컬럼명 수정 및 결측값 처리 : 코드 구현 편의를 위해 컬럼명을 수정하여 컬럼명 가독성을 높임. 카테고리 데이터의 일부에 결측치가 발생하여 처리
    - 파생 변수 추가 : 음식점 카테고리 분류, 상호명 등을 조합하여 "키워드리스트"라는 파생 변수를 추가하였고, 이를 유사도 계산에 활용하여 분석 효율성 도모
  
- 데이터 모델링
  - 음식재료 기반 추천 모델
    - 키워드 리스트와 리뷰 데이터 벡터화
      - 텍스트 피처 벡터라이징 : CountVectorizer()
    - 각각의 코사인 유사도 결과 저장
      - 사이킷런 cosine_similarity()
      - 키워드리스트, 리뷰 텍스트 각각 수행
    - 재료기반 음식점 리스트 추출 : 음식 재료를 입력받았을 때 후보 음식점을 도출. 코사인 유사도, 협업필터링, 딥러닝 등 다양한 알고리즘 모델링 시도.
    - 최종 알고리즘 생성 : 카테고리 유사도, 블로그 리뷰 유사도, 별점, 리뷰 수를 종합하여 가중치를 주면서 최종 알고리즘 구현

  - 사용자 감정상태 기반 추천 모델
      - 감정 상태 입력 받기
      - 감정에 대응하는 음식점 리스트 추출
        - 감정, 음식점 키워드리스트 매핑
        - 사전 설문조사 결과를 토대로 감정별 음식 취향 카테고리 선정 후 알고리즘 수행
      - <재료 기반 음식점 추천 모델>과 동일한 과정 수행
      - 리스트업된 정보를 통합하여 하나의 인풋데이터셋을 생성하고,  모델링을 수행
      - 생성된 모델들과 데이터에서 뽑은 기초통계(EDA)자료를 종합하여 적절한 가중치를 주며 최종 모델을 생성

- 데이터 모델링 결과
  - 음식재료 기반 추천 모델 : '닭'을 입력하면, 닭을 재료로 하는 음식점 리스트를 뽑고, 알고리즘에 의해 추천된 음식점 return
  - 사용자 감정상태 기반 추천 모델 : 추천된 결과를 보면 일부 업종의 편향성이 보이는데, 이는 사용한 데이터의 부족과 부정확성에 기인한 것으로 판단되며, 크롤링 오류 개선, 데이터의 추가확보 등의 작업으로 개선 가능할 것으로 예상된다.

## 4. 프로젝트 insight
- **프로젝트 의의**
  - 기존 시장의 여러가지 app을 통해 예약, 배달, 추천 서비스를 따로 각각 이용해오던 소상공인들은 기존 서비스들을 all-in-one 으로 이용가능
  - 지차제는 지역주민을 대상으로 한 적극적인 건강 분위기 조성으로 지역발전에 기여할 수 있으며, 소상공인 지원사업을 효과적으로 진행가능
  - 일반 사용자들은 건강한 식당을 손쉽게 추천받을 수 있을 뿐 아니라, 건강에 특화된 커뮤니티 참여로 더 나은 삶의 질을 도모 가능

- **what I learned**
  - tensorflow 프레임워크로 추천시스템 개발 경험 :
    - 코사인 유사도를 활용하면서 해당 알고리즘을 사용하면 유사한 단어들은 1점에 가까워지고, 관련성 없는 단어들은 0점에 수렴하게 된다는 점과 피쳐 벡터화를 거치면 0~1 사이의 직관적인 점수화가 가능해져 결과적으로 텍스트를 기반으로 가장 쉽게 "비슷함"의 정도를 파악할 수 있다는 점이 공부가 되었다. (구현 시 sklearn 활용)
  - 이미지 분류모델의 판단 기준에 대한 생각 :
    - 이미지 분류 모델에서 학습이 잘 되어 100% 슬픔이라는 결과가 나오는 경우가 있었는데, 얼굴 표정을 보고 감정을 판단하는 것은 "100% 슬픔"이라 판단하는 기준에 주관이 들어있기 때문에 인간에게도 어려운 task이므로, 감정의 판단에 있어 그 경계가 모호하다. 만약 이 task를 실제 비즈니스에서 활용한다고 가정한다면, 판단의 기준을 세우는 것이 어쩌면 프로젝트에서 가장 중요한 업무가 아닐까 하는 생각을 해 보았다. 본 프로젝트에서는 사전 설문조사 결과를 토대로 감정별 음식 취향 카테고리 선정후 알고리즘 수행하였으나, 실제 비즈니스에서는 각 사업부와의 협업을 통한 기준정립이 필수일 것 같다.
