# # 데이터 타입(data type)

# # 1. 숫자
# # 정수(integer) - 소수점 X
# from sys import getsizeof
# a = 10

# # 실수(float) - 소수점 O
# b = 3.14

# # 복소수(complex) - 실수부&허수부
# c = 3 + 4j  # (j=>i)

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))


# # 2. 문자열(string)
# name = "에단"
# print(name, type(name))


# # 3. 불리언(boolean)
# 참 = True
# 거짓 = False

# print(참, type(참))
# print(거짓, type(거짓))

# print('bool', 10 > 5, type(10 > 5))  # 비교연산의 결과로 불리언 값 얻을 수 있
# print('bool', 10 == 5, type(10 == 5))
# print('bool', 10 <= 5, type(10 <= 5))


# # 4. None 타입 - 아직 값 할당 X
# result = None
# print(result)


# # 산술연산자
# a = 20
# b = 10

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)    # 나눗셈 결과 항상 float
# print(a // b)   # int
# print(a % b)
# print(a ** b)


# # 비교연산자
# x = 5
# y = 10

# print(x == y)
# print(x >= y)
# print(x <= y)
# print(x != y)
# print(x > y)
# print(x < y)

# age = 7
# print(x < age < y)  # age가 x보다 크고 y보다 작음


# # 논리연산자
# print('논리연산자')
# p = True
# q = False

# print(p and q)  # 둘 다 True
# print(p or q)   # 하나라도 True
# print(not p)    # 논리부정

# d = 10
# e = 20
# f = 30
# print((d < e) and (e > f))
# print((d < f) or (e > f))


# # 할당 연산자
# print("할당 연산자")
# z = 10
# z += 10
# print(z)
# z -= 15
# print(z)
# z *= 3
# print(z)


# # 멤버십 연산자
# print("멤버십 연산자")
# fruits = ["사과", "바나나", "체리"]  # list
# print("사과" in fruits)
# print("수박" in fruits)

# # None 타입
# result = None

# str = "문자열"
# print(getsizeof(1))
# print(getsizeof("1"))
# print(getsizeof(str))
# print(getsizeof("문자열"))


# # 자료형
# numm = input("숫자를 입력하세요 :")
# print(numm, type(numm))
# a = int(numm) / 2   # 명시적 형변환
# print(a)

# num = int(input("숫자입력하세요 : "))
# print(num)
# a = num / 2
# print(a)

# w = 3.14
# print(int(w))  # 데이터 손실


# # 이스케이프 문자
# print("안녕\n하세요")
# print("안녕\t하세요")
# print("안녕\'하세요")
# print("안녕\"하세요")
# print("안녕\\하세요")


# year = "올해는 %d년 %s의 해이다" % (2024, "용띠 ")
# print(year)  # 올해는 2024년 용띠의 해이다

# number = "저는 올해 %d살입니다." % 20
# print(number)  # 저는 올해 20살입니다.
# calc = "10 나누기 4는 %.3f입니다." % 2.5
# print(calc)  # 10 나누기 4는 2.500입니다.
# text = "저는%5s에서 살고있습니다." % "서울"
# print(text)  # 저는 서울에서 살고있습니다.
# char = "이모티콘은 %c 이것으로 할께요" % "©"
# print(char)  # 이모티콘은이것으로 할께요


# country = "대한민국"
# city = "서울"
# people = "한국인"
# text = "저는 올해 {0}살입니다." .format(20)
# print(text)  # 저는 올해 20살입니다
# text = "저는 {0}사람이며 {1}에 살고있습니다.".format(country, city)
# print(text)  # 저는 대한민국사람이며 서울에 살고있습니다.
# text = "제가 사는 {0}은 {country}에 있습니다.".format(city, country="한국")
# print(text)  # 제가 사는 서울은 한국에 있습니다
# text = "나는 {1}이다. {{ 그리고 }} {0}에 산다.". format(city, people)
# print(text)  # 나는 한국인이다. { 그리고 } 서울에 산다.
# text = "{}점수: {}점, {}점수 : {}점".format("영어", 100, "수학", 90)
# print(text)


# a = "[{0:<10}]".format("hey")
# print(a)  # 좌측정렬, 나머지공백 [hey
# a = "[{0:>10}]".format("hey")
# print(a)  # 우측정렬, 나머지공백 [hey]
# a = "[{0:^10}]".format("hey")
# print(a)  # 가운데정렬, 좌/우공백 [ hey/ 오른쪽이 더 많음
# a = "[{0:!<10}]".format("hey")
# print(a)  # 좌측정렬, 특수문자 [hey! !!!!!! ]
# a = "[{0:^20.7f}]".format(1 / 3)
# print(a)  # 가운데정렬, 좌/우공백, 전체길이 20 [0.3333333
# a = "[{0:,}] ".format(123456789)
# print(a)
# # 세자리수 마다, [123,456,789]

# print("\n")
# print("|\ _ /|")
# print("| q p |\t/}")
# print("( @ )\"\"\"\\")
# print("|\"^\"` \t|")
# print("||_/=\\\\__|")
# print("\n")

# a = "[{0:=^9}]".format("박도희")
# print(a)
# text = "문자열 실습입니다. {{ 중괄호 }}를 출력해보세요".format()
# print(text)


# b = "문자열 실습입니다. {{{0:^9}}}를 출력해보세요".format("중괄호")
# print(b)

# 출력 = "{{{0:^9}}}".format("중괄호")
# text = f'문자열 실습입니다. {출력}를 출력해보세요'
# print(text)


# print("문자열 인덱싱")

# a = "Hello, python"

# print("a[7]", a[7])
# print("a[-6]", a[-6])

# print("a[0:5]", a[0:5])
# print("a[7:]", a[7:])
# print("a[:5]", a[:5])
# print("a[:]", a[:])

# date = "20240930"
# print(date[:4] + "년" + date[4:6] + "월" + date[6:] + "일")
# print(len(date))
# print(date.count('2'))
# print(date.find('4'))
# # print(date.index('5'))

# # replace 첫번째 변경하고자 하는 문자, 두번째
# print(date.replace('0', '1', 2))
# print(date.split('0'))


# text = "Hello, python"
# print(text.upper())
# print(text.lower())

# text = "     Hello  world "
# print("[" + text.strip() + "]")
# print(text.split())

# print("123".isdigit())
# print("dkdkdk".isdigit())

# print("hello".isalpha())
# print("hello".isalnum())
# print("hello".isspace())

# text = "hello"
# print(text.upper().isupper())
# print(text.lower().islower())


# name = input("이름을 입력하세요. ")
# age = int(input("나이를 입력하세요. "))
# print("안녕하세요! ", name, "님 " "(", age, "세)")

# name = input("이름을 입력하세요. ")
# birth = int((input("태어난 년도를 입력하세요. ")))
# year = int((input("올해 년도를 입력하세요. ")))
# age = year - birth + 1
# print("올해는", year, "년,", name, "의 나이는", age, "세 입니다.")

number = int(input())

answer = 0

for i in range(len(str(number))):
    answer += number % 100  # answer = answer + (number % 100)
    number //= 100  # number = number // 100
    # print(answer)
    # answer += number % 100  # answer = answer + (number % 100)


# for i in range(1):
#     answer += number % 100 나머지
#     print(answer)
#     print(number)
#     number //= 100 몫
#     print(number)
#     answer = answer + number


print(number)
print(answer)
