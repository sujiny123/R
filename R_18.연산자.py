install.packages

v1<-c('A','B','C')
str_c(v1,'1')

paste(v1,'1')
paste0(v1,'1')

paste(v1,'1',sep='_')
str_c(v1,'1',sep='_')

#Character 개수 카운트
#nchar(x)
#str_length(x)
s<-'Hello'
nchar(s)

#소문자 변환
#tolower(x)
tolower(s)

#대문자 변환
#toupper(x)
toupper(s)

#2개의 문자 벡터에 중복항목 없이 합치기
#union(x,y)
x<-c('hello','world','r','program')
y<-c('hi','world','r','coding')
union(x,y)

#교집합 intersect(x,y)
intersect(x,y)

#차집합 setdiff(x,y)
setdiff(x,y)

#setequal(x,y)
setequal(x,y)

#문자 공백 제거 : trim
#str_trim(x,side='both'/'left'/'right')
s2<- c('     hello World     ','     hi R     ')
str_trim(s2)
str_trim(s2,side='both')

#stirng 반복해서 추출
#rep(x, times, each, length.out)

rep(1:3,times=2)
rep(1:3,times=2,each=3)
rep(1:3, times=2, each=3, len=4)
rep('hello',times=2)

#str_dup(x, times)
str_dup('hello',times=2)

#문자열 일부분 추출
#substr(x,start,stop)
substr('hello', 1,2)

#함수(Function)
#함수명<- function(매개변수){함수의 몸체}
fibo<-function(n){
  if(n%%2==0){
    print('짝수')
    }else{
  print('홀수')
    }
  }
fibo(7)
fibo(8)

#plot->ggplot
#plot(x,y,xlab,ylab,main)
#점의종류(pch)
#점의크기(cex)
#점의색상(col), col=#FF0000 or col='red'

install.packages("mlbench")
#data(Ozone)
help(Ozone)
str(Ozone)
plot(Ozone$V8,Ozone$V9, xlab='Sandburg Temp', ylab='El Monte Temp')
#차트제목
plot(Ozone$V8,Ozone$V9, xlab='Sandburg Temp', ylab='El Monte Temp', main='Ozone', pch='+',cex=2,col='#ff0000')

#축값 범위(xlim,ylim) xlim=c(최소값, 최대값)
max(Ozone$V8, na.rm=T)
max(Ozone$V9, na.rm=T)
plot(Ozone$V8,Ozone$V9, xlab='Sandburg Temp', ylab='El Monte Temp', main='Ozone', pch='+',cex=2,col='#ff0000',xlim=c(0,100),ylim=c(0,90))
