import numpy as np
from score_analyzer import ScoreAnalyzer
a = np.array([70, 80, 90])
b = np.array([55, 65, 60])
c = np.array([40, 100, 70])
d = np.array([75, 80, 70])
e = np.array([65, 65, 65])
analyzer = ScoreAnalyzer(np.array([a, b, c, d, e]))
print("学生ごとの平均点",analyzer.calculate_student_averages())
print("科目ごとの平均点",analyzer.calculate_subject_averages())
print("合計点が最も高い学生のインデックス",analyzer.get_top_student_index())