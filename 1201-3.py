#项目1
"""
score = [0,0,0,0,0,0,0,0,0,0]
print("请输入10位评委对选手的打分：")
for i in range(0,10):
    score[i] = int(input("请输入第%d位评委的得分："%(i+1)))
    if score[i] < 0 or score[i] > 100:
        score[i] = int(input("请输入第%d位评委的得分："%(i+1)))
score.sort()
num = (sum(score) - score[0] - score[9])/8
print("去掉一个最高分%d分，去掉一个最低分%d分，最终得分：%.2f"%(score[9],score[0],num))
"""
scores = []
count = int(input("请输入人数："))
for i in range(0,count):
    scores.append(0)
    scores[i] = int(input("请输入第%d位评委的得分："%(i+1)))
    if scores[i] < 0 or scores[i] > 10:
        scores[i] = int(input("输入错误，请输入第%d位评委的得分："%(i+1)))
scores.sort()
num = (sum(scores) - scores[0] - scores[-1])/(count-2)
print("去掉一个最高分%d分，去掉一个最低分%d分，最终得分：%.2f"%(scores[-1],scores[0],num))
