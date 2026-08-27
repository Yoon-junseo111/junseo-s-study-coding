## 가계부 프로그램 ##

# 무한 반복

# 사용자가 종료를 하기 전 까지 계속 메뉴를 보여준다.
income_list = []    # 여러 개의 수입을 저장할 리스트
expense_list = []   # 여러 개의 지출을 저장할 리스트



while True:  # 항상 참을 보여준다.
    print("=" * 30)          # 메뉴 출력
    print("가계부 프로그램")
    print("=" * 30)
    print("1. 수입 추가")
    print("2. 지출 추가")
    print("3. 내역 조회")
    print("4. 잔액 조회")
    print("5. 종료")
    
    # # 사용자에게 메뉴 번호를 입력받는다.
    # menu = input("메뉴 선택 : ")
    
    # # 사용자가 1을 입력했을 때
    # if menu == "1":
    #     print("수입 추가 기능은 준비중 입니다.")
        
    # # 사용자가 2를 입력했을 때
    # elif menu == "2" :
    #      print("지출 추가 기능은 준비중 입니다.")
    
    # # 사용자가 3을 입력했을 때
    # elif menu == "3" :
    #     print("내역 조회 기능은 준비중 입니다.")

    # # 사용자가 4를 입력했을 때
    # elif menu == "4" :
    #     print("잔액 조회 기능은 준비중 입니다.")
           
    # # 사용자가 5를 입력했을 때
    # elif menu == "5" :
    #     print("프로그램을 종료합니다.")
    #     break # 반복문 종료
        
# 1~5번이 아닌 다른 값을 잘못 입력했을 때
    # else : 
    #     print("잘못된 입력입니다. 1~5번 중에서 입력해주세요")
# ================================
# 가계부 프로그램
# ==============================
# 1. 수입 추가
# 2. 지출 추가
# 3. 내역 조회
# 4. 잔액 조회
# 5. 종료
# 메뉴 선택 : 1
# 수입 추가 기능은 준비중 입니다.       
    # input() 은 문자열(str)로 저장된다.                  
    menu = input("메뉴 선택 :")


    # 1. 수입 추가
    if menu == "1":
        
        money = int(input("수입 금액 : "))    # int를 사용하는 이유는 계산을 하기 위해 숫자로 변환하기 위해서이다.
        memo = input("메모 : ")               # 메모 입력
        
        # 딕셔너리 형태로 저장
        income = {"금액" : money,
                "메모" : memo}
        

        income_list.append(income)    # 수입 리스트에 추가
        
        print("수입이 등록되었습니다.")
        
    ## 2. 지출 추가 ##

    elif menu == "2":
        
        money = int(input("지출 금액 : "))  # 숫자로 변환
        memo = input("메모 :")
        
        # 딕셔너리 형태로 저장
        expense = {"금액" : money,
                "메모" : memo}
        
        expense_list.append(expense)    # 지출 리스트에 추가
        
        print("지출이 등록되었습니다.")
        
        
    ## 3. 거래 내역 조회 ##
    elif menu == "3" :
        
        print("\n===== 수입 내역 ======")
        # 저장된 수입이 없을 경우
        if len(income_list) == 0:            # income_list의 길이가 0이면 수입이 없는 상태
            print("등록된 수입이 없습니다")
        
        # 저장된 수입이 있을 경우
        else:                                      # 저장된 수입이 있을 경우
            for data in income_list:
                print(f"금액 : {data['금액']}원")   # 현재 거래의 금액 값을 출력
                print(f"메모 : {data['메모']}")     # 현재 거래의 메모 값을 출력
                print("-" * 20)                     # 구분선
                 
    ## 4. 잔액 조회 ##
    elif menu == "4" :
        # 총 수입과 총 지출을 저장할 변수
        total_income = 0     
        total_expense = 0
        
        # 총 수입 계산
        for data in income_list:               # income_list에 저장된 데이터를 하나씩 꺼낸다. , data는 딕셔너리 하나에 저장
            total_income += data["금액"]       # 수입 리스트를 반복하면서 금액을 모두 더한다.
        
        # 총 지출 계산
        for data in expense_list:             # 리스트에 저장된 지출을 하나씩 꺼낸다.
            total_expense += data["금액"]     # 지출 리스트를 반복하면서 금액을 모두 더한다.
         
        # 잔액 계산   
        balance = total_income - total_expense
            
                
        print("\n===== 잔액 조회 ======")
        print(f"총 수입 : {total_income:,}원")
        print(f"총 지출 : {total_expense:,}원")
        print(f"현재 잔액 : {balance:,}원")
        
    ## 5. 종료 ##
    elif menu == "5" :
        print("프로그램을 종료합니다")
        break   # while 반복문을 종료한다.

    ## 잘못 입력했을 때 ##
    else:
        print("잘못된 메뉴입니다")
        


     
            
