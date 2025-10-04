

from py2neo import Graph
import matplotlib.pyplot as plt


def bolt_connect():
    # 连接到 Neo4j 数据库，用 bolt 协议
    client = Graph("bolt://localhost:7687", user="neo4j", password="12345678")
    try:
        # 查询 Neo4j 中的所有节点
        result = client.run("MATCH (n) RETURN n LIMIT 5")

        # 打印查询结果
        print("Query Result:")
        for record in result:
            print(record)

        print("Connection successful and query executed!")

    except Exception as e:
        print(f"Error connecting to Neo4j: {e}")


def http_connect():
    try:
        # 通过 HTTP 协议连接到 Neo4j
        client = Graph("http://localhost:7474/", user="neo4j", password="12345678")

        # 测试连接，查询数据库版本
        version = client.run("RETURN 1 AS result").data()

        if version:
            print("Connection successful.")
        else:
            print("Connection failed.")
    except Exception as e:
        print(f"Error occurred: {e}")


def neo4j_connect():
    try:
        # 通过 HTTP 协议连接到 Neo4j
        client = Graph("neo4j://localhost:7687/", auth=("neo4j", "12345678"),name="medicine")

        # 测试连接，查询数据库版本
        version = client.run("RETURN 1 AS result").data()

        if version:
            print("Connection successful.")
        else:
            print("Connection failed.")
    except Exception as e:
        print(f"Error occurred: {e}")


def draw():
    # 数据
    percentages = [60.25, 55.55, 62.26, 75.25, 83.78, 85.36, 91, 86.7, 86.1, 88.2]
    weeks = [f"第{i + 1}周" for i in range(len(percentages))]  # 生成 "第1周", "第2周", ...

    # 创建柱状图
    plt.figure(figsize=(10, 6))
    plt.bar(weeks, percentages, color='skyblue')

    # 添加标题和标签
    plt.title("每周准确率柱状图")
    plt.xlabel("周次")
    plt.ylabel("准确率 (%)")

    # 显示图形
    plt.xticks(rotation=45)  # 让x轴的标签旋转，以便更清晰
    plt.tight_layout()  # 自动调整布局
    plt.show()




# 确保只有在直接运行脚本时才调用 main 方法
if __name__ == "__main__":
    bolt_connect()

    #http_connect()

    #neo4j_connect()

    #draw()


