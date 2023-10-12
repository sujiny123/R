#복지패널 데이터를 이용한 데이터 분석

raw<- read.spss(file="C:/k_digital/r/source/Day006/Koweps_hpc10_2015_beta1.sav", to.data.frame=T)
welfare<-raw
dim(welfare)
str(welfare)
welfare<-rename(welfare,
       gender=h10_g3,
       year=h10_g4,
       marriage=h10_g10,
       religion=h10_g11,
       code_job=h10_eco9,
       income=p1002_8aq1,
       code_region=h10_reg7)
#1. 성별에 따른 급여의 차이는 있을까?
table(welfare$gender)
welfare$gender<-ifelse(welfare$gender==1,'M','F')
table(welfare$gender)
summary(welfare$income)
table(welfare$income)
gender_income<-welfare %>%
  filter(!is.na(income)) %>%
  group_by(gender)%>%
  summarise(mean_income=mean(income))
gender_income  
#2. 나이와 급여의 관계는 있을까?
table(welfare$year)
welfare$year<-2015-welfare$year
summary(year)
age_income<- welfare%>%
  filter(!is.na(income)) %>%
  group_by(year) %>%
  summarise(mean_income=mean(income))
head(age_income,10)
ggplot(age_income,aes(x=year,y=mean_income)) + geom_line()
#3. 연령대에 따른 급여의 차이는 있을까?
# 연령대 : 청소년(30세미만)-young, 중장년(60세미만)-middle, 노년-old
welfare$gen<-ifelse(welfare$year<30,'young',ifelse(welfare$year<60,'middle','old'))
table(welfare$gen)
ages_income <-  welfare %>%
  filter(!is.na(income)) %>%
  group_by(gen) %>%
  summarise(mean_income=mean(income))
ages_income
ggplot(ages_income,aes(x=gen,y=mean_income)) + geom_point()

#엑셀파일에서 특정시트에 있는 내용을 불러오는 작업
jobList<- read_excel("C:/k_digital/r/source/Day006/Koweps_Codebook.xlsx", sheet=2, col_names = T)
head(jobList)
str(jobList)
#welfare 데이터프레임에 열추가, 하나의 데이터프레임으로 합치는 작업
welfare<-left_join(welfare,jobList,by='code_job')
names(welfare)
job_male <- welfare %>%
  filter(!is.na(job.x) & gender=="M") %>%
  group_by(job.x) %>%
  summarise(n=n()) %>%
  arrange(desc(n)) %>%
  head(10)

