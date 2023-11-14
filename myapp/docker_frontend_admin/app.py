import pandas as pd
import streamlit as st
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# GraphQL 클라이언트 설정
transport = RequestsHTTPTransport(url="http://localhost:8888/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)


def main():
    st.title("Player Management Dashboard")

    # CRUD 작업을 위한 탭 구성
    tab1, tab2, tab3, tab4 = st.tabs(["Read", "Create", "Update", "Delete"])

    with tab1:
        read_players()
    with tab2:
        create_player()
    with tab3:
        update_player()
    with tab4:
        delete_player()


def read_players():
    query = gql(
        """
        query getAllPlayers {
            getAllPlayers {
                createdAt
                nickname
                id
                noOfGames
            }
        }
    """
    )
    result = client.execute(query)
    players = result["getAllPlayers"]

    df = pd.DataFrame(players)

    # 각 행에 대한 삭제 버튼 추가
    for i in df.index:
        col1, col2 = st.columns([0.9, 0.1])
        player = df.iloc[i]
        with col1:
            st.text(f"{player['nickname']} ({player['id']})")
        with col2:
            if st.button("🗑️", key=f"delete_{player['id']}"):
                delete_player(player["id"])
                st.experimental_rerun()

    # # Streamlit에서 트리 형태로 결과 표시
    # st.write(players)


def create_player():
    with st.form("Create Player"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, step=1)
        submit_button = st.form_submit_button("Create Player")

        if submit_button:
            mutation = gql(
                """
                mutation CreatePlayer($name: String!, $age: Int!) {
                    createPlayer(name: $name, age: $age) {
                        player {
                            id
                            nickname
                        }
                    }
                }
            """
            )
            variables = {"name": name, "age": age}
            result = client.execute(mutation, variable_values=variables)
            st.success("Player created!")


def update_player():
    with st.form("Update Player"):
        player_id = st.text_input("Player ID")
        new_name = st.text_input("New Name")
        new_age = st.number_input("New Age", min_value=0, step=1)
        submit_button = st.form_submit_button("Update Player")

        if submit_button:
            mutation = gql(
                """
                mutation UpdatePlayer($id: ID!, $newName: String, $newAge: Int) {
                    updatePlayer(id: $id, name: $newName, age: $newAge) {
                        player {
                            id
                            name
                            age
                        }
                    }
                }
            """
            )
            variables = {"id": player_id, "newName": new_name, "newAge": new_age}
            result = client.execute(mutation, variable_values=variables)
            st.success("Player updated!")


def delete_player():
    with st.form("Delete Player"):
        player_id = st.text_input("Player ID")
        submit_button = st.form_submit_button("Delete Player")

        if submit_button:
            mutation = gql(
                """
                mutation DeletePlayer($id: ID!) {
                    deletePlayer(id: $id) {
                        player {
                            id
                        }
                    }
                }
            """
            )
            variables = {"id": player_id}
            result = client.execute(mutation, variable_values=variables)
            st.success("Player deleted!")


if __name__ == "__main__":
    main()
