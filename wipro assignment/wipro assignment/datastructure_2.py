def find_runner_up(scores):
    
    unique_scores = set(scores)
    
    
    unique_scores.remove(max(unique_scores))
    
    
    return max(unique_scores)

# Example Usage:
scores_list = [2, 3, 6, 6, 5]
print(find_runner_up(scores_list)) 