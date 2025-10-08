# 写入文件（覆盖写入模式 "w"）
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("第一行：Hello, Python!\n")
    f.write("第二行：这是文件写入示例。\n")

print("写入完成！")