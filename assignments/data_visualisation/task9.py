import matplotlib.pyplot as plt
import numpy as np

study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [45, 50, 55, 60, 68, 72, 78, 85, 90, 95]
assignment_scores = [40, 48, 52, 58, 63, 67, 73, 80, 85, 88]

plt.figure(figsize=(8, 6))

plt.scatter(
    study_hours,
    exam_scores,
    color='blue',
    marker='o',
    label='Exam Scores'
)

plt.scatter(
    study_hours,
    assignment_scores,
    color='red',
    marker='^',
    label='Assignment Scores'
)

plt.title('Study Hours vs Performance')
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.legend()
plt.grid(True)

plt.show()

exam_corr = np.corrcoef(study_hours, exam_scores)[0, 1]
assignment_corr = np.corrcoef(study_hours, assignment_scores)[0, 1]

print("Correlation (Study Hours vs Exam Scores):", round(exam_corr, 3))
print("Correlation (Study Hours vs Assignment Scores):", round(assignment_corr, 3))

plt.savefig("dashboard.png")
plt.savefig("dashboard.pdf")
plt.savefig("dashboard.svg")

plt.savefig(
    "dashboard_high_resolution.png",
    dpi=300
)
