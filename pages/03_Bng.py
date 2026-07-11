import streamlit as st

st.title("🎯 2인용 빙고")

with st.expander("📖 게임 방법", expanded=True):
    st.markdown("""
    ### 게임 규칙

    - 두 명이 번갈아 플레이합니다.
    - 플레이어 1 : O
    - 플레이어 2 : X

    ### 승리 조건

    아래 중 하나를 먼저 완성하면 승리!

    - 가로 3칸
    - 세로 3칸
    - 대각선 3칸

    먼저 1빙고를 만드는 사람이 승리합니다.
    """)

if "board" not in st.session_state:
    st.session_state.board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

if "turn" not in st.session_state:
    st.session_state.turn = "O"

if "winner" not in st.session_state:
    st.session_state.winner = None


def check_bingo(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def board_full(board):

    for row in board:
        for cell in row:
            if cell == "":
                return False

    return True


st.subheader(f"현재 차례 : {st.session_state.turn}")

for row in range(3):

    cols = st.columns(3)

    for col in range(3):

        value = st.session_state.board[row][col]

        label = value if value else "⬜"

        if cols[col].button(
            label,
            key=f"{row}_{col}",
            disabled=(
                value != ""
                or st.session_state.winner is not None
            )
        ):

            current = st.session_state.turn

            st.session_state.board[row][col] = current

            if check_bingo(
                st.session_state.board,
                current
            ):
                st.session_state.winner = current

            else:
                st.session_state.turn = (
                    "X"
                    if current == "O"
                    else "O"
                )

            st.rerun()

if st.session_state.winner:

    st.balloons()

    st.success(
        f"🎉 플레이어 {st.session_state.winner} 승리!"
    )

elif board_full(st.session_state.board):

    st.warning("🤝 무승부!")

if st.button("🔄 새 게임"):

    st.session_state.board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    st.session_state.turn = "O"
    st.session_state.winner = None

    st.rerun()
