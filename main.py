"""
========== AI Assistant ==========

你好，我是 AI 助手。

1. 自我介绍
2. 记录信息
3. 查看信息
4. 退出

请选择：
"""
# 菜单骨架
while True:
    print("========== AI Assistant ==========\n")
    print("你好，我是 AI 助手。\n")
    print("1. 自我介绍")
    print("2. 记录信息")
    print("3. 查看信息")
    print("4. 退出\n")

    choice = input("请选择：")
    
    import json
    try:
        if choice == "1":
            print("这里以后写自我介绍功能")
            from assistant import introduce
            introduce()
        elif choice == "2":
            print("这里以后写记录功能")
            from assistant import record
            record()
        elif choice == "3":
            print("这里以后写查看功能")
            from assistant import view
            view()
        elif choice == "4":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入。")

    except FileNotFoundError:
        print("没有找到用户资料，请先选择“记录信息”")

    except json.JSONDecodeError:
        print("JSON 解析错误，请检查数据文件格式。")
    

    