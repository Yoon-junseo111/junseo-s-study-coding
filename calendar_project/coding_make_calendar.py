# 캘린더 만들기


import calendar


year = int(input("연도 입력 : "))   # 입력 받기
month = int(input("월 입력 : "))    # 입력 받기

print(year)
print(month)

# 연도 입력 : 2026
# 월 입력 : 7
# 2026
# 7
#      July 2026
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31

print(calendar.month(year, month))

print("=" * 30)
print("달력 프로그램")
print("=" * 30)

year = int(input("연도 : "))  
month = int(input("월 : ")) 

print()
print(calendar.month(year, month))  # 달력 출력