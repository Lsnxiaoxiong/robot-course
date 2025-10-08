
# 写入文件（覆盖写入模式 "w"）
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("第一行：Hello, Python!\n")
    f.write("第二行：这是文件写入示例。\n")

print("写入完成！")

# 追加写入模式 "a"
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("第三行：追加内容。\n")

print("追加完成！")

# 读取文件所有内容
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("文件内容如下：")
print(content)

# 一行一行读取
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("读取到一行：", line.strip())


# 读取所有行到列表
with open("example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("文件行列表：", lines)

import os

if os.path.exists("example.txt"):
    print("文件存在！")
else:
    print("文件不存在！")