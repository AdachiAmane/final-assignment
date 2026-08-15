import numpy as np
class ScoreAnalyzer:
    def __init__(self, score_data):
        self.score_data = score_data
    
    def calculate_student_averages(self):
        return np.mean(self.score_data, axis = 1)
    
    def calculate_subject_averages(self):
        return np.mean(self.score_data, axis = 0)
    
    def get_top_student_index(self):
        return np.argmax(np.sum(self.score_data, axis = 1))