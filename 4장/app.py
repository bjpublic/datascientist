from flask import Flask # 플라스크 사용을 위한 라이브러리 

app = Flask(__name__) # 주요 함수가 실행될 때 변수(app) 설정 

data = {"IDs": ["A", "B", "C", "D"]} 

@app.route('/') # / 경로에 응답할 함수
def hello():
    return 'Hello, World!'

@app.route('/ID/<name>') # /ID/<name> 경로에 응답할 함수
def ID(name):
    if name in data["IDs"]: # name이 데이터에 있는 경우
        return f'Thank you for visiting again, {name}!'
    else: # name이 데이터에 없는경우
        return f'Hi, {name}!'

if __name__ == '__main__': # localhost:8081 서버 app 열기 
    app.run(host='0.0.0.0', port=8081) 
