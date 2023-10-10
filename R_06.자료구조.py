# 산술연산자
(11+54*2)/3-10
9 %%3
5%/%2
5**3

#변수
x=5
print(x)
x<-10

# 대입과 동시에 출력을 함
(x<- 2)
#변수 삭제
rm(x)

x<-2
y<-3

# 현재 사용중인 변수의 목록을 출력
ls()

# 출력함수 : print()
help(print)
x<-'one'
y<-'two'
print(x,quote = F)

# 특수상수 NA
aaa<-100
bbb<-75
ccc<-80
ddd<-NA

stu<-c(aaa,bbb,ccc,ddd)

# is.자료형() : 해당 자료형이 맞습니까? TRUE/FALSE
# as.자료형() : 해당 자료형으로 바꾸는 함수

is.na(ddd)

# 특수상수 NULL
x<- NULL
is.null(x)
is.null(1)
is.null(NA)

# vector 내장함수
val<-c(1,2,3,4,5,6,7,8,9)
## summary() : 수치데이터의 기초 통계량을 한꺼번에 보여주는 함수
summary(val)
x<-10

x<-1:5
xy<-rnorm(30) #정규분포 난수를 생성하는 함수
length(x)
range(x)
mean(x)
var(x)
sd(x)

#벡터의 요소에 접근 : 인덱스
#[인덱스]
x[2]
x[-2]
x[3] = 30
x[c(2,4)]

#벡터화 연산 : 벡터에 저장된 데이터의 요소단위로 계산을 수행한다.
#벡터 합치기 : append(a,b)- a,b 두개의 벡터를 연결하는 함수
#append(a, b, after_index)
x<- c(3, 6, 8, 12, 15)
y<- c(5, 10, 15, 20, 25)
z<- append(x, y)
w<- append(x,y,3)

c(1,2) + c(4,5)
c(1,2,3) +1

v<--5:5
#seq = sequence generation seq(from, to, by)
q<- seq(1,5,0.5)

qq<-seq(10)

x<- c(1,2,3)
y<-c(4,2,6)
x==y

# rep(벡터, times=반복횟수 or each =개별반복횟수)
(x<- rep(c('a','b','c'), times=4))
#중복값을 제거하고 대표값만 추출하는 함수
y<-unique(x)
xx<-c('a','b','c','d','d')
#문자를 결함 paste
k<- paste(xx[1],xx[2])
paste(xx[1],xx[2])
paste('hello','world')
cat(paste('hello','\nworld'))
paste('aaa','bbb','ccc')
paste('aaa','bbb','ccc', sep='')
#substring('문자열',시작위치,마지막위치)
substring('abcdefghi',2,5)
#논리값 : T,F
# 논리연산자 : and(&), or(|), not(!)

T|F 
!T

c(T,T)&c(T,F)

#factor < vector
gender<-factor('M', c('M','F'))
nlevels(gender)
levels(gender)
levels(gender[1])
levels(gender)[1]
levels(gender) <- c('male', 'Female')
gender
help(factor)

ordered(c('a','b','c'))
factor(c('a','b','c'), ordered = T)

#행렬(Matrix)
help(matrix)

matrix(c(1:9), nrow=3) #ncol=3, byrow=F 생략
matrix(1:9, ncol=3)
matrix(1:9, nrow=3, byrow = T)
matrix(1:9, nrow=3, dimnames = list(c('item1', 'item2', 'item3'), c('att1','att2','att3')))

##행렬의 데이터에 접근하는 방법 : [행인덱스,열인덱스]
x<-matrix(c(1,2,3,4,5,6,7,8,9), ncol=3)
x[1,1]
x[1,2]
x[2,1]
x[2,2]
x[1:2, ] # 열인덱스 생략하면 모든 열을 추출
x[-3,]
x[-2,-2]
x[c(1,3),c(1,3)]
y<-matrix(1:9, nrow=3, dimnames = list(c('item1', 'item2', 'item3'), c('att1','att2','att3')))

y['item1',]
x

x*2
x +y
#전치행렬
t(x)
help(array)
matrix(1:12, ncol=4)
array(1:12, dim = c(3,4))
x<-array(1:12, dim = c(2,2,3))

x

dim(x)

x[1,1,1]
x[1,2,3]
x[,,3]

#list 리스트
x<-list(name='홍길동',height=170)
x
x$name
x$height
x<-list(name='홍길동',height=c(170, 187, 163))
x
x$name
x$height
x$height[2]

list(a=list(val=c(1,2,3)), b=list(val=c(1,2,3,4)))

#리스트 내 데이터에 접근하는 방법 : $
#리스트명$변수명$키 or 리스트[[인덱스]]
x<- list(name='홍길동', height=c(1,3,5))
x
x$name
x$height
x[[1]]
x[[2]]
x[[2]][2]

#데이터프레임(dataframe)
d<-data.frame(x=c(1:5),y=c(2,4,6,8,10))
d
d2<-data.frame(x=c(1:5), y=c(2,4,6,8,10), z=c('M','F','M','F','M'))
d2
## 기존에 데이터프레임에 특정 컬럼 추가
d2$v <- c(3,6,9,12,15)
d2
d2$x
d2[,1]

d2[,c('x','y')]
d2[,c(1,2)]
d2[,'x',drop=F]
str(d2)

# 타입(data type)
#mode(), typeof(), class()-자료구조
class(c(1,2))
class(matrix(c(1,2)))
class(list(c(1,2)))
class(data.frame(x=c(1,2)))
str(c(1,2))
str(matrix(c(1,2)))

#is.factor(),is.matrix(), is.data.frame(), is.character()
is.numeric(c(1,2,3))
is.numeric(c('a','b','c'))
is.matrix(matrix(c(1,2)))

#형변환 : as.*

x<- c('m','f')
is.character(x)
as.factor(x)
as.numeric(as.factor(x))
