import requests

url = 'https://finance.vietstock.vn/data/GetReportDataDetailValueByReportDataIds'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'language=vi-VN; Theme=Light; AnonymousNotification=; _cc_id=83e45c2d0dcd2986e89238607da15e7f; dable_uid=69769416.1737454022882; vst_isShowTourGuid=true; panoramaId_expiry=1739259983020; panoramaId=251f301233e3b0b4652ce1a13032185ca02c1f72afa20622ce4dc6af06095828; panoramaIdType=panoDevice; _gid=GA1.2.330408573.1738655882; isShowLogin=true; ASP.NET_SessionId=jb1ldzdg5tqwzkku3bf2o2ph; __RequestVerificationToken=3V_sJzzohjlPSn3UhTTlViAB9gELb_C5WA9Jzyuihoe5lfD7qxfHHyc1hF9oJeW5qmE3RNjyRajxWPfH2YBdlTesgncYheNfGcJX7Kr7gBk1; vts_usr_lg=C8DCE14B1683AF0069293259236CF695AA0D3AFF92942585561D4A9D359894A80D9955E393DAC85D8B34470509D7985F70FA90CB9D0116E0B935477B848D932882C64F265F177E06F72D445F39AB63BC4B727B3D861ACE9B115CBEB7E5C3EF2D20EACF84F392F941E0B7C62866BBAB88BE486520E8652B02AE933E47770F2924; vst_usr_lg_token=6XJMHzSTr0WF1wi4u4pwEg==; finance_viewedstock=VCB,; _gat_UA-1460625-2=1; FCNEC=%5B%5B%22AKsRol8mqcMsGZ9-7OqX3y9X9a0CMjf1I4v9cFd6RY22BJzZjTdrwDtEmzW6JTaBNzIxHXfNFCd1yApKNZfoRZDOjKiN1us19UBXQAtxCXjJjcjmLFXH8ieDlfZil7ms56kQwPeBhxa6TEET6x_R2Biq7FoBzsT1yg%3D%3D%22%5D%5D; __gads=ID=8881e7114534e6df:T=1737454010:RT=1738736931:S=ALNI_MZ6gmnvnIZQpRinNlxnu9s8bkiO-w; __gpi=UID=000010025ee1d5c7:T=1737454010:RT=1738736931:S=ALNI_MY8_dChnqdyNqr0pyc3h2Les6DtYw; __eoi=ID=c8bba028bcf14297:T=1737454010:RT=1738736931:S=AA-AfjY3M9vBh_peoZrY6ACJwgyM; cto_bundle=9q6NW19RcU1iT0JiZnZYVXNyVnZlVExoaEc3NTJ5UkEzbVlxJTJCRzJSTzRzcSUyRnlNRXQwMnJxT0slMkJWQU92NWhoODdPYmlodEpDeDZWRCUyQmpiUjU4OFhtMlB4ZnlSYXhjMEJkSHBCNm1MaHhicTBueSUyQiUyQkNqRiUyRkt6dVo0RXJzeU1UWEtuWVp1ZHVFOVRiQ3FQRk9TTjBzZWpLZnZHRm50NDMlMkZKcnRDQnVvYVA1RiUyRjRpbVYxbEdRWG1Zc01QNUtnJTJCUGY3WVRwWEN6JTJGM0lYTnVvTFhqaXNxNmFYT1ZuZyUzRCUzRA; _ga=GA1.2.1607150910.1737454008; _ga_EXMM0DKVEX=GS1.1.1738736928.5.1.1738736974.14.0.0; cto_bundle=hnOPyl9RcU1iT0JiZnZYVXNyVnZlVExoaEc5JTJCcGFaJTJCM1dUb0UlMkJZNUtkb3lmcHE1Zm81TlhlQTRVMW9nbCUyQiUyQiUyRmFMbTVqNzlGYkF6N1IwMVBMa3ZzZFpIdHZ2R2pQekJOcHRwNHFydmtNJTJGJTJGbkZRNEVtb2RCU1k4eUVidVNrNCUyRnJ0ZVhWUW1PWWhjenRxMDRqbjd5V3pTNG9XSzBTQVdkWm9wV2J1a3M5NSUyQmc2a0RZWnVBbjlJbUNIUXJFJTJCN01yUSUyQjBlbzRGeTZtYXFVUzZLSDJwVDZrejRORm9nJTNEJTNE; cto_bidid=wqCclV9BYWszRElteFolMkJCZ211MkxoQkhQNCUyRkp4ZG9PQ0QlMkY5S0RyQlBjd3ZtS3hoMnclMkYwUThwNGVNbDFvS2pCdFBjOWpnclFrbHhkUjlVSnZRQU9FWjBNJTJCcE01NzBtOTczRFlhUSUyRnlTWmI2OVA3byUzRA',
    'Origin': 'https://finance.vietstock.vn',
    'Referer': 'https://finance.vietstock.vn/VCB/tai-chinh.htm?tab=CDKT',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'StockCode': 'VCB',
    'Unit': '1000000000',
    'listReportDataIds[0][Index]': '0',
    'listReportDataIds[0][ReportDataId]': '243465',
    'listReportDataIds[0][IsShowData]': 'true',
    'listReportDataIds[0][RowNumber]': '60',
    'listReportDataIds[0][YearPeriod]': '2023',
    'listReportDataIds[0][TotalCount]': '64',
    'listReportDataIds[0][SortTimeType]': 'Time_ASC',
    'listReportDataIds[1][Index]': '1',
    'listReportDataIds[1][ReportDataId]': '256180',
    'listReportDataIds[1][IsShowData]': 'true',
    'listReportDataIds[1][RowNumber]': '61',
    'listReportDataIds[1][YearPeriod]': '2024',
    'listReportDataIds[1][TotalCount]': '64',
    'listReportDataIds[1][SortTimeType]': 'Time_ASC',
    'listReportDataIds[2][Index]': '2',
    'listReportDataIds[2][ReportDataId]': '252264',
    'listReportDataIds[2][IsShowData]': 'true',
    'listReportDataIds[2][RowNumber]': '62',
    'listReportDataIds[2][YearPeriod]': '2024',
    'listReportDataIds[2][TotalCount]': '64',
    'listReportDataIds[2][SortTimeType]': 'Time_ASC',
    'listReportDataIds[3][Index]': '3',
    'listReportDataIds[3][ReportDataId]': '258433',
    'listReportDataIds[3][IsShowData]': 'true',
    'listReportDataIds[3][RowNumber]': '63',
    'listReportDataIds[3][YearPeriod]': '2024',
    'listReportDataIds[3][TotalCount]': '64',
    'listReportDataIds[3][SortTimeType]': 'Time_ASC',
    'listReportDataIds[4][Index]': '4',
    'listReportDataIds[4][ReportDataId]': '262546',
    'listReportDataIds[4][IsShowData]': 'true',
    'listReportDataIds[4][RowNumber]': '64',
    'listReportDataIds[4][YearPeriod]': '2024',
    'listReportDataIds[4][TotalCount]': '64',
    'listReportDataIds[4][SortTimeType]': 'Time_ASC',
    '__RequestVerificationToken': 'HBU-Q7ej1dJksYL8O_q3OjGaRBlOpohMMM37A0nzweq3LVzj1iAVcfA-NnBJhHzDb5X4hY4_b8c-84LjvV7tvjuYt2xO772uXq9sNFPDuiueV_UfHc_TYlne_zelelEe0'
}

response = requests.post(url, headers=headers, data=data)

print(response.text)