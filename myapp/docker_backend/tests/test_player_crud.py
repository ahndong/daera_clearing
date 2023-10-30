# tests/test_player_crud.py

from fastapi.testclient import TestClient
from main import app  # FastAPI 앱의 경로를 적절하게 수정하세요.

client = TestClient(app)


def test_create_player():
    # GraphQL 뮤테이션 정의
    mutation = """
    mutation createPlayer {
      createPlayer(
        playerData: {nickname: "test2", getBbozziRatio: 1.5, setBbozziRatio: 1.5}
      ) {
        id
        nickname
      }
    }
    """
    response = client.post("/graphql", json={"query": mutation})
    assert response.status_code == 200
    data = response.json()

    # 응답에서 player 정보 추출
    player = data.get("data", {}).get("createPlayer", {})

    assert player
    assert player["nickname"] == "test2"
    # ... 기타 검증 ...
