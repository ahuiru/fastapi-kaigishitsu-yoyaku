import streamlit as st
import datetime
import uuid
import requests
import json

page = st.sidebar.selectbox('Chose your page', ['users', 'rooms', 'bookings'])

if page == "users":
  st.title('ユーザー登録画面')
  with st.form(key='user'):
    # user_id: str = str(uuid.uuid4())[:8]
    user_name: str = st.text_input('ユーザー名', max_chars=12)
    data = {
      # 'user_id': user_id,
      'user_name': user_name
    }
    submit_button = st.form_submit_button(label='ユーザー登録')

  if submit_button:
    url = 'http://127.0.0.1:8000/users'
    res = requests.post(
      url,
      data=json.dumps(data)
      # data=json.dumps(data)
    )
    if res.status_code == 200:
      st.success('ユーザー登録完了')
    st.write(res.status_code)
    st.json(res.text)
elif page == "rooms":
  st.title('会議室登録')

  with st.form(key='room'):
    room_id: str = str(uuid.uuid4())[:8]
    room_name: str = st.text_input('会議室名', max_chars=12)
    capacity: int = st.number_input('定員', step=1)
    data = {
      "room_id": room_id,
      'room_name': room_name,
      "capacity": capacity
    }
    submit_button = st.form_submit_button(label='会議室予約')

  if submit_button:
    st.write('## 送信データ')
    st.json(data)
    st.write('## レスポンス結果')
    url = 'http://127.0.0.1:8000/rooms'
    res = requests.post(
      url,
      data=json.dumps(data)
    )
    if res.status_code == 200:
      st.success('会議室登録完了')
    st.write(res.status_code)
    st.json(res.text)
elif page == "bookings":
  st.title('APIテスト画面（会議室）')

  with st.form(key='booking'):
    user_id: int = 1
    room_id: int = 1
    booked_num: int = st.number_input('予約人数', step=1)
    date: datetime.datetime = st.date_input('日付:', min_value=datetime.date.today())
    start_datetime: datetime.datetime = st.time_input('開始時刻:', value=datetime.time(hour=9, minute=0))
    end_datetime: datetime.datetime = st.time_input('終了時刻:', value=datetime.time(hour=20, minute=0))

    data = {
      "booking_id":booking_id,
      "user_id":user_id,
      "room_id":room_id,
      "booked_num":booked_num,
      "start_datetime":datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=start_datetime.hour,
        minute=start_datetime.minute,
      ).isoformat(),
      "end_datetime":datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=end_datetime.hour,
        minute=end_datetime.minute,
      ).isoformat(),
    }
    submit_button = st.form_submit_button(label='リクエスト送信')

  if submit_button:
    st.write('## 送信データ')
    st.json(data)
    st.write('## レスポンス結果')
    url = 'http://127.0.0.1:8000/bookings'
    res = requests.post(
      url,
      data=json.dumps(data)
    )
    st.write(res.status_code)
    st.json(res.json())
