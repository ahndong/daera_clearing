# tests/test_player_crud.py

from fastapi.testclient import TestClient
from main import app  # FastAPI 앱의 경로를 적절하게 수정하세요.

from datetime import datetime
import random

client = TestClient(app)

# 현재 시간과 난수를 조합하여 고유한 nickname 생성
current_time_str = datetime.now().strftime("%Y%m%d%H%M%S")
random_number = random.randint(100, 999)
unique_nickname = f"test_{current_time_str}_{random_number}"


def test_create_player():
    # GraphQL 뮤테이션 정의
    mutation = f"""
    mutation createPlayer {{
      createPlayer(
        playerData: {{nickname: "{unique_nickname}", getBbozziRatio: 1.5, setBbozziRatio: 1.5}}
      ) {{
        id
        nickname
      }}
    }}
    """
    response = client.post("/graphql", json={"query": mutation})
    assert response.status_code == 200
    data = response.json()

    # 응답에서 player 정보 추출
    player = data.get("data", {}).get("createPlayer", {})

    assert player
    assert player["nickname"] == unique_nickname
    # ... 기타 검증 ...
