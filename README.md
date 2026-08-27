# Python 기초 학습 및 가계부 프로그램

Python의 기본 자료형과 문법을 학습하고, 학습한 내용을 활용하여 간단한 콘솔 기반 가계부 프로그램을 구현했습니다.

Dictionary, Set, Tuple의 특징과 주요 메서드를 학습했으며,
List와 Dictionary를 활용하여 수입과 지출 데이터를 관리하는 프로그램을 작성했습니다.

---

# Python 자료형 학습

## 딕셔너리 (Dictionary)

Python의 Dictionary 자료형의 기본 구조와 데이터 관리 방법을 학습했습니다.

### 학습 내용

- Dictionary 생성
- Key / Value 구조
- 데이터 추가 및 삭제
- `del`을 이용한 데이터 삭제
- `pop()`을 이용한 데이터 삭제 및 반환
- `clear()`를 이용한 전체 데이터 삭제
- `update()`를 이용한 Dictionary 결합
- `keys()`, `values()`, `items()` 활용
- `get()`을 이용한 데이터 조회
- 반복문을 이용한 Key / Value 순회
- `in`을 이용한 Key 존재 여부 확인

### 예제 코드

```python
data = {
    "양파": "채소",
    "수박": "과일",
    "삼겹살": "고기"
}

print(data.keys())
print(data.values())
print(data.items())

for key, value in data.items():
    print(f"key: {key}, value: {value}")
```

---

## 집합 (Set)

Python의 Set 자료형과 집합 연산 방법을 학습했습니다.

Set은 중복된 값을 허용하지 않는 특징을 가지고 있어
데이터의 중복을 제거할 때 활용할 수 있습니다.

### 학습 내용

- Set 생성
- 합집합
- 차집합
- 교집합
- `add()`를 이용한 요소 추가
- `remove()`를 이용한 요소 삭제
- `update()`를 이용한 여러 요소 추가
- Set의 중복 제거 특성
- List의 중복 데이터 제거

### 예제 코드

```python
a = {0, 1, 2, 3, 4}
b = {3, 4}

# 차집합
print(a - b)

# 교집합
print(a & b)
```

List의 중복 데이터도 Set을 활용하여 제거할 수 있습니다.

```python
my_list = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

my_list = list(set(my_list))

print(my_list)
```

---

## 튜플 (Tuple)

Python의 Tuple 자료형과 List와의 차이점을 학습했습니다.

Tuple은 생성된 이후 특정 요소의 값을 변경하거나 삭제할 수 없는
불변(Immutable) 자료형이라는 특징이 있습니다.

### 학습 내용

- Tuple 생성
- 단일 요소 Tuple 생성
- Tuple Packing
- Tuple Unpacking
- 변수 Swapping
- Indexing
- Slicing
- Tuple의 불변성

### 패킹과 언패킹

```python
data = 1, 2, 3

a, b, c = data
```

### 변수 값 교환

Tuple의 Packing과 Unpacking을 이용하여 두 변수의 값을 간단하게 교환할 수 있습니다.

```python
a = 100
b = 200

a, b = b, a
```

---

# 가계부 프로그램

Python의 기본 문법과 List, Dictionary를 활용하여
콘솔 환경에서 사용할 수 있는 간단한 가계부 프로그램을 구현했습니다.

사용자가 프로그램을 종료하기 전까지 메뉴가 반복적으로 출력되며,
메뉴 번호를 선택하여 수입과 지출을 관리할 수 있도록 구성했습니다.

---

## 주요 기능

### 수입 추가

수입 금액과 메모를 입력받아 Dictionary 형태로 생성한 후
수입 List에 저장합니다.

```python
income = {
    "금액": money,
    "메모": memo
}

income_list.append(income)
```

---

### 지출 추가

지출 금액과 메모를 입력받아 Dictionary 형태로 생성한 후
지출 List에 저장합니다.

```python
expense = {
    "금액": money,
    "메모": memo
}

expense_list.append(expense)
```

---

### 거래 내역 조회

등록된 수입 및 지출 내역을 조회할 수 있도록 구현했습니다.

각 거래 데이터는 Dictionary 형태로 저장되며,
List를 반복하면서 금액과 메모 정보를 출력합니다.

---

### 잔액 조회

등록된 수입과 지출 데이터를 반복하여 각각의 합계를 계산하고,
총 수입에서 총 지출을 빼 현재 잔액을 계산합니다.

```python
balance = total_income - total_expense
```

출력되는 정보:

- 총 수입
- 총 지출
- 현재 잔액

---

### 메뉴 구성

`while True` 반복문을 이용하여 프로그램이 종료될 때까지
메뉴를 계속 사용할 수 있도록 구현했습니다.

```text
==============================
가계부 프로그램
==============================
1. 수입 추가
2. 지출 추가
3. 내역 조회
4. 잔액 조회
5. 종료
```

`if / elif / else` 조건문을 이용하여 사용자가 선택한 메뉴에 따라
각 기능이 실행되도록 구성했습니다.

1~5 이외의 값을 입력하면 잘못된 입력이라는 메시지를 출력합니다.

---

# 사용한 Python 문법

가계부 프로그램을 구현하면서 다음 Python 문법과 자료형을 활용했습니다.

- 변수
- `input()`
- `print()`
- `int()`
- List
- Dictionary
- `append()`
- `for`
- `while`
- `if / elif / else`
- `break`
- f-string
- 반복문을 이용한 합계 계산

---

# 프로그램 실행 흐름

```text
프로그램 실행
      ↓
메뉴 출력
      ↓
사용자 메뉴 선택
      ↓
┌───────────────────────┐
│ 1. 수입 추가          │
│ 2. 지출 추가          │
│ 3. 내역 조회          │
│ 4. 잔액 조회          │
│ 5. 프로그램 종료      │
└───────────────────────┘
      ↓
선택한 기능 실행
      ↓
메뉴로 돌아가기
      ↓
5번 선택 시 종료
```

---

# 실행 결과

## 실행 결과 1

![가계부 실행 결과 1](p_account_book_result1.png)

## 실행 결과 2

![가계부 실행 결과 2](p_account_book_result2.png)

---

# 학습 및 구현 정리

이번 학습을 통해 Python의 기본 자료형인 딕셔너리(Dictionary), 집합(Set), 튜플(Tuple)의 특징과 사용 방법을 익혔습니다.

또한 단순 문법 학습에서 끝내지 않고 List와 Dictionary를 실제 프로그램에 적용하여
여러 개의 수입 및 지출 데이터를 관리하고 계산하는 가계부 프로그램을 구현했습니다.
