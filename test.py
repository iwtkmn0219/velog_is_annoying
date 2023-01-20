from urllib.request import urlopen, Request
import re

# Get code
code = []
url = f"https://github.com/iwtkmn0219/boj/blob/main/python/{3005}.py"
print(url)
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
github_contents = str(urlopen(req).read().decode("utf8"))
LINE_REGULAR_EXPRESSION = "(<tr>)([\s\S]+?)(</tr>)"
lines = re.findall(LINE_REGULAR_EXPRESSION, github_contents)
# code = re.findall("(<span class=\"pl-token\"[\s\S]+?>)([\s\S]+?)(</span>)", code)
for line in lines:
    # print("-------------------------------")
    # print(line)
    # print(f'\'{line[1]}\'')
    tmp = line[1].replace("js-file-line\">", "js-file-line\">  ")
    # print(f'\'{tmp}\'')
    code_sector = re.findall("(>)([a-zA-Z\S\s\W\w]+?)(<)", tmp)
    # print("CODE IS:")
    for i in range(2, len(code_sector)):
        print(code_sector[i][1], end='')
    print()
    # print("-------------------------------")
