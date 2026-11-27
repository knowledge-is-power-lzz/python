scores = []
print("请输入成绩(最多10个,输入-1结束):")
while len(scores) < 10:
    score = int(input(f"第{len(scores)+1}个成绩："))
    if score == -1:
        break
    scores.append(score)

counts = {"优": 0, "良": 0, "中": 0, "及格": 0, "不及格": 0}

for s in scores:
    if s >= 90:
        counts["优"] += 1
    elif s >= 80:
        counts["良"] += 1
    elif s >= 70:
        counts["中"] += 1
    elif s >= 60:
        counts["及格"] += 1
    else:
        counts["不及格"] += 1

for k, v in counts.items():
    print(f"{k}:{v} 人")
