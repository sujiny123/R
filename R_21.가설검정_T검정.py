#t-test : 두그룹 간의 평균 비교
#정규성확인 및 검정
#등분산성 검정

#단일 표본 t-test(one sample t-test) : 특정 그룹의 평균이 특정값과 같은지 비교
#독립 표본 t-test(two sample t-test) : 서로 다른 두 그룹간의 평균을 비교
#대응 표본 t-test(paired t-test) : 한 그룹내에서 동일한 대상을 반복 측정해서 전과 후의 평균을 비교

names(row)

# 추출할 변수 : id, 성별, 나이, 당뇨병유무(19세이상), 인슐린 주사, 공복혈당, 당화혈색소 
vars<- c('ID','sex','age','HE_DM','DE1_31','HE_glu','HE_HbA1c')
row<-read.spss('C:/k_digital/r/source/Day009/HN18_ALL.sav', to.data.frame = T)
names(row)
data_f<-select(row,vars)

#데이터 확인
head(data_f,10)
#변수별 결측치 확인
introduce(data_f)

#결측치 제거
data_f<-na.omit(data_f)
head(data_f,10)

#가설 : 당뇨환자에서 인슐린 투여군과 비투여군의 혈당에 차이가 있다.
#당뇨병 유병유무(19세이상):1(정상),2(공복혈당장애),3(당뇨병)
#재분류 : 1.정상 2. 공복혈당장애 -> 정상(0) 3.당뇨병-> 당뇨병(1)

data_f$HE_DM2<-ifelse(data_f$HE_DM==3,1,0)

#인슐린 투여 DE1_31
#0(아니오),1(예),8(비해당),9(모름)
#필요대상 추출
data_subj<-subset(data_f,data_f$HE_DM2==1 & data_f$DE1_31==0| data_f$DE1_31==1)
#최종대상자수
nrow(data_subj)
#데이터확인
head(data_subj, 10)

#t검정 수행시 사전에 정규성을 띄고 있어야 한다는 전제 조건
#시각적인 방법(히스토그램)과 통계량을 이용하는 방법
#histogram
hist(data_subj$HE_glu, freq=F, ylim=c(0,0.02), xlab='He_glu(공복혈당)')
#dernel density plot
lines(density(data_subj$HE_glu),col='blue',lwd=2)
#Q-Q plot
qqnorm(data_subj$HE_glu, col='blue')
qqline(data_subj$HE_glu,col='red',lwd=2)

#Shapiro-Wilk test : 정규성 검정
#귀무가설(H0) : 정규분포를 따른다.
#대립가설(H1, 연구가설) : 정규분포를 따르지 않는다.
shapiro.test(data_subj$HE_glu)
#p-value<0.05, 귀무가설 기각, 정규분포를 따르지 않는다.
#shapiro 검정은 표본크기가 5000 넘는 경우 오류 발생

#Kolmogorov-Smirnov test
ks.test(data_subj$HE_glu, y='pnorm', alternative = 'two.sided')

#등분산성 검정
#귀무가설 : 두그룹의 분산은 차이가 없다.
#대립가설 : 두그룹의 분산은 차이가 있다.
var.test(data_subj$HE_glu~data_subj$DE1_31)

#데이터 분석 결과
#정규분포를 따르지 않고, 인슐린 그룹간 분산이 다르다.
t.test(data_subj$HE_glu~data_subj$DE1_31,paired=F,var.equal=F, conf.level=0.95)

#p-value =0.1676, 인슐린 투여 여부에 따라 공복혈당이 다르지 않다고 할 수 있다.

#일원배치 분산분석(one-way ANOVA)
# 세개 이상의 집단간의 평균의 차이가 통계적으로 유의미한지 비교할때 사용
#가정 : 정규성, 등분산성, 독립성
#귀무가설 : 모든 모집단의 평균은 동일하다.
#대립가설 : 모든 모집단의 평균은 동일하지 않다.

study<-read.csv('C:/k_digital/r/source/Day009/ANOVA 예제.csv', header=T)
#정규성확인
shapiro.test(subset(study, group=='A')$time)
shapiro.test(subset(study, group=='B')$time)
shapiro.test(subset(study, group=='C')$time)
#결론 : 모든그룹의 p-value>0.05 이므로 귀무가설 채택

#등분산성확인
install.packages('lawstat')
library(lawstat)
levene.test(study$time, study$group, location = "mean")
#p-value=0.801>0.05 귀무가설 채택, 등분산

#ANOVA
result<-aov(time~group, data=study)
result
summary(result)
#p-value<0.05, 귀무가설 기각
#세 고등학교의 학생들의 평균 공부시간은 유의미한 차이가있다.
