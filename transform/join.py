import pandas as pd
import json
import traceback
from error.page_end_error import PageEndError


def process(data):
    try:
        price = data["price"]["Data"]["Data"]
        statistic = data["statistic"]["Data"]["Data"]
        khoingoai = data["khoingoai"]["Data"]["Data"]
        tudoanh = data["tudoanh"]["Data"]["Data"]["ListDataTudoanh"]

        data_names = ["price", "statistic", "khoingoai", "tudoanh"]
        check_page_end = False
        for name in data_names:
            check_page_end = check_page_end or (len(locals().get(name)) > 0)
        if not check_page_end:
            raise PageEndError()

        price_df = pd.DataFrame(price)
        statis_df = pd.DataFrame(statistic)
        khoingoai_df = pd.DataFrame(khoingoai)
        tudoanh_df = pd.DataFrame(tudoanh)

        price_df = price_df.rename(columns={"Ngay": "Date"})
        khoingoai_df = price_df.rename(columns={"Ngay": "Date"})

        dataframes = [price_df, statis_df, khoingoai_df, tudoanh_df]

        for df in dataframes:
            if not df.empty:
                df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

        result = pd.DataFrame()
        for df in dataframes:
            if df.empty:
                continue
            if result.empty:
                result = df
                continue
            common_columns = set(result.columns).intersection(df.columns) - {"ThayDoi"}
            print("Common columns:", common_columns)
            result = pd.merge(result, df, on=list(common_columns), how="outer")

        result = result.drop(
            columns=[col for col in result.columns if col.startswith("ThayDoi_")]
        )

        result["Date"] = result["Date"].dt.strftime("%d/%m/%Y")
        result_json = result.to_json(orient="records")
        # result_json = json.dumps(result.to_dict(orient="records"))
    except PageEndError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
    
    return result_json
