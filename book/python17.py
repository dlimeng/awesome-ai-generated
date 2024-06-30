import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(-2, 10, 500)
y1 = 0.5 * np.log(x + 2)  # 工业机器人
y2 = np.log(x + 2)  # 毛绒娃娃
y3 = np.log(x + 2) - 0.5  # 人形机器人
y4 = np.log(x + 2) - 1.5  # 健康人

# 绘制图像
plt.figure(figsize=(12, 8))

plt.plot(x, y1, label="工业机器人", linestyle='--', color="brown")
plt.plot(x, y2, label="毛绒娃娃", linestyle='--', color="brown")
plt.plot(x, y3, label="人形机器人", color="brown")
plt.plot(x, y4, label="健康人", linestyle='--', color="brown")

# 恐怖谷区域
plt.fill_between(x, -2, 0, where=(x > 4) & (x < 6), color='gray', alpha=0.3, label="恐怖谷")

# 添加标签和标题
plt.title("恐怖谷效应", fontsize=16)
plt.xlabel("逼真性", fontsize=14)
plt.ylabel("好感度", fontsize=14)

# 添加注释
plt.text(2, -0.2, "工业机器人", fontsize=12, verticalalignment='bottom')
plt.text(4.5, 0.7, "毛绒娃娃", fontsize=12, verticalalignment='bottom')
plt.text(5.5, -0.5, "人形机器人", fontsize=12, verticalalignment='bottom')
plt.text(8, 0.5, "健康人", fontsize=12, verticalalignment='bottom')
plt.text(6, -1.5, "尸体", fontsize=12, verticalalignment='top')
plt.text(5.2, -0.8, "僵尸", fontsize=12, verticalalignment='top')

plt.axhline(0, color='gray', linestyle='--')
plt.axvline(4, color='red', linestyle='--')
plt.axvline(6, color='red', linestyle='--')

# 添加图例
plt.legend()

# 显示图像
plt.grid(True)
plt.show()
