#'dplyr'설치및 로드

# mtcars 데이터셋의 구조와 내용 확인
str(mtcars)
#행의 수와 열의 수를 확인하는 함수
nrow(mtcars)
ncol(mtcars)
# 수치형 데이터셋의 기초통계량을 확인
summary(mtcars)

#주요함수
#주어진조건에 만족하는 행을 추출 : filter(df, condition), subset()
filter(mtcars, cyl==4)

#[조건식],[인덱스],[행조건식,열조건식],[행인덱스,열인덱스]
mtcars[mtcars$cyl==4,]

#논리연산자 : and(&), or(|), not(!)
filter(mtcars, cyl>=6 & mpg>20)

#열추출 : select(df,v1,v2,...)
tail(select(mtcars,am,gear),10)

#정렬 : arrange(df,v) or arrange(df, desc(v))
head(arrange(mtcars,wt))
head(arrange(mtcars,desc(wt)))

#열추가 : mutate(df,v=조건)
mutate(mtcars, year='2023')

#연비(mpg)를 이용하여 순위를 구하고 해당 순위를 파생변수 mpg_rank 추가
mutate(mtcars,mpg_rank=rank(mpg))

#중복값제거 : distinct(df,v)
#도수분포표 : table()
table(mtcars$cyl)
distinct(mtcars,cyl)
distinct(mtcars,cyl,gear)

#요약 : summarise(df,v=기술통계함수) or summarize()
summarise(mtcars,mpg_mean=mean(mpg), mpg_min=min(mpg),mpg_max=max(mpg))

#그룹별로 : group_by(df,v)
summarise(group_by(mtcars,cyl), n())

#n_distinct() : 중복을 제거한 개수 추출 n() : 전체개수
#위 두 함수는 개별적으로 사용불가 반드시 summarise, filter, mutate에서만 사용

#샘플 : sample_n(df, 추출할개수), sample_frac(df, 추출할비율)
sample_n(mtcars,10)
sample_frac(mtcars,0.2)

#파이프 연산자 or 연결연산자 : %>%, shift+ctrl+M 
group_by(mtcars,cyl) %>% summarise(cnt=n())
#mpg(연비)를 이용하여 순위를 계산한 후 해당 값을 mp_rank라는 변수에 대입
mp_rank <- mutate(mtcars, mpg_rank=rank(mpg))
arrange(mp_rank, mpg_rank)
mutate(mtcars, mpg_rank=rank(mpg)) %>%
  arrange(mpg_rank)
