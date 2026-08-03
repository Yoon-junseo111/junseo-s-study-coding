## 주문 프로그램 ## ex) 햄버거

order_list = []   # 주문 내역을 저장할 리스트

# 프로그램을 종료할 때까지 반복
while True: 
    
    # 메뉴판 출력
    print("\n" + "=" * 35)   # 구분선
    print("햄버거 주문 프로그램")
    print("=" * 35)    # 구분선
    print("1. 불고기 버거  -  5000원")
    print("2. 치즈 버거  -  5500원")
    print("3. 새우 버거  -  5500원")
    print("4. 감자 튀김 - 2500원")
    print("5. 콜라  - 2000원")
    print("6. 주문 내역")
    print("7. 결제")
    print("8. 종료")
    
    # 사용자에게 메뉴 번호 입력받기  
    menu = input("메뉴 선택 :")
        
    ## 1. 불고기 버거 주문 ##
    if menu == "1":
        
        quantity = int(input("수량 :")) # 수량을 quantity 변수에 저장
        
        # 딕셔너리 형태로 주문 정보 저장
        order = {
            "메뉴": "불고기버거",
            "가격": 5000,
            "수량": quantity
        }    
        
        order_list.append(order)
        
        print("불고기버거가 장바구니에 담겼습니다.")
        
        
    ## 2. 치즈 버거 주문 ##
    elif menu == "2":   # 조건 검사
        
        quantity = int(input("수량 :")) # 수량을 quantity 변수에 저장
        
        # 딕셔너리 형태로 주문 정보 저장 
        order = {
                "메뉴": "치즈버거",
                "가격": 5500,
                "수량": quantity
            }    
            
        order_list.append(order)
        
        print("치즈버거가 장바구니에 담겼습니다.")
        
        
    ## 3. 새우 버거 주문 ##
    elif menu == "3":   # 조건 검사
        
        quantity = int(input("수량 :"))  # 수량을 quantity 변수에 저장
        
        # 딕셔너리 형태로 주문 정보 저장 
        order = {
                "메뉴": "새우버거",
                "가격": 5500,
                "수량": quantity
                }    
        
        order_list.append(order)
        
        print("새우버거가 장바구니에 담겼습니다.")
        

    ## 4. 감자 튀김 주문 ##
    elif menu == "4":   # 조건 검사
        
        quantity = int(input("수량 :")) # 수량을 quantity 변수에 저장
        
        # 딕셔너리 형태로 주문 정보 저장 
        order = {
                "메뉴": "감자튀김",
                "가격": 2500,
                "수량": quantity
                }    
        
        order_list.append(order)
        
        print("감자튀김이 장바구니에 담겼습니다.") 
        

    ## 5. 콜라 주문 ##
    elif menu == "5":   # 조건 검사
        
        quantity = int(input("수량 :")) # 수량을 quantity 변수에 저장
        
        # 딕셔너리 형태로 주문 정보 저장 
        order = {
                "메뉴": "콜라",
                "가격": 2000,
                "수량": quantity
                }    
        
        order_list.append(order)
        
        print("콜라가 장바구니에 담겼습니다.")
        

    ## 6. 주문 내역 조회 ##
    elif menu == "6":   # 조건 검사
        
        # 주문이 없으면 출력
        if len(order_list) == 0:
            print("주문 내역이 없습니다.")
            
        # 주문이 있으면 출력
        else:
            print("\n======주문 내역=======")
            
            # 리스트에 저장된 주문을 하나씩 출력
            for data in order_list:
                # 메뉴명 출력
                print(f"메뉴 : {data['메뉴']}")
                
                # 가격 출력
                print(f"가격 : {data['가격']}원")
                
                # 수량 출력
                print(f"수량 : {data['수량']}개")
                
                # 가격 * 수량 계산
                print(f"금액 : {data['가격'] * data['수량']}원")
                
                print("-" * 20)
                
                
    ## 7. 결제 ##
    elif menu == "7":  # 조건 검사
        
        # 총 금액 저장 변수
        total = 0
        
        # 모든 주문 금액을 더한다.
        for data in order_list:
            
            total += data["가격"] * data["수량"]
        
        print("=" * 30)
        print(f"총 결제 금액 : {total:,}원")   # 총 결제 금액 결과값
        print("=" * 30)

    ## 8. 종료 ##
    elif menu == "8":  # 조건 검사
        
        print("프로그램을 종료합니다.")
        break # 반복문 종료

