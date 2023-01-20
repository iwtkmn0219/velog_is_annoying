from urllib.request import urlopen, Request
import re

f = open("text.txt", "w", encoding="utf8")

print("문제 번호를 입력하세요:", end=" ")
problem_number = int(input())

# Input problem number and get data
url = "https://www.acmicpc.net/problem/" + str(problem_number)
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urlopen(req)
boj_contents = str(html.read().decode("utf8"))

# Get text
TITLE_REGULAR_EXPRESSION = "(<title>)([\w\W]+)(</title>)"
boj_title = re.findall(TITLE_REGULAR_EXPRESSION, boj_contents)[0][1].split(": ")[1]
velog_title = f"[백준 Python] {problem_number}번 {boj_title}"
main_contents = f"[백준 {problem_number} {boj_title}]({url})"
PROBLEM_REGULAR_EXPRESSION = "(<h2>문제)([\s\S]+?)(</section>)"
problem = re.findall(
    "(<p>)([\s\S]+?)(</p>)", re.findall(PROBLEM_REGULAR_EXPRESSION, boj_contents)[0][1]
)
INPUT_REGULAR_EXPRESSION = "(<h2>입력)([\s\S]+?)(</section>)"
input_ = re.findall(
    "(<p>)([\s\S]+?)(</p>)", re.findall(INPUT_REGULAR_EXPRESSION, boj_contents)[0][1]
)
OUTPUT_REGULAR_EXPRESSION = "(<h2>출력)([\s\S]+?)(</section>)"
output = re.findall(
    "(<p>)([\s\S]+?)(</p>)", re.findall(OUTPUT_REGULAR_EXPRESSION, boj_contents)[0][1]
)

f.write(velog_title + "\n\n")
f.write("백준\npython\n\n")
f.write(main_contents + "\n\n")
f.write("## 문제\n")
for p in problem:
    f.write(p[1] + "\n\n")
f.write("## 입력\n")
for i in input_:
    f.write(i[1] + "\n\n")
f.write("## 출력\n")
for o in output:
    f.write(o[1] + "\n\n")
f.write("## 풀이 및 회고\n")
f.write("### 풀이\n\n")
f.write("### 회고\n\n")
f.write("## 코드\n```python\n\n```\n")
f.write(
    f"[>> iwtkmn0219의 Github <<](https://github.com/iwtkmn0219/boj/blob/main/python/{problem_number}.py)"
)
f.close()
