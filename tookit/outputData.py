import json
import os

class OutputData:
    CONST_TXT = "txt"
    CONST_JSON = "json"
    CONST_CSV = "csv"
    STANDARD_LIST = [CONST_TXT, CONST_JSON, CONST_CSV]
    ENCODING_TYPE="utf-8"

    def __init__(self, filename, outputname, level="1", pattern="txt"):
        self.filename = filename
        self.outputname = outputname
        self.pattern = pattern if self.checkPatternStandard(pattern) else "txt"
        self.level = level

    def initFile(self):
        return

    def checkPatternStandard(self, pattern):
        return pattern in self.STANDARD_LIST

    def output(self, data):
        if self.pattern == self.CONST_TXT:
            self.outputTxt(data)
        elif self.pattern == self.CONST_JSON:
            self.outputJson(data)
        else:
            pass

    def outputTxt(self, data):
        with open(self.filename, 'a+', encoding=self.ENCODING_TYPE) as f:
            for i in data:
                f.write(str(i) + "\n")

    def readAllJsonData(self):
        if os.path.exists(self.filename) == False or os.path.getsize(self.filename) == 0:
            return []
        else:
            with open(self.filename, 'r+', encoding=self.ENCODING_TYPE) as load_f:
                if load_f:
                    load_dict = json.load(load_f)
                    return load_dict
        return []

    def outputJson(self, newdata):
        data = self.readAllJsonData()

        with open(self.filename, 'w+', encoding=self.ENCODING_TYPE) as load_f:

            if type(newdata) == dict:
                data.append(newdata)
            elif type(newdata) == list:
                for i in newdata:
                    data.append(i)

            json.dump(data, load_f, indent=4, ensure_ascii=False)
            load_f.close()

    def outputCsv(self):
        return


if __name__ == '__main__':
    output = OutputData("123", "json")
    output.outputJson([
        {
            "protocol": "https",
            "port": "443",
            "ip": "220.181.107.196",
            "domain": "baidu.com",
            "host": "https://test.baidu.com",
            "link": "https://test.baidu.com",
            "title": "百度众测 | 众包任务平台"
        },
        {
            "protocol": "http",
            "port": "80",
            "ip": "220.181.107.196",
            "domain": "baidu.com",
            "host": "test.baidu.com",
            "link": "http://test.baidu.com",
            "title": ""
        }
    ])