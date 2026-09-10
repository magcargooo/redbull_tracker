import streamlit as st
import json
from datetime import date
try:
    with open("records.json", "r") as file:
        records = json.load(file)
except FileNotFoundError:
    records = []
for record in records:
    record["date"] = date.fromisoformat(record["date"])   
st.title("Red Bull Tracker")
tab1, tab2 = st.tabs(["記録する", "記録を見る"])
with tab1:
    count = st.number_input("本数", min_value=1, step=1)
    capacity = st.selectbox("容量", [250, 330, 335, 473])
    flavor = st.selectbox("種類", ["オリジナル", "シュガーフリー", "グレープ", "マスカット", "チェリー", "すだち", "大宮オレンジソウル"])
    if st.button("記録する"):
        today = date.today()
        record = {"date": today,"flavor": flavor,"count": count,"capacity": capacity}
        records.append(record)

        save_records = []
        for record in records:
            save_record = {"date": str(record["date"]),"flavor": record["flavor"],"count": record["count"],"capacity": record["capacity"]}
            save_records.append(save_record)

        with open("records.json", "w") as file:
            json.dump(save_records, file)
        st.success("記録しました！")
with tab2:        
    st.subheader("記録一覧")
    total_count = 0
    for record in records:
        st.write("日付:", record["date"])
        st.write("種類",record["flavor"])
        st.write("本数",record["count"])
        st.write("容量",record["capacity"])
        total_count += record["count"]
    st.write("合計:" , str(total_count),"本") 

    st.subheader("月別集計")
    total_month=0
    selected_year = st.number_input("年", min_value=2020, step=1,key="month_year")
    selected_month = st.selectbox("月", [1,2,3,4,5,6,7,8,9,10,11,12])
    for record in records:
        if selected_year ==record["date"].year and selected_month==record["date"].month:
            total_month += record["count"]
    st.write(str(selected_year),"年",str(selected_month),"月","合計:" ,str(total_month,),"本")

    st.write("年別集計")
    total_year=0
    selected_year = st.number_input("年", min_value=2020, step=1,key="year_year")
    for record in records:
        if selected_year ==record["date"].year:
            total_year += record["count"]
    st.write(str(selected_year),"年","合計:" ,str(total_year,),"本")

    st.subheader("種類別集計")
    flavor_totals = {}
    for record in records:
        flavor = record["flavor"]
        if flavor not in flavor_totals:
            flavor_totals[flavor] = 0
        flavor_totals[flavor] += record["count"]
    for flavor in flavor_totals:
        st.write("種類名:",flavor,str(flavor_totals[flavor]),"本")
            
    st.subheader("月間種類別集計")
    monthly_flavor_totals={}
    selected_year = st.number_input("年", min_value=2020, step=1,key="monthly_flavor_year")
    selected_month = st.selectbox("月", [1,2,3,4,5,6,7,8,9,10,11,12],key="monthly_flavor_month")
    for record in records:
        if selected_year ==record["date"].year and selected_month==record["date"].month:
            flavor = record["flavor"]
            if flavor not in monthly_flavor_totals:
                monthly_flavor_totals[flavor] = 0
            monthly_flavor_totals[flavor] += record["count"]
    for flavor in monthly_flavor_totals:
        st.write(str(selected_year),"年",str(selected_month),"月","種類名:",flavor,str(monthly_flavor_totals[flavor]),"本")

    if monthly_flavor_totals:
        most_flavor = max(monthly_flavor_totals, key=monthly_flavor_totals.get)
        st.write(selected_year, "年", selected_month, "月:", "最多種類:", most_flavor, ":", monthly_flavor_totals[most_flavor], "本")
    else:
        st.write("この年月の記録はありません")
        
    st.subheader("年間最多種類")
    year_flavor_totals={}
    selected_year = st.number_input("年", min_value=2020, step=1,key="year_flavor_totals")
    for record in records:
        if selected_year ==record["date"].year:
            flavor = record["flavor"]
            if flavor not in year_flavor_totals:
                year_flavor_totals[flavor] = 0
            year_flavor_totals[flavor] += record["count"]
    for flavor in year_flavor_totals:
        st.write(str(selected_year),"年","種類名:",flavor,str(year_flavor_totals[flavor]),"本")

    if year_flavor_totals:
        most_flavor = max(year_flavor_totals, key=year_flavor_totals.get)
        st.write(selected_year, "年", "最多種類:", most_flavor, ":", year_flavor_totals[most_flavor], "本")
    else:
        st.write("この年の記録はありません")