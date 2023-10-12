#데이터 정제 : 이상치와 결측치 처리
#결측치(missing value) : 누락된 값
#is.na()
#na.omit(): NA 결측값이 존재하는 행을 제거
#na.rm = T/F
str(airquality)
table(is.na(airquality))
table(is.na(airquality$Solar.R))
mean(airquality$Temp)
mean(airquality$Ozone)
#Ozon에 결측값이 아닌 관측데이터만 추출
air_narm<-airquality[!is.na(airquality$Ozone),]
mean(air_narm$Ozone)
air_omit<-na.omit(airquality)
mean(air_omit$Ozone)

mean(airquality$Ozone, na.rm=T)

#이상치(outlier)
patients1<-data.frame(name=c('환자1','환자2','환자3','환자4','환자5'), age=c(22,30,41,27,38), gender= c(1,2,1,3,2), blood.type= c(1,3,2,4,5))
str(patients)
# 성별에서 이상치를 제거
patients_omit<-patients[patients$gender=='M'|patients$gender=='F',]
patients_omit

#patients 에서 성별과 혈액형에 이상치를 제거하고 추출
patients_outlier <- patients[(patients$gender=='M'|patients$gender=='F')&(patients$blood.type=='A'|patients$blood.type=='B'|patients$blood.type=='O'|patients$blood.type=='AB'),]

patients1
#성별의 이상치를 결측치 처리
patients1$gender<-ifelse(patients1$gender>2,NA,patients1$gender)
#혈액형의 이상치를 결측치 처리
patients1$blood.type<-ifelse(patients1$gender<1|patients1$gender>4,NA,patients1$blood.type)

#이상치를 판단하기 어려운 데이터의 처리
  boxplot(airquality[,1:4])
boxplot(airquality[,1])$stats  

#Ozone 컬럼에 이상치를 찾아 결측처리
air<-airquality
air$Ozone<-ifelse(air$Ozone<1|air$Ozone>122,NA,air$Ozone)
table(is.na(air$Ozone))

#cars 데이터셋의 dist의 이상치를 제거한 후 dist의 평균을 계산하시오.
#이상치판단은 boxplot을 이용할것
str(cars)
boxplot(cars[,2])$stats
cars1<-ifelse(cars$dist<2|cars$dist>93,NA,cars$dist)
mean(cars1,na.rm=T)
