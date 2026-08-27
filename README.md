# Python Study

## Dictionary, Set, Tuple

Python의 기본 자료형인 Dictionary, Set, Tuple의 특징과
기본적인 사용 방법을 학습하고 예제 코드를 작성했습니다.

### Dictionary
- Dictionary 생성
- Key / Value 데이터 관리
- 데이터 추가 및 삭제
- `pop()`, `clear()`, `update()`
- `keys()`, `values()`, `items()`
- `get()`을 이용한 값 조회
- 반복문을 이용한 Key / Value 순회

### Set
- Set 생성
- 합집합, 차집합, 교집합
- `add()`, `remove()`, `update()`
- Set의 중복을 허용하지 않는 특징
- List의 중복 데이터 제거

### Tuple
- Tuple 생성
- List와 Tuple의 차이
- Tuple의 불변성
- Tuple Packing / Unpacking
- 변수 Swapping
- Indexing / Slicing

# Account Book Program

Python의 기본 문법과 List, Dictionary를 활용하여
콘솔 환경에서 사용할 수 있는 간단한 가계부 프로그램을 구현했습니다.

사용자가 프로그램을 종료하기 전까지 메뉴가 반복적으로 출력되며,
메뉴 번호를 선택하여 수입과 지출을 관리할 수 있도록 구성했습니다.

---

## Key Features

### Income

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

### Expense

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

### Transaction History

등록된 수입 및 지출 내역을 조회할 수 있도록 구현했습니다.

각 거래 데이터는 Dictionary 형태로 저장되며,
List를 반복하면서 금액과 메모 정보를 출력합니다.

---

### Balance

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

### Menu System

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

# Concepts Used

가계부 프로그램을 구현하면서 다음 Python 문법과 자료형을 활용했습니다.

- Variable
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

# Program Flow

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

# Result

## Account Book Result 1

![Account Book Result 1](p_account_book_result1.png)

## Account Book Result 2

![Account Book Result 2](p_account_book_result2.png)

---

# Development Summary

이번 학습을 통해 Python의 기본 자료형인 Dictionary, Set, Tuple의 특징과 사용 방법을 익혔습니다.

또한 단순 문법 학습에서 끝내지 않고 List와 Dictionary를 실제 프로그램에 적용하여
여러 개의 수입 및 지출 데이터를 관리하고 계산하는 가계부 프로그램을 구현했습니다.

  
