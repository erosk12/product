import streamlit as st
import pandas as pd

# 앱 제목 설정
st.title("제품 평가 애플리케이션")

# 제품 정보 입력 양식 생성
product_info = st.form("제품 정보")
product_name = product_info.text_input("제품명")
product_brand = product_info.text_input("브랜드")
product_type = product_info.text_input("유형")

# 맛 평가 입력 양식 생성
tasting_notes = st.form("맛 평가")
sweetness = tasting_notes.slider("단맛", 0, 10, step=0.1)
sourness = tasting_notes.slider("신맛", 0, 10, step=0.1)
refreshness = tasting_notes.slider("상쾌함", 0, 10, step=0.1)
body = tasting_notes.slider("바디감", 0, 10, step=0.1)
aroma = tasting_notes.slider("향", 0, 10, step=0.1)
alcohol_content = tasting_notes.number_input("알코올 도수", 0, 100)
price = tasting_notes.number_input("가격", 0, 100)
purchase_location = tasting_notes.text_input("구매처")

# 제출 버튼을 클릭하면 데이터를 Google 스프레드시트에 저장합니다.
if st.form_submit_button("제출"):
    # 현재 날짜와 시간을 가져옵니다.
    now = pd.Timestamp.now()

    # 데이터를 데이터 프레임으로 저장합니다.
    data = {
        "제품명": product_name,
        "브랜드": product_brand,
        "유형": product_type,
        "단맛": sweetness,
        "신맛": sourness,
        "상쾌함": refreshness,
        "바디감": body,
        "향": aroma,
        "알코올 도수": alcohol_content,
        "가격": price,
        "구매처": purchase_location,
        "날짜": now
    }
    df = pd.DataFrame(data)

    # 스프레드시트가 없으면 생성합니다.
    try:
        df.to_excel("products.xlsx", sheet_name="Ratings")
    except FileNotFoundError:
        with pd.ExcelWriter("products.xlsx") as writer:
            df.to_excel(writer, sheet_name="Ratings")

    # 데이터를 표시합니다.
    st.write("제품 정보:")
    st.write(product_name)
    st.write(product_brand)
    st.write(product_type)

    st.write("맛 평가:")
    st.write(sweetness)
    st.write(sourness)
    st.write(refreshness)
    st.write(body)
    st.write(aroma)
    st.write(alcohol_content)
    st.write(price)
    st.write(purchase_location)

    # 이전에 동일한 제품을 평가한 기록이 있는지 확인합니다.
    if product_name in df["제품명"].unique():
        # 동일한 제품의 이전 평가를 표시합니다.
        st.write("이전 평가:")
        st.dataframe(df[df["제품명"] == product_name])
    else:
        # 동일한 제품의 이전 평가가 없습니다.
        st.write("이 제품에 대한 이전 평가가 없습니다.")

# 제출 버튼을 생성합니다.
submit_button = st.form_submit_button("제출")
