import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
st.set_page_config(  # Disable Streamlit's rerun behavior
    layout="wide",
    page_title="Water Usage",
    page_icon="🚰"
)

# Google Sheets configuration
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Myproject.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('Morning Meeting Task List').sheet1

# Streamlit form
st.title('Water Usage Form')
st.markdown(
    """
    <style>
    body {
        background-image: url('background_image.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Date field
current_date = datetime.date.today()
date_str = st.date_input('Date', value=current_date).strftime('%Y-%m-%d')
# date = st.date_input('Date', value=current_date)

# Water Input section
st.subheader('Water Input')
idc_water_1 = st.text_input('IDC Water-1')
idc_water_2 = st.text_input('IDC Water-2')
water_tanker=st.text_input('Water Tanker ')
rain_water_r_d=st.text_input('Rain Water R and D')
rain_water_main_building=st.text_input('Rain Water Main Building')

# Industrial Usage section
st.subheader('Industrial Usage')
paint_shop = st.text_input('Paint Shop')
r_and_d = st.text_input('R & D')
tl_press_cooling_tower = st.text_input('TL Press Cooling Tower')
fl_tl_line = st.text_input('FL/TL Line')
fl_ca_lab = st.text_input('FL CA Lab')
tl_ca_lab = st.text_input('TL CA Lab')
solar_panel_cleaning = st.text_input('Solar Panel Cleaning')
injection_moulding_press_cooling_tower = st.text_input('Injection Moulding / Press Cooling Tower')
filteration_water_cycle=st.text_input('Filteration Water Fresh')
filteration_water_recycle=st.text_input('Filteration Recycle')
ro_system=st.text_input('RO System [R/D]')

# Non Industrial Usage section
st.subheader('Non Industrial Usage')
r_d_toilet = st.text_input('R/D Toilet')
r_d_water_intake = st.text_input('R/D Water Intake')
mkt_office_toilet = st.text_input('Mkt/Office Toilet')
operator_toilet_1 = st.text_input('Operator Toilet 1')
operator_toilet_2 = st.text_input('Operator Toilet 2')
canteen_service_center = st.text_input('Canteen/Service Center')
paint_shop_toilet=st.text_input('Paint Shop Toilet')
canteen_kitchen=st.text_input('Canteen Kitchen')
main_gate_security=st.text_input('Main Gate Security')

# Submit button
if st.button('Submit'):
    if not all([date_str, idc_water_1, idc_water_2, paint_shop, r_and_d, tl_press_cooling_tower,
            fl_tl_line, fl_ca_lab, tl_ca_lab, solar_panel_cleaning,
            injection_moulding_press_cooling_tower, r_d_toilet, r_d_water_intake,
            mkt_office_toilet, operator_toilet_1, operator_toilet_2, canteen_service_center,water_tanker,
            rain_water_main_building,rain_water_r_d,ro_system,paint_shop_toilet,canteen_kitchen,
            main_gate_security,filteration_water_cycle,filteration_water_recycle]):
        st.error('Please fill in all fields.')
    else:   
        if not sheet.get('A1'):
            column_names=['Date', 'idc_water_1', 'idc_water_2', 'paint_shop', 'r_and_d', 'tl_press_cooling_tower',
            'fl_tl_line', 'fl_ca_lab', 'tl_ca_lab', 'solar_panel_cleaning',
            'injection_moulding_press_cooling_tower', 'r_d_toilet', 'r_d_water_intake',
            'mkt_office_toilet', 'operator_toilet_1', 'operator_toilet_2', 'canteen_service_center','water_tanker',
            'rain_water_main_building','rain_water_r_d','ro_system','paint_shop_toilet','canteen_kitchen',
            'main_gate_security','filteration_water_cycle','filteration_water_recycle']
            sheet.insert_row(column_names, index=1)
        # Store the form data in Google Sheets
        row = [date_str, idc_water_1, idc_water_2, paint_shop, r_and_d, tl_press_cooling_tower,
            fl_tl_line, fl_ca_lab, tl_ca_lab, solar_panel_cleaning,
            injection_moulding_press_cooling_tower, r_d_toilet, r_d_water_intake,
            mkt_office_toilet, operator_toilet_1, operator_toilet_2, canteen_service_center,water_tanker,
            rain_water_main_building,rain_water_r_d,ro_system,paint_shop_toilet,canteen_kitchen,
            main_gate_security,filteration_water_cycle,filteration_water_recycle]
        sheet.append_row(row)
        st.success('Data Uploaded successfully!')



