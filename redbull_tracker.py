import json
from datetime import date 
def integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except:
            print("数字を入力してください")
def add_record(records):
        today = date.today()
        while True:
            count = integer("本数を入力してください：")
            if count >= 1:
                break
            else:
                print("1以上を入力してください")    
        while True:
            capacity = integer("容量を入力してください：")
            if capacity >= 250:
                break
            else:
                print("現状国内流通最小サイズは250mlです")
        flavors = ["オリジナル", "シュガーフリー", "パープル"]
        index = 1
        for flavor in flavors:
            print(str(index) + ". " + flavor)
            index += 1
        while True:
            flavor = integer("種類を入力してください：")
            if flavor >= 1 and flavor <= 3:
                selected_flavor = flavors[flavor - 1]
                break
            else:
                print("1〜3を入力してください")
        record= {"date" : today,"flavor": selected_flavor,"count": count,"capacity": capacity}
        records.append(record)
        save_records = []
        for record in records:
            save_record = {
    "date": str(record["date"]),
    "flavor": record["flavor"],
    "count": record["count"],
    "capacity": record["capacity"]
}
            save_records.append(save_record)
        with open("records.json", "w") as file:    
            json.dump(save_records, file)
            print("JSON保存完了")
        print("記録を追加します")
        print("日付:"+str(today))
        print("種類:"+selected_flavor)
        print("本数:"+str(count)+"本")
        print("容量:"+str(capacity)+"ml")
        
def show_records(records):
    total_count=0
    print("=== 記録一覧 ===")
    for record in records:
        print("日付:"+str(record["date"]))
        print("種類:"+record["flavor"])
        print("本数:"+str(record["count"])+"本")
        print("容量:"+str(record["capacity"])+"ml")
        total_count+=record["count"]
    print("合計:" + str(total_count)+"本")
    
def show_monthly_total(records):
        monthly_total = 0
        selected_year = integer("年を入力してください：")

        while True:
                selected_month = integer("月を入力してください：")
                if 1 <= selected_month <= 12:
                    break
                else:
                    print("正しい日付を入力してください")

        for record in records:
            if record["date"].year == selected_year and record["date"].month == selected_month:
                monthly_total += record["count"]
        print("=== 月別 ===")
        print(str(selected_year)+"年"+str(selected_month)+"月:"+str(monthly_total)+"本")
    
def show_year_total(records):
    year_total = 0
    selected_year = integer("年を入力してください：")
    for record in records:
        if  record["date"].year== selected_year:
            year_total+=record["count"]
    print("=== 年別 ===")
    print(str(selected_year)+"年:"+str(year_total)+"本")
    
def show_flavor_total(records):
            original=0
            sugarfree=0
            purple=0
            for record in records:
                if record["flavor"]=="オリジナル" :
                    original+=record["count"]
                if record["flavor"]=="シュガーフリー":
                    sugarfree+=record["count"]
                if record["flavor"]=="パープル":
                    purple+=record["count"]
            print("=== 種類別 ===")
            print("オリジナル:"+str(original)+"本")
            print("シュガーフリー:"+str(sugarfree)+"本")
            print("パープル:"+str(purple)+"本")
            
def show_monthly_flavor_total(records):
                selected_year = integer("年を入力してください：")
                while True:
                    selected_month = integer("月を入力してください：")
                    if 1 <= selected_month <= 12:
                            break
                    else:
                        print("1〜12を入力してください")
                original=0
                sugarfree=0
                purple=0
                for record in records:
                    if record["flavor"]=="オリジナル"and record["date"].year == selected_year and record["date"].month == selected_month:
                        original+=record["count"]
                    if record["flavor"]=="シュガーフリー"and record["date"].year == selected_year and record["date"].month == selected_month:
                        sugarfree+=record["count"]
                    if record["flavor"]=="パープル"and record["date"].year == selected_year and record["date"].month == selected_month:
                        purple+=record["count"]
                print("=== 種類別 ===")
                print("オリジナル:"+str(original)+"本")
                print("シュガーフリー:"+str(sugarfree)+"本")
                print("パープル:"+str(purple)+"本")
                
def show_monthly_most_flavor(records):
                selected_year = integer("年を入力してください：")
                while True:
                    selected_month = integer("月を入力してください：")
                    if 1 <= selected_month <= 12:
                        break
                    else:
                        print("1〜12を入力してください")
                original=0
                sugarfree=0
                purple=0
                for record in records:
                    if record["flavor"]=="オリジナル"and record["date"].year == selected_year and record["date"].month == selected_month:
                        original+=record["count"]
                    if record["flavor"]=="シュガーフリー" and record["date"].year == selected_year and record["date"].month == selected_month:
                        sugarfree+=record["count"]
                    if record["flavor"]=="パープル" and record["date"].year == selected_year and record["date"].month == selected_month:
                        purple+=record["count"]
                print("==="+str(selected_year)+"年"+str(selected_month)+"月"+"で一番飲んだ種類 ===")
                if original >= sugarfree and original >= purple:
                    print("オリジナル:" + str(original) + "本")
                elif sugarfree >= original and sugarfree >= purple:
                    print("シュガーフリー:"+str(sugarfree)+"本")
                else:
                    print("パープル:"+str(purple)+"本")
                    
def show_year_most_flavor(records):
            selected_year = integer("年を入力してください：")
            original=0
            sugarfree=0
            purple=0
            for record in records:
                if record["date"].year== selected_year and record["flavor"]=="オリジナル":
                    original+=record["count"]
                if record["date"].year== selected_year and record["flavor"]=="シュガーフリー":
                    sugarfree+=record["count"]
                if record["date"].year== selected_year and record["flavor"]=="パープル":
                    purple+=record["count"]
            print("==="+str(selected_year)+"年"+"で一番飲んだ種類 ===")
            if original >= sugarfree and original >= purple:
                print("オリジナル:" + str(original) + "本")
            elif sugarfree >= original and sugarfree >= purple:
                print("シュガーフリー:"+str(sugarfree)+"本")
            else:
                print("パープル:"+str(purple)+"本")
    
                
try:
    with open("records.json", "r") as file:
        records = json.load(file)
except FileNotFoundError:
    records = []
for record in records:
    record["date"] = date.fromisoformat(record["date"])    
print("=== Red Bull Tracker ===")
while True:
    while True:
        selected_number = integer("1.飲んだ記録を追加 2.記録を見る 3.終了")

        if 1 <= selected_number <= 3:
            break
        else:
            print("正しい数字を入力してください")
            
    if selected_number==1:
        add_record(records)

        
    elif selected_number == 2:
        print("=== 記録を見る ===")

        while True:   
            while True:  
                sub_number = integer("1.記録一覧 2.月別集計 3.年別集計 4.全期間種類別 5.月間種類別 6.月間最多種類 7.年間最多種類 8.戻る")

                if 1 <= sub_number <= 8:
                    break
                else:
                    print("正しい数字を入力してください")
        
            if sub_number==1:  
                show_records(records)
        
            elif sub_number==2:
                show_monthly_total(records)

            elif sub_number==3:
                show_year_total(records)
            
            elif sub_number==4:
                show_flavor_total(records)
        
            elif sub_number==5:
                show_monthly_flavor_total(records)
            
            elif sub_number==6:
                show_monthly_most_flavor(records)

            elif sub_number == 7:
                show_year_most_flavor(records)
                
            elif sub_number == 8:
                print("戻ります")
                break

       
    elif selected_number==3:
        print("終了します")
        break
    else: 
        print("正しい番号を入力してください")