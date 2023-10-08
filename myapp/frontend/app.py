from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # 로그인 여부는 예시로 False를 사용. 실제 구현시 로직 추가
    is_logged_in = False
    return render_template("index.html", is_logged_in=is_logged_in)


if __name__ == "__main__":
    app.run(debug=True)
