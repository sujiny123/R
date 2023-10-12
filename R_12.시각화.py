#시각화 ggplot2 패키지를 이용
#패키지 설치-외부패키지
#패키지로딩- 패키지가 제공하는 다양한 함수를 사용
#기본문법 - 레이어 구조이용
## style1. ggplot(data,aes()) + geom_point()
# style2. ggplot(data)+ geom_point(aes())
#mapping(매핑)-연결, a<-1
#aes() : x,y축에 관한 값을 매핑
#내장데이터셋 airquality
str(airquality)
ggplot(airquality, aes(x=Day, y=Temp)) + geom_point()
#산점도(산포도) : 두 관측데이터의 상관관계를 분석할 떄 효율적으로 사용
#볼릿(심볼)의 크기와 색상을 변경하는 작업(기본점의크기 1.5)
ggplot(airquality, aes(x=Day, y=Temp)) + geom_point(color='red', size=3)

ggplot(airquality, aes(x=Day, y=Temp, color='red', size=3)) + geom_point()

# 선그래프 : 시계열 데이터, geom_line()
ggplot(airquality, aes(x=Day, y=Temp)) + geom_line()

# 막대그래프 : 빈도(크기), geom_bar()
#실린더종류에 따른 차종의 빈도수 확인
# factor() : 범주형의 의미를 가지고 비어있는 값을 제외할때 
ggplot(mtcars, aes(x=factor(cyl))) + geom_bar(width=0.5)
table(mtcars$cyl)

#누적막대그래프
table(mtcars$gear)
ggplot(mtcars, aes(x=factor(cyl))) + geom_bar(aes(fill=factor(gear)))
#fill() - 해당 축의 값이 색상으로 채워지는 옵션

#누적막대 그래프를 선버스트 차트를 이용
ggplot(mtcars, aes(x=factor(cyl))) + geom_bar(aes(fill=factor(gear))) + coord_polar(theta='y')

# 상자수염그래프 : geom_boxplot()
# 전체 데이터의 분포를 확인하는 시각화도구로 이상치를 판단할때 유용
# 날짜별로 그룹화 하여 사용해야함
ggplot(airquality, aes(x=Day, y=Temp, group = Day)) + geom_boxplot()

#히스토그램 : geom_histogram()
ggplot(airquality, aes(Temp)) + geom_histogram(binwidth=1)

#선추가 : geom_abline()
#geom_abline(intercept=절편, slope=기울기)
ggplot(economics, aes(x=date, y=psavert)) +geom_line() + geom_abline(intercept=12.18671, slope=-0.0005444)

#평행선 추가 : geom_hline(yintercept=y절편)
ggplot(economics, aes(x=date, y=psavert)) +geom_line() + geom_abline(intercept=12.18671, slope=-0.0005444) + geom_hline(yintercept=mean(economics$psavert))

# 수직선 추가 : geom_vline(xintercept=x절편)
ggplot(economics, aes(x=date, y=psavert)) +geom_line() + geom_abline(intercept=12.18671, slope=-0.0005444) + geom_hline(yintercept=mean(economics$psavert)) +geom_vline(xintercept=as.numeric(min_date))
min_psavert<- min(economics$psavert)
min_psavert
min_date<-economics[economics$psavert==2.2,'date']
#개인 저축률이 가장 낮은 시기를 이용해서 수직선 추가

#레이블 추가 : geom_text(aes(label=레이블, vjust=세로위치, hjust=가로위치))
ggplot(airquality, aes(x=Day, y=Temp)) + geom_point() +geom_text(aes(label=Temp, vjust=0, hjust=0))

#세로와 가로의 위치값이 모두 0이면 점의 오른쪽위
#세로와 가로의 위치값이 + 이면 값은 왼쪽/아래, -이면 오른쪽/위

#도형이나 화살표 추가 : annotate()
#그래프 영역에 투명 박스나 화살표를 이용하여 특정 영역을 강조하는 역할
#annotate('모양', xmin=x시작값, xmax=x끝, ymin=y시작값, ymax=y끝)
#mtcars 데이터셋에 무게와 연비를 기준으로 산점도 그래프를 구현한다.

ggplot(mtcars, aes(x=wt, y=mpg)) +geom_point() +annotate('rect', xmin=3, xmax=4, ymin=13, ymax=20, alpha=0.5, fill='skyblue')

#annotate()함수의 모양 부분에 화살표를 뜻하는 segment를 추가
# x, xend와 y, yend를 추가
ggplot(mtcars, aes(x=wt, y=mpg)) +geom_point() +annotate('rect', xmin=3, xmax=4, ymin=13, ymax=20, alpha=0.5, fill='skyblue') + annotate('segment', x=2.5, xend=3.7, y=10, yend=17, arrow=arrow(), color='red') + annotate('text', x=2.5, y=10, label='point')

#그래프의 제목, 축제목 추가 : labs()
#labs(x='x축제목', y='y축제목', title='그래프제목')
ggplot(mtcars, aes(x=gear)) + geom_bar() + labs(x='기어수', y='자동차수', title='기어별 자동차수')

#디자인 테마 : theme()
theme_gray()

