from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    # 로그인 여부는 예시로 False를 사용. 실제 구현시 로직 추가
    is_logged_in = False

    # GraphQL 서버
    url = "http://localhost:8888/graphql"

    # GraphQL 쿼리. 이 부분은 실제 쿼리에 맞게 수정되어야 합니다.
    query = """
    {
        getAllGameinfos {
            id
            start
            finish
            playTimeMin
            netPlayer
            netBuyin
            netGameFee
            netBbozzi
        }
    }
    """

    # GraphQL 쿼리 요청 수행
    response = requests.post(url, json={"query": query})
    json_data = response.json()

    # 데이터 추출 (에러 처리는 실제 구현에서 고려되어야 함)
    gameinfos = json_data["data"]["getAllGameinfos"]

    # 템플릿 렌더링 및 데이터 전달
    return render_template("index.html", is_logged_in=is_logged_in, gameinfos=gameinfos)


if __name__ == "__main__":
    app.run(debug=True)
