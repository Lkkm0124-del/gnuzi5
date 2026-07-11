import streamlit as st
import random

st.title("✌️ 가위바위보")

with st.expander("📖 게임 방법", expanded=True):
    st.markdown("""
    ### 게임 규칙

    - 가위, 바위, 보 중 하나를 선택합니다.
    - 컴퓨터도 랜덤으로 하나를 선택합니다.
    - 승패 규칙

      - 가위 ✌️ > 보 ✋
      - 바위 ✊ > 가위 ✌️
      - 보 ✋ > 바위 ✊

    - 컴퓨터를 이기면 승리입니다!
    """)

choices = ["가위", "바위", "보"]

user = st.radio(
    "선택하세요",
    choices,
    horizontal=True
)

if st.button("대결하기"):

    computer = random.choice(choices)

    st.write(f"👤 당신 : {user}")
    st.write(f"🤖 컴퓨터 : {computer}")

    if user == computer:
        st.success("🤝 무승부!")

    elif (
        (user == "가위" and computer == "보")
        or
        (user == "바위" and computer == "가위")
        or
        (user == "보" and computer == "바위")
    ):
        st.balloons()
        st.success("🎉 승리!")

    else:
        st.error("😢 패배!")
