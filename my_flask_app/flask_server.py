from flask import Flask, request, jsonify, render_template
import os
import json

app = Flask(__name__)

# Flask 템플릿 경로를 명시적으로 설정
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# JSON 데이터를 저장할 파일 이름
JSON_FILE = 'received_data.json'

@app.route('/')
def home():
    return "Welcome to the Flask server!"

@app.route('/display', methods=['GET'])
def display_data():
    try:
        # JSON 파일에서 데이터 읽기
        with open(JSON_FILE, 'r') as file:
            data_list = [json.loads(line) for line in file]
    except FileNotFoundError:
        data_list = []
    except json.JSONDecodeError:
        return "Error decoding JSON data.", 500

    # 템플릿 렌더링
    return render_template('data.html', data_list=data_list)

if __name__ == '__main__':
    # Flask 서버 실행
    app.run(port=7001, debug=False)
