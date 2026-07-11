import streamlit as st
import random

st.title("🔢 업앤다운 게임")

with st.expander("📖 게임 방법", expanded=True):
    st.markdown("""
    ### 게임 규칙

    - 컴퓨터는 1~100 사이의 숫자를 하나 정합니다.
    - 숫자를 입력하고 확인 버튼을 누릅니다.
    - 입력한 숫자가 정답보다 작으면

      ⬆️ UP

    - 입력한 숫자가 정답보다 크면

      ⬇️ DOWN

    - 최대 20번 안에 정답을 맞혀야 합니다.
    - 20번 안에 맞히면 승리!
    """)

MAX_TRY = 20

if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.count = 0
    st.session_state.game_over = False

st.write(f"⏳ 남은 기회 : {MAX_TRY - st.session_state.count}")

guess = st.number_input(
    "숫자 입력",
    min_value=1,
    max_value=100,
    step=1,
    disabled=st.session_state.game_over
)

if st.button(
    "확인",
    disabled=st.session_state.game_over
):

    st.session_state.count += 1

    if guess < st.session_state.answer:
        st.warning("⬆️ UP!")

    elif guess > st.session_state.answer:
        st.warning("⬇️ DOWN!")

    else:
        st.success(
            f"🎉 정답! {st.session_state.count}번 만에 성공!"
        )
        st.balloons()
        st.session_state.game_over = True

    if (
        st.session_state.count >= MAX_TRY
        and not st.session_state.game_over
    ):
        st.error(
            f"💀 게임 오버! 정답은 {st.session_state.answer}였습니다."
        )
        st.session_state.game_over = True

if st.button("🔄 새 게임"):

    st.session_state.answer = random.randint(1, 100)
    st.session_state.count = 0
    st.session_state.game_over = False

    st.rerun()
