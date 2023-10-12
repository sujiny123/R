#dplyr 패키지 : 데이터 프레임을 핸들링할때 가장 기본적으로 사용되는 함수
#filter(df,x) : 행추출,subset()
#select(df,x,y) : 열추출,df[,c('x','y')]
#mutate(df,z=x+y) : 열추가(파생변수), df$z<-df$x+df$y, transform()
#arrange(df,x) : 정렬, order(), sort()
#distinct(df,x) : unique 행 추출 , unique()
#rename(df,y=x) : 변수명변경, names(df)[names(df)=='x']<-'y'
#summarise() : 집계, aggregate()
#group_by() : 그룹별집계
#inner_join(df1,df2), merge(df1,df2)
#left_join(df1,df2), merge(df1,df2,all.x=T)

# 세계 각국의 기대수명과 1인당 국내 총생산, 인구에 대한 정보를 집계한 데이터셋
install.packages("gapminder")

str(gapminder)
head(gapminder,20)
#각나라별 기대수명추출
gapminder[,c('country','lifeExp')]

#각나라별 기대수명과 측정년도 추출
gapminder[,c('country','lifeExp','year')]

select(gapminder, country, lifeExp)
gapminder %>%
  select(country, lifeExp)

gapminder[gapminder$country=='Croatia',c('lifeExp','pop')]

# Croatia의 1990년 이후의 기대수명과 인구를 추출
gapminder[gapminder$country=='Croatia'&gapminder$year>1990,c('lifeExp','pop')]

#Croatia의 기대수명과 인구의 평균을 추출하시오.
#apply(데이터셋,방향,함수) 방향 (1행 2열)
apply(gapminder[gapminder$country=='Croatia',c('lifeExp','pop')],2,mean)
#Croatia 정보추출
filter(gapminder,country=='Croatia')
gapminder %>%
  filter(country=='Croatia')

#크로아티아의 기대수명과 인구 추출
gapminder %>%
  filter(country=='Croatia') %>%
  select('lifeExp','pop')

# 인구(pop) 평균
mean(gapminder$pop)
summarise(gapminder,mean(pop))

#대륙별 인구의 평균
summarise(group_by(gapminder,continent), mean(pop))

gapminder %>%
  group_by(continent) %>%
  summarise(mean(pop))

#대륙별 나라의 인구평균
gapminder %>%
  group_by(continent,country) %>%
  summarise(mean(pop))

#mtcars
str(mtcars)
#행추출 : filter(데이터, 조건식)
#실린더의 개수가 4기통에 해당하는 자동차의 정보만 추출하시오.
mtcars %>%
  filter(cyl==4)

#실린더가 6기통 이상이고 연비(mpg) 20을 초과하는 자동차 정보만 추출
filter(mtcars,cyl>=6&mpg>20)

#mtcars 에서 변속기(am)과 기어(gear)데이터만 추출
select(mtcars,c('am','gear'))

#mtcars에서 무게(wt)를 기준으로 오름차순 정렬한 후 상위 6개만 추출

head(arrange(mtcars,desc(wt)))

#mtcars에 year라는 생산년도를 담을 열을 추가한 후 1974라는 값 표시
mutate(mtcars, year='1974')
#자동차별 연비(mpg)순위를 구하여 mpg_rank 열을 추가하여 표시
mutate(mtcars,mpg_rank=rank(mpg))
#mtcars의 실린더개수에 따른 종류와 기어개수에 따른 종류 추출
distinct(mtcars,cyl)
distinct(mtcars,gear)
#자동차 실린더 개수의 평균,최소값,최대값 추출
summarise(mtcars,cyl_mean=mean(cyl))
summarise(mtcars,cyl_min=min(cyl))
summarise(mtcars,cyl_max=max(cyl))

#동일한 실린더 개수를 가진 차가 몇대인지 추출
gp<-group_by(mtcars,cyl)
summarise(gp,n())

#동일한 실린더 개수를 가진 차들중 기어값이 중복인 데이터를 제외한 건수
gp<-group_by(mtcars,cyl)
summarise(gp,n_distinct(gear))

#EDA(탐색적 데이터 분석)
tips<- read.csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
str(tips)
head(arrange(tips,desc(tip)))
summarise(tips,mean(total_bill))
ggplot(tips,aes(x=tip, y=total_bill)) + geom_point()
tips$sex<-as.factor(tips$sex)
tips$smoker<-as.factor(tips$smoker)
tips$day<-as.factor(tips$day)
tips$time<-as.factor(tips$time)
summary(tips)
#동석자수의 분포
tips%>%
  ggplot(aes(size)) + geom_histogram()
#2명이 같이 오는 경우가 제일 많다.

#총계산금액에 따른 팁액수 분석
tips%>%
  ggplot(aes(total_bill,tip)) + geom_point()

tips%>%
  ggplot(aes(total_bill,tip)) + geom_point(aes(col=day, pch=sex), size=3)

#탐색적 데이터 분석 : mpg
summary(mpg)
mpg<-as.data.frame(ggplot2::mpg)
str(mpg)

# 자동차 배기량(displ)에 따른 고속도로연비(hwy)
ggplot(mpg,aes(displ,hwy)) + geom_point()
median(mpg$displ)
#자동차 배기량이 4이하인 자동차와 5이상인 자동차 중 어떤 자동차의 고속도로 연비가 높은지 분석
mpga<-filter(mpg,displ<=4)
mean(mpga$hwy)
mpgb<-filter(mpg,displ>=5)
mean(mpgb$hwy)
