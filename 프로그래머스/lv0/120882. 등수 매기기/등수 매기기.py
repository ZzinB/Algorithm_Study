def solution(score):
    avg = [sum(i)/2 for i in score]
    score_avg = sorted(avg, reverse=True) 
    answer =[] 
    for i in avg:
        answer.append(score_avg.index(i)+1) 
    return answer