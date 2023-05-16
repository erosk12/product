import streamlit as st
import requests
import datetime

# Google 스프레드시트 ID 및 공개 API 키 지정
spreadsheet_id = '1RodiRk48wJ3UbjZeFRdWx9a1bAgBGhpItBt8GanhTDc'
public_key = 'AIzaSyAvZuCVIZnf8brFXxfbQQr2sX-yYD4ib_Q'

# 제품 목록 가져오기
def get_products():
    response = requests.get('https://sheets.googleapis.com/v4/spreadsheets/{}/values?key={}&range=A1:A'.format(spreadsheet_id, public_key))
    products = response.content.decode('utf-8').splitlines()
    return products

# 제품 검색
def search_product(product_name):
    products = get_products()
    for product in products:
        if product.startswith(product_name):
            return product
    return None

# 제품 등록
def register_product(product_name, price, flavor, purchase_location):
    requests.post('https://sheets.googleapis.com/v4/spreadsheets/{}/values?key={}&append=true&valueInputOption=RAW&range=A1'.format(spreadsheet_id, public_key),
                  data={'values': [[product_name, price, flavor, purchase_location, str(datetime.datetime.now())]]})

# 애플리케이션 UI
st.title('제품 찾기')

# 제품 검색
product_name = st.text_input('제품명을 입력하세요:')
if st.button('검색'):
    product = search_product(product_name)
    if product:
        st.write('제품 정보:', product)
    else:
        st.write('제품을 찾을 수 없습니다.222ㄹㄹㄹㄹㄹ')

# 제품 등록
if st.button('등록'):
    with st.form('register_product'):
        product_name = st.text_input('제품명:')
        price = st.text_input('가격:')
        flavor = st.text_input('맛:')
        purchase_location = st.text_input('구입처:')
        if st.form_submit_button('등록'):
            register_product(product_name, price, flavor, purchase_location)
            st.write('등록이 완료되었습니다.')
