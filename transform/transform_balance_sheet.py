import pandas as pd
import json
import traceback
from error.page_end_error import PageEndError

def read_balance_schema():
    with open("test/result1.json", mode = "r", encoding="utf-8") as f:
       data = json.loads(f.read())
    data =  data["data"]
    return data

def convert_to_quarter(period):
    end_period = period.split('-')[1]
    year = int(end_period[:4])
    month = int(end_period[4:])
    quarter = (month - 1) // 3 + 1
    return f"Q{quarter}{year}"

def process(data):
    try:
        tbl1_data = read_balance_schema()
        df1 = pd.DataFrame(tbl1_data)
        tbl2_data = data['report_list']["data"]
        df2 = pd.DataFrame(tbl2_data)
        tbl3_data = data["balance_value"]["data"]
        df3 = pd.DataFrame(tbl3_data)
        ticker = data["ticker"]
        result = pd.merge(df1, df3)
        df_result = result[["ReportNormName","Value1","Value2","Value3","Value4","Value5"]]
        df2["PeriodRange"] = df2["PeriodBegin"].astype(str) + "-" + df2["PeriodEnd"].astype(str)
        df2 = df2[-5:]
        period_list = df2["PeriodRange"].to_list()
        cols_replace = ["Value1","Value2","Value3","Value4","Value5"]
        replace_cols_dict = {x:y for x, y in zip(cols_replace, period_list)}
        df_result = df_result.rename(columns = replace_cols_dict)
        id_vars = [df_result.columns[0]]
        value_vars = df_result.columns[1:]
        df_result = df_result.melt(id_vars=id_vars, value_vars=value_vars, var_name="report_id", value_name="value")
        df_result["report_id"] = ticker + "BCDKT" +df_result["report_id"].apply(convert_to_quarter)
        df_result = df_result.rename(columns={"ReportNormName": "account"})
        result = df_result.to_json(orient="records", force_ascii=False).encode("utf-8")
    except Exception as e:
        traceback.print_exc()
    return result

