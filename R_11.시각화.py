#데이터 시각화 : plot(), barplot(), boxplot(), pie() => ggplot2
# plot() : 산점도 그래프
# plot(y축 데이터, 옵션)or(x축데이터,y축데이터,옵션)
y<-c(1,1,2,2,3,3,4,4,5,5)
plot(y)

# pch : 심볼모양
plot(y, pch=5)

cars
plot(cars$speed, cars$dist)
#xlab, ylab - x축, y축 이름
# main - 그래프 제목
# sub -그래프 부제목
# ann - T/F, 제목 지정여부
# axes - T/F, 축 표시여부
# axis - 사용자 지정 축값
# type - 그래프 종류(l=line, p=point, b=both)
# lty(line style) : 0()
x<-1:10
y<-1:10
plot(x,y,pch='*',type='l',lty='dotted',col='blue')

x<-runif(100)
y<-runif(100)http://127.0.0.1:13267/graphics/plot_zoom_png?width=1920&height=1017
##y의 값이 0.5보다 크면 1, 아니면 18
plot(x,y,pch=ifelse(y>0.5,1,18))

# 산점도 + 텍스트 추가
library(MASS)
str(Animals)
Animals

plot(Animals$body,Animals$brain, pch=16, col='blue', 
     xlab='Body weight(kg)', ylab='brain weight(g)',xlim=c(0,250),ylim=c(0,1400))
text(x=Animals$body,y=Animals$brain, labels=row.names(Animals),pos=4)

plot(~Sepal.Length+Sepal.Width, data=iris, pch=rep(15:17, each=50),col=c('red','green','blue')[iris$Species], cex=1.5)
legend('topright', legend = levels(iris$Species), pch=15:17, col=c('red','green','blue'), cex=1.2, bty='n')

#막대그래프 : barplot(), 도수분포표, 빈도
?barplot
sales<-c(0.12,0.3,0.26,0.16,0.04,0.12)
barplot(sales, names.arg=c('berry','cherry','apple','banana','candy','cream'), horiz=T)

#누적 막대그래프
xx<-matrix(1:6, nrow=3)
xx
barplot(xx)

# 시즌별 티켓 판매량을 그래프로 표현
aaa<-c(110, 300,150,280,310)
bbb<-c(180,200,210,190,170)
ccc<-c(210,150,260,210,70)
data <- matrix(c(aaa,bbb,ccc),5,3)
data
barplot(data, main='스포츠경기별 티켓 판매량',xlab='종목',ylab='판매량', beside=T, 
        names.arg=c('야구','축구','농구'),border='blue',col=rainbow(5), ylim=c(0,400))
legend(16,400,c('야구','축구','농구'), cex=0.8, fill = rainbow(5))

#단순하게 그래프를 그리는 qplot(x,y,옵션)
qplot(Sepal.Length, Petal.Length, data=iris)

#꽃잎그래프(sun flower graph)
x<- c(1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,6,6,6,6)
y<- c(2,1,3,2,3,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2)
dt<-data.frame(x,y)
dt
sunflowerplot(dt)
data("mtcars")

stars(mtcars[1:4],flip.labels = F,key.loc = c(13,1.5))
#ggplot 시각화하는단계-레이어구조
# step1. 도화지(캔버스-배경)-축을그린다.
ggplot(data=mpg, aes(x=displ, y=hwy)) +geom_point() +xlim(3,6)+ylim(10,30)
#step2. 그래프의 종류
#geom_bar(): 막대그래프
#geom_histogram() : 히스토그램
#geom_boxplot(): 박스플롯
#geom_line() : 선그래프
#geom_point() : 산점도 그래프
#step3. 기타옵션을 지정해서 그래프를 정교하게 표현
