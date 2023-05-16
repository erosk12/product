import streamlit as st
import requests

# Google 스프레드시트 ID 지정
spreadsheet_id = '1RodiRk48wJ3UbjZeFRdWx9a1bAgBGhpItBt8GanhTDc'

# 제품 목록 가져오기
def get_products():
    response = requests.get('https://docs.google.com/spreadsheets/d/{}/export?format=csv'.format(spreadsheet_id))
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
    requests.post('https://docs.google.com/spreadsheets/d/{}/edit?usp=sharing'.format(spreadsheet_id),
                  data={'valueInputOption': 'RAW', 
                        'range': 'A1',
                        'value': product_name + ',' + price + ',' + flavor + ',' + purchase_location})

# 애플리케이션 UI
st.title('전통주 찾기')

# 제품 검색
product_name = st.text_input('제품명을 입력하세요:')
if st.button('검색'):
    product = search_product(product_name)
    if product:
        st.write('제품 정보:', product)
    else:
        st.write('제품을 찾을 수 없습니다.')

# 제품 등록
if st.button('등록'):
    product_name = st.text_input('제품명:')
    price = st.text_input('가격:')
    flavor = st.text_input('맛:')
    purchase_location = st.text_input('구입처:')
    with st.form('register_product'):
        if st.form_submit_button('등록'):
            register_product(product_name, price, flavor, purchase_location)
            st.write('제품이 등록되었습니다.')
