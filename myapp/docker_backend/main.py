import strawberry
import uvicorn
import argparse

from fastapi import FastAPI

from config import DatabaseSession

from Graphql.query import Query
from Graphql.mutation import Mutation

from strawberry.fastapi import GraphQLRouter


def init_app():
    db = DatabaseSession()
    apps = FastAPI(
        title="yachtahn@gmail, Fast API, My First Test",
        description="Fast API",
        version="1.0.0",
    )

    @apps.on_event("startup")
    async def startup():
        await db.create_all()

    @apps.on_event("shutdown")
    async def shutdown():
        await db.close()

    @apps.get("/")
    def home():
        return "welcome home! this is fast api by 안동현"

    # add graphql endpoint
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    apps.include_router(graphql_app, prefix="/graphql")

    return apps


app = init_app()

# ArgumentParser를 생성하여 설명을 추가합니다.
parser = argparse.ArgumentParser(description="Run the FastAPI server.")
# 'port'라는 인자를 추가하고, 기본값을 설정합니다.
parser.add_argument("--port", type=int, default=8000, help="Port to listen on")
# 입력된 인자를 파싱합니다.
args = parser.parse_args()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=args.port, reload=True)


# 실행 시에는 다음 명령어로 실행을 한다.
# python ./myapp/docker_backend/main.py --port 5000
