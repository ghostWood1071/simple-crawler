from playwright.sync_api import sync_playwright, Page, Browser, Locator
import json
import time
class Crawler():
    def __init__(self, pipeline) -> None:
        self.playwright = sync_playwright().start()
        self.browser:Browser = self.playwright.chromium.launch(channel="chrome", headless=False)
        self.page = self.browser.new_page(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        self.pipeline = pipeline
        self.results = []

    def get_from_file(self, input_val,**kwargs):
        file_name = kwargs.get("file_name")
        with open(file_name, mode='r') as f:
            data = json.loads(f.read())
        return data

    def goto(self, input_val=None, **kwargs) -> Locator:
        try:
            self.page.context.clear_cookies()
            if type(input_val) is str:
                self.page.goto(input_val)
            else:
                self.page.goto(kwargs.get("link"))
        except:
            pass
        if kwargs.get("delay"):
                time.sleep(kwargs.get("delay"))
        return self.page

    def select(self, input_val=None, **kwargs) -> Locator:
        if type(input_val) is Locator:
            return input_val.locator(kwargs.get("selector"))
        return self.page.locator(kwargs.get("selector"))
    
    def click(self, input_val=None, **kwargs):
        if type(input_val) is Locator:
            input_val.locator(kwargs.get("selector")).click()
        else:
            self.page.locator(kwargs.get("selector")).click()
        return self.page
    
    def scroll(self, input_val=None, **kwargs):
        self.page.press("End")
        if kwargs.get("wait"):
            time.sleep(int(kwargs.get("wait")))
        return input_val
    
    def getlinks(self, input_val=None, **kwargs):
        links = []

        origin = kwargs.get("origin") if kwargs.get("origin") else ""
        
        for index in range(input_val.count()):
            child = input_val.nth(index)
            links.append(f'{origin}{child.get_attribute("href")}') 
        return links
    
    def get_links_by_cond(self, input_val:Locator=None, **kwargs):
        links = []
        callback = kwargs.get("callback")
        link_expr = kwargs.get("link_selector")
        origin = kwargs.get("origin") if kwargs.get("origin") else ""
        
        for index in range(input_val.count()):
            child = input_val.nth(index)
            if callback(child):
                links.append(f'{origin}{child.locator(link_expr).get_attribute("href")}') 
        return links
        
    def foreach(self, input_val=None, **kwargs):
        for link in input_val:
            tmp_val = link
            for action in kwargs.get("actions"):
                try:
                    method = getattr(self, action.get("name"))
                    tmp_val = method(tmp_val, **action.get("params"))
                    time.sleep(kwargs.get("delay"))
                except Exception as e:
                    print("error: ", self.page.url)

    def get_detail(self, input_val:None, **kwargs):
        data = {}
        for key in list(kwargs.keys()):
            data[key] = ""
            text_parent = self.page.locator(kwargs.get(key))
            for index in range(text_parent.count()):
                data[key] += "\n" + text_parent.nth(index).inner_text()
            data[key] = data[key].strip("\n")
        data["url"] = self.page.url
        self.results.append(data)
    
    def get_table(self, input_val:None, **kwargs):
        data = {
            "name": kwargs.get("tbl_name"),
            "headers": [],
            "rows": []
        }
        header_selector = kwargs.get("header")
        row_selector = kwargs.get("row")
        cell_selector = kwargs.get("cell")
        headers = self.page.locator(header_selector)
        for i in range(headers.count()):
           data["headers"].append(headers.nth(i).inner_text())
        rows = self.page.locator(row_selector)
        for i in range(rows.count()):
            cells = rows.nth(i).locator(cell_selector)
            row = []
            for j in range(cells.count()):
                row.append(cells.nth(j).inner_text())
            data["rows"].append(row)
        self.results.append(data)

    def run(self):
        tmp_val = None
        for action in self.pipeline:
            method = getattr(self, action.get("name"))
            tmp_val = method(tmp_val, **action.get("params"))
        self.page.context.close()
        self.page.close()
        self.browser.close()
        self.playwright.stop()
        return self.results
