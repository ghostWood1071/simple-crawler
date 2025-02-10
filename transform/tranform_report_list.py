import pandas as pd
import json
import traceback
from error.page_end_error import PageEndError


def process(data):
    price = data["report_list"]["data"]
    price = price[-5:]
    result = {}
    for id, item in enumerate(price):
        tmp_item = {f'{x}-{id}': y for x, y in item.items() if x in ["ReportDataID", "RowNumber"]}
        result.update(tmp_item)
    return result

