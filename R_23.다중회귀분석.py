#보스턴 집값 예측 : 회귀 분석(선형회귀분석)
data("Boston")

#해당 데이터셋을 파일로 저장
write.csv(Boston,file='boston.csv', row.names = T)
df<-read.csv('C:/k_digital/r/source/Day009/boston.csv',header = T,stringsAsFactors = F)
#종속변수에 해당하는 medv(집값)을 제외하고 데이터 추출
df<-df[,-1]

#변수의 의미
#crim : 1인당 범죄율
#zn : 25000초과하는 거주지역의 비율
#indus : 비상업지역이 점유하고 있는 토지의 비율
#chas : 찰스강 경계 1, 아니면 0
# nox : 10ppm당 일산화질소
#rm : 평균 방의 개수
#age : 1940년 이전에 건축된 소유주택의 비율
#dis : 직업센터까지의 접근성의 지수
#rad : 방사형 도로까지의 접근성지수 - 도시고속도로
#tax : 재산세율
#ptratio : 학생과 교사의 비율
#black : 흑인의 비율
#lstat : 저소득층 비율
#medv : 주택가격(단위1000)

#기술통계량
install.packages('Hmisc')
summary(medv~crim+zn,data=df)
library(Hmisc)
describe(df)
#결측치확인
df[complete.cases(df),]
head(df,10)
df<-na.omit(df)
#결측치 대체
df$crim[is.na(df$crim)]<-0

install.packages('DMwR')
mean_crim<-mean(df$crim)

#데이터 분할 - 학습, 성능평가
#랜덤 샘플링
df_idx<-sample(1:506,300)
df_train<-df[df_idx,]
df_test<-df[-df_idx,]

nrow(df_train)
nrow(df_test)

#다중회귀분석
result<-lm(medv~.,data=df_train)
summary(result)

#다중공선성 : 독립 변수들 간의 지나친 상관관계가 존재
#팽창지수
install.packages('car')
library(car)
vif(result) #10이상이면 다중공선성이 발생했다고 간주
