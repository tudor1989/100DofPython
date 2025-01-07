student_scores = [139, 190, 165, 125, 181, 107, 157, 67, 187, 33, 178, 130, 90, 138, 156, 85, 169, 194, 179, 121]

max_score = 0 
for score in student_scores:
  if score > max_score:
    max_score = score
print(max_score)
