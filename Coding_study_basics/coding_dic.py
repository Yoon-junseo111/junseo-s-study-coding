# 자료형 - 딕셔너리

# dict의 역할로는 자바스크립트의 JSON 모양과 동일한 형태로 구성되어 있고
# 웹프로그램과 연동되거나, 크롤링, 데이터베이스와 연동된 프로그램을 작성할 때 굉장히 많이 사용된다.

a = dict()
a = {} # 중괄호
a = {"sea": "바다"}
a = {"numbers": [1, 2, 3, 4, 5]}

# 추가
a = {}  # 생성만
a = dict()

a["sea"] = "바다"
a["numbers"] = [1, 2, 3, 4, 5]


# 삭제
del a["python"]

# 리스트처럼 pop 가능
# 단, pop() 호출시 값을 반환하는 점이 del 과 다름
return_value = a.pop("numbers")

# 모두 삭제하기
a.clear()


# 딕셔너리 결합
a = {"a": 1234, "b": "4567"}
b = {"c": "zzzz", "d": "qqqq"}
a.update(b)


# 딕셔너리 메서드
a = {"양파": "채소", "수박": "과일", "삼겹살": "고기"}
print(a.keys())
print(a.values())
print(a.items())

print(a["양파"]) # 없으면 오류
print(a.get("양파")) # 없으면 None 리턴

for k, v in a.items():
    print(f"key:{k}" "value: {v}")


a = {"양파": "채소", "수박": "과일", "삼겹살": "고기"}
"삼겹살" in a

