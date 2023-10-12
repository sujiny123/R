#추론통계분석 : 가설검정
#A학원에 수강하면 성적에 도움이 되느냐?
before_study <- c(34,76,76,63,73,75,67,78,81,53,58,81,77,80,43,65,76,63,54,64,85,54,70,71,71,55,40,78,76,100,51,93,64,42,63,61,82,67,98,59,63,84,50,67,80,83,66,86,57,48)

#학원을 다닌 후 성적
after_study <- c(74,87,89,98,65,82,70,70,70,84,56,76,72,69,73,61,83,82,89,75,48,72,80,66,82,71,49,54,70,65,74,63,65,101,82,75,62,83,90,76,87,90,78,63,59,79,74,65,77,74)

# boxplot 비교
boxplot(before_study,after_study,names=c('수강전','수강후'))

#t-검정 : 집단간의 차이를 검증하는 도구, t-test()
#t.test(x,y,paired=T/F,var.equal=T/F, alternative=양측검정,단측검정)
#paired = T, 대응표본, 한 집단으로부터 두번 반복해 샘플을 추출
#paired = F, 독립표본, 서로 독립된 집단에서 각각 샘플을 추출
#alternative = 'two.sided' 두집단이 서로 같은지 비교
#alternative = 'less' A less than B, A가 B보다 작은지 비교
#alternative = 'greater' A greater than B, A가 B보다 큰지 비교
#반드시 한 가지의 가정이 선행되어야 한다. - 정규분포
#샘플수가 30개 미만이면 정규분포 여부를 반드시 확인해야한다.
#동일집단을 대상으로 하는 대응표본
t.test(before_study,after_study,paired=T)
#p-value<0.05, 대립가설이 채택
t.test(before_study,after_study,paired=T,alternative = 'greater')
#대립가설 : 두집단의 평균의 차가 0보다 크다
#p-value>0.05, 대립가설 기각 -> 수강후 성적이 떨어졌다는것은 기각한다.
#A회사의 건전지 수명시간이 1000시간일때
#귀무가설 : 건전지의 수명시간은 1000시간이다.
#대립가설 : 건전지의 수명시간은 1000시간이 아니다.
a<-c(980,1003,963,1032,1012,1002,996,1102,1017,1003)
#정규분포 여부를 확인 : Shapiro-wilk 검정
#귀무가설 : 정규분포를 따른다.
#대립가설 : 정규분포를 따르지 않는다.
shapiro.test(a)
#p-value>0.05 이기 때문에 귀무가설 채택

t.test(a,mu=1000,alternative='two.sided')
#결론 : 건전지의 평균수명시간은 1000시간이다.

#수학평균점수가 55점이다.
#0교시 수업후 학생들의 성적이 올랐다고 할 수 있는지
#귀무가설 : 오르지 않았다.
#대립가설 : 성적이 올랐다.
#0교시후 학생들의 수학점수
score<-c(58,49,39,99,32,88,62,30,55,65,44,55,57,53,33,42,39)

#피셔검정(Fisher's exact Test) : 표본수가 적거나 데이터의 분포가 치우진 경우에 적용
# fisher.test(data)
#정수기회사의 직원채용 분석 - 몇명의 AS기사 채용이 필요한지 분석
purifier_df<- read.table(file='clipboard', header=T, sep='\t',stringsAsFactors = T)

#데이터 구조 확인
str(purifier_df)
#purifier : 총 정수기 대여수(전월)
#old_purifier : 10년이상 노후된 정수기 대여수(전월)
#as_time : AS소요시간(당월)

#상관관계 : 총 정수기 대여수와 AS시간의 상관관계
plot(purifier_df$purifier,purifier_df$as_time, xlab='총정수기대여수',ylab='as시간')
#상관관계 : 10년이상 노후된정수기의 대여수와 AS시간의 상관관계
plot(purifier_df$old_purifier,purifier_df$as_time, xlab='노후정수기대여수',ylab='as시간')

#수치데이터의 기초통계량
summary(purifier_df)

#독립변수 : 정수기 총 대여수-노후된 정수기의 총 대여수
#종속변수 : AS시간
#파생변수 : young_purifier
purifier_df$Y_purifier<-purifier_df$purifier-purifier_df$old_purifier
lm_result<-lm(as_time~Y_purifier+old_purifier,purifier_df)
lm_result
summary(lm_result)
#AS시간 = 0.0881*10년미만 +0.23977*10년이상 +193.73664
#예측
input_predict<-data.frame(Y_purifier=230000,old_purifier=70000)
result<-predict(lm_result,input_predict)
result
#구간추정
result<-predict(lm_result, input_predict, interval = 'confidence',level=0.95)
result

#상관계수 : 피어슨 상관계수, 스피어만 상관계수
cor(purifier_df$purifier,purifier_df$as_time)
cor(purifier_df$old_purifier,purifier_df$as_time)

#상관분석
#구내식당 음식값이 매출에 미치는 영향을 분석
#귀무가설 : 상관관계가 없다.
#대립가설 : 상관관계가 있다.
x<-c(70,72,62,64,71,76,0,65,74,72)
y<-c(70,74,65,68,72,74,61,66,76,75)
cor.test(x,y,method='pearson')

#R base 내장데이터 women
str(women)
plot(women$height, women$weight)
#상관계수
cor(women$height,women$weight)

#회귀분석 : 독립변수와 종속변수
#체중=3.45*신장 -87.52
#종속변수 ~ 독립변수
model<-lm(women$weight~women$height)
model
#신장이 180인 사람의 체중은 얼마인가?
model$coefficients[[2]]*180 + model$coefficients[[1]]

summary(model)
plot(women$height,women$weight)
#회귀선
abline(model)

#자동차의 속도와 제동거리 데이터 셋 cars
str(cars)
plot(cars$speed,cars$dist)
cor(cars$speed,cars$dist)
#lm(formula, data)
#제동거리 ~ 속도 + 타이어면적
head(cars,10)
#차속도에 따른 제동거리 확인하는 회귀분석
model<-lm(dist~speed,cars)
model
#회귀방정식
#제동거리=3.9324*speed-17.5791
summary(model)
abline(model)
#회귀분석의 모델의 평가 요소
#독립변수의 유의성, 모델의 정확도, 오차항의 정규성

#가로2,세로2
par(mfrow=c(2,2))
plot(model)

#예측 : 새로운 독립변수를 대입해서 종속변수의 값을 확인
#점 추정과 구간 추정
#predict(model,data,intrval,level)
model<-lm(dist~speed,cars)

#독립변수에 여러값을 담아 예측
speed<-c(50,60,70,80,90,100)
new_input<-data.frame(speed)
new_input
#예측 - 점추정
result<-predict(model,new_input)
str(result)
cbind(new_input,result)

#예측 - 구간추정
#interval='confidence' : 모델계수의 불확실성을 감안한 구간 추정
#interval='prediction' : 모델계수의 불확실성과 결과의 오차를 감안한 구간추정
result<-predict(model, new_input, interval = 'confidence',level=0.95)
result
