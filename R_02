# 자료형(data type)
## 변수(variable) : 변하는 수, 기억장소
## 변수명을 작성하는 규칙(명명법) : 영문자(대,소문자), 숫자, 특수문자, 첫글자 문자, _, $

## 상수(constant) : 변하지않는 수, 값(data)
## R의 기본자료형 : 수치형(numeric), 문자형(character), 논리형(logical), 복소수형(complex)
## 대입연산자 또는 치환연산자 : 좌변 = 우변, V=C, v, 수식, <-, ->
## 변수
x <- 5
y = 10

## 출력함수 print()
print(x)

## 변수 대입과 동시에 출력
(z<-2)

y
x+y

# 변수 제거 : rm(), rm = remove
rm(x)
xx<-print ##객체복사
print('안녕하세요')
xx('안녕하세요')
rm(xx)

## 현재 메모리에 저장된 변수의 목록을 확인하는 명령
ls()
help(ls)

x <- "one"
x
print(x, quote = F) # T=True F=False

# 출력서식을 지정하여 출력하는 함수 sprintf = string print format
## 서식기호 : %s, %f, %i
## 홍길동의 나이는 낭랑 18세 입니다.
print("홍길동의 나이는 낭랑 18세 입니다.")
sprintf("%s의 나이는 낭랑 %i세 입니다.", "이순신", 23)

# 자료구조 : 데이터를 효율적으로 저장하기 위한 틀
## 벡터(vector) : 하나 이상의 데이터를 관리하는 자료구조, 요소
## 벡터의 특징 : R에서 하나 이상의 데이터를 관리하는 자료구조, scalar도 벡터로 취급
## 벡터의 생성함수 : c()
## 벡터의 인덱스의 시작값 1부터
## 하나의 벡터에는 하나의 자료형만 사용할 수 있다.
## NA : 결측값

v1 <- c(1, 2, 3, 4, 5)
v2 <- 1:5
v3 <- c(1.5, 10, 'two', 5, 'five')

## start:end, step=1 생략
x2 = 1:15
x3 = c('one', 'two','three')
x1= c(1, 2, 3, 4)
# 벡터 합치기 : append(변수1, 변수2)
x3 = append(x1, x2)
x4 = c(x1, 0, x2)

## vector(length=n) : 요소가 n개인 비어있는 벡터를 생성하는 함수
vector(length=5) # mode='logical' 기본형
# 벡터안에 또다른 벡터를 담을 수 있다.
c(1, 2, 3, c(4:6))
y=c()
y=c(y, c(1:3)) # append

# seq(start, stop, by) by = 1
xx = seq(1,5)
yy = c(1,2,3,4,5)
zz= 1:5

seq(0, 1, length.out = 11) #length.out = 요소 개수

a= seq(10)

# rep(벡터, times=반복횟수), each = 요소별 반복횟수
rep(c(1:3), times=3)
rep(c(1:3), each=2)

# 자료형을 이용한 벡터의 생성
# numeric(integer, double), character, logical
integer(length=10) #정수형의 기본값은 0

# 벡터를 구성하는 자료를 요소(item)라고 부른다.
# 요소의 위치를 인덱스(index)라고 부른다.
# 인덱스의 시작은 1이다.
## 인덱스를 이용한 요소에 접근 [], [조건식]
x=1:11
x[5]
x[2:5]
x[c(1, 3, 5)]

# 벡터의 각 셀에 이름을 부여할 수 있다.
y= c(a=1, b=10, c=7)
y['a']
y[c('b','c')]

xx=c(1, 3, 5)
names(xx)=c('lee', 'kim', 'park')
xx
xx[c('lee', 'park')]
xx['kim']
names(xx)[2]

# 벡터의 주요 내장함수
typeof(xx)
mode(xx)

## 벡터의 길이 = 벡터를 구성하는 요소의 개수, length()
a= c('x', 'y', 'z')

a[-2] # 해당 인덱스를 제외
length(a)
## NROW()- 대문자, 행렬과 벡터에서 모두 사용, 행의 수
## nrow()- 소문자, 행렬(matrix)에서 행의 개수를 추출하는 함수

NROW(a)
nrow(a)
## 통계함수
## cor() : 상관계수, cumsum() : 누적함수 length() : 요소의 개수
## max() : 최대값, mean() : 평균값, min() : 최소값, range() : 범위
## rank : 순위, sd() : 표준편차, sum() : 합계, summary(): 기초통계량

## 데이터분석에서 주로 사용되는 함수 : matrix(행과열) 나 dataframe(표)
## head () tail() summary()
## R에 내장된 데이터셋 -data()
data(iris)
iris

#데이터 구조
str(iris)
head(iris)

head(iris, 10)
summary(iris)

x = 1:10

# 총합
sum(x)

# 평균
mean(x)

var(x)
sd(x)
median(x)
max(x)
min(x)
range(x)
quantile(x)

## 벡터의 연산 : 벡터의 요소들을 이용하여 수정, 삭제, 추가
## 사칙연산, 내장함수
## 스칼라(scalar) : 하나의 요소로 구성된 자료 구조
## 벡터(vector) : 하나 또는 그이상의 요소로 구성된 자료구조

x=10
y=c(1:5)
length(y)
10+20

x=c(1:5)
y =c(6:10)
x+y # 벡터화 연산
z=c(1:3)
z+x
x+9
x-9
x*3
x/3
x%/%3
x%%3
x[3]=30
x
x[c(2,4)]=9

## 벡터 x의 모든요소의 값을 1로 변경하시오.
x[c(1:5)]=1
x

## 벡터 x의 첫번째 요소자리에 0을 추가
c(0, x)
x
x=c(0,x)
x
## append(벡터,벡터)
x= append(x, 0)
x
help(append)

# v_a의 마지막 요소의 값을 제외하고 추출
v_a= c('A', 'B', 'C', 'D', 'E')
length(v_a)
v_a[-length(v_a)]

# 논리형 벡터 : 논리형(logical) - TRUE(T) or FALSE(F)
v_b = c(FALSE, TRUE, TRUE, FALSE, FALSE)

# and/&, or/|, not/!
!v_b
v_b[c(2:3)]

# 펜시인덱스
# 논리값을 이용하여 인덱스 처리하는 기능
v_t =c('첫번째', '두번째','세번째','네번째','다섯번째')

#두번째, 세번째 요소만 추출
v_t[v_b]

# %in% : ~안에 포함여부를 판단하여 출력하는 연산자
'a' %in% c('a','b','c')

# 합집합(union), 교집합(intersect), 차집합(setdiff)
setdiff(c('a','b','c'), c('a','d'))
intersect(c('a','b','c'), c('a','d'))
union(c('a','b','c'), c('a','d'))

# 집합간의 비교연산
setequal(c('a','b','c'), c('a','d'))
setequal(c('a','b','c'), c('a','b','c','b'))

# all(), any()
x=1:10
x>5

all(x>5)
any(x>5)

head(x)
tail(x)
tail(x,3)
