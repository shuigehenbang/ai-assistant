# 功能1：自我介绍
def introduce():
    print("你好，我是AI助手。\n我可以帮你记录个人信息。")

# 功能2：记录信息
def record():
    data = {
        "name": input("请输入姓名："),
        "job": input("请输入职业："),
        "goal": input("请输入学习目标：")
    }

    import json
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 功能3：查看信息
def view():
    import json
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"你好，{data['name']}")
        print(f"你的职业是：{data['job']}")
        print(f"你的学习目标是：{data['goal']}")