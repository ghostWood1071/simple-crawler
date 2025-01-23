from bs4 import BeautifulSoup
import json

class HTMLToJson:
    def __init__(self, HTMLContent):
        self.HTMLContent = HTMLContent

    def ConvertToJson(self):
        soup = BeautifulSoup(self.HTMLContent, 'html.parser')
        items = soup.select('ul.News_Title_Link li')

        list_item = []
        for item in items:
            time = item.select_one('.timeTitle').text.strip() if item.select_one('.timeTitle') else None
            title = item.select_one('a').get('title', '').strip() if item.select_one('a') else None 
        
            list_item.append({
                'Time': time,
                "Title": title
            })

        return json.dumps(list_item, ensure_ascii=False)