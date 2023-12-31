#R을 이용한 통계분석 : 기술통계분석과 추론통계분석

#수치형자료를 분석하는 작업 : 기술통계량

x <- c(
  64, 84, 82, 81, 68, 85, 76, 89, 93,
  77, 66, 64, 86, 74, 64, 70, 53, 98, 
  59, 79, 57, 59, 65, 67, 80)

#평균
mean(x)

#중앙값
median(x)

#최소값,최대값
min(x)
max(x)

storeA <- c(20,21,23,22,26,28,35,35,41,42,43,45,44,45,46,47,47,46,47,58,58,59,60,56,57,57,80)
storeB<- c(5,6,11,13,15,16,20,20,21,23,22,27,27,30,30,32,36,37,37,40,40,43,44,45,51,54,70,600)
storeC<-c (5,5,5,12,10,11,20,20,20,20,20,21,20,30,32,31,31,31,36,40,40,51,61,51,61,61,70)
#A,B,C식당의 배달시간을 이용해서 가장 빠른 배달을 하는 식당을 찾는 작업
#A와 B 비교해서 가장 빠르게 배달하는 식당은?
mean(storeA)
mean(storeB)

median(storeA)
median(storeB)

quantile(storeA)
quantile(storeB)
#boxplot으로 이상치 찾아내기
boxplot(storeB)
boxplot(storeA,storeB,names=c('A식당','B식당'))
#B식당의 이상치를 제거한 후 배달시간
storeB<-storeB[storeB<600]
boxplot(storeB)
points(c(mean(storeA),mean(storeB)),pch=2, col='red',cex=2)
mean(storeC)
mean(storeB)

quantile(storeB)
quantile(storeC)

boxplot(storeB,storeC)

#구간별 데이터의 분포를 확인하는 시각화도구
#히스토그램 : 연속형데이터
#막대그래프 : 이산형데이터(범주형데이터)

hist(storeB,main='B식당 배달시간',xlab='배달시간구간',ylab='배달건수')
hist(storeC,main='C식당 배달시간', xlab='배달시간구간', ylab='배달건수')

# 분산과 표준편차
# 첨도와 왜도

var(storeB)
var(storeC)

sd(storeB)
sd(storeC)

#B식당>C식당>A식당

#범주형 데이터의 분석 : 파이차트, 막대그래프
bloodType <- c('A','B','A','AB','O','A','O','B','A','O','O','B','O','A','AB','B','O','A','A','B')

#도수분포표
table(bloodType)

#pie(데이터,범주명,col,lty,main)
pie(table(bloodType), labels= c('A형','AB형','B형','O형'), lty=2, col=heat.colors(4), main='우리반 혈액형 분포도')

addmargins(table(bloodType))

#막대차트 barplot(height, names.arg, space, horiz=T/F, main, xlab, ylab, col, beside, xlim, ylim)
barplot(table(bloodType), names.arg=c('A형','AB형','B형','O형'),main='우리반 혈액형 분포도', xlab='혈액형',ylab='학생수',col=heat.colors(4))

names<-c('aaa','bbb','ccc','ddd','eee','ggg','fff','hhh','iii','jjj','kkk','lll','mmm','nnn','ooo','ppp','qqq','rrr','sss','ttt')
sex <- c('남','여','남','남','여','여','남','여','여','여','여','남','남','남','여','여','남','여','여','여')
classDF<-data.frame(name=names, gender=sex, blood= bloodType)
classDF

classTable<-table(classDF[,2:3])
addmargins(table(classDF[,2:3]))
barplot(classTable,legend=T,ylim=c(0,10), col = heat.colors(2), beside=T)

library(MASS)
MASS::survey
survey<-survey[,c('Sex','Exer','Smoke')]
head(survey)
table(survey$Sex)
table(survey$Exer)
table(survey$Smoke)
xtabs(~Sex,survey)

#교차표 : 둘 이상의 범주형 데이터를 이용해서 빈도와 비율
table(Sex=survey$Sex, Smoke=survey$Smoke)
pie(table(survey$Smoke))
