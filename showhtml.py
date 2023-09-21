def generate_html(file_path, output_path): # 랭킹txt 파일을 html에 띄우는 함수
    with open(file_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines() # txt파일의 line 읽기
    
    # HTML 생성
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: #333;
                text-align: center;
            }}
            
            .container {{
                max-width: 800px;
                margin: 0;
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
            }}
            
            p {{
                line-height: 1.5;
            }}
            
        </style>
    </head>
    <body>
        <div class="container">
            <h1>최종 순위</h1>
            <p>플레이한 게임의 최종 랭킹입니다. 자신의 순위 및 다른 사용자들의 순위를 확인하세요.   (하단에 있음)</p>
            <p>실제 사용자가 플레이한 코인의 그래프는 이 코인그래프를 유사하게 작성한 것입니다.</p>
            <img src='bitcoin_1.png' style="width: 1000px; height: 300px">
            <p>코인도 투자 中 하나지만, 추천을 안드리는 이유가 여러가지 있습니다.</p>
            <p>1. 중독성 : 게임처럼 보이지만, 큰 돈이 오고 나가기 떄문에 도박의 일종이고, 빠져나오기 쉽지 않습니다.</p>
            <p>2. 변동성 : 코인 가격이 예기치 않게 크게 변화합니다.</p>
            <p>3. 세력, 안전장치 X 등</p>
            <p>이 게임은 가상체험을 통하여 실제 돈을 쓰지 않으면서 코인의 위험성을 깨닫고, 접근하지 않게 하기 위하여 제작되었습니다.</p>
            <p>이 영상은 코인의 위험성에 대한 다큐멘터리 영상입니다.</p>
            <a href="https://www.youtube.com/watch?v=74koqD12jG0">2030 투자중독 실태 보고</a>
        </div>
        <pre>{}</pre> 
    </body>
    </html>
    """
    
    content = '\n'.join(lines) # txt 파일의 내용을 HTML에 삽입
    html_output = html_template.format(content)

    with open(output_path, 'w') as output_file:
        output_file.write(html_output) # HTML 파일 저장

generate_html('rankingdata.txt', 'ranking.html')

import http.server
import socketserver
import webbrowser

def open_html_file(file_path):
    
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}/{file_path}") # 기본 웹브라우저에 html 띄움
        httpd.serve_forever()    
    
open_html_file('ranking.html')