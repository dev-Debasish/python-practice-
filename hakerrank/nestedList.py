# data = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     data.append([name, score])
#     data.score.sort()
 
# print(data)


if __name__ == "__main__":
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
        
    print(data)
    
    # step-1: sort the list by scores
    sorted_score = sorted(data, key = lambda x: x[1])
    
    # step-2: Extract unique scores
    unique_scores = sorted(set(x[1] for x in sorted_score))
    
    if len(unique_scores) > 1 :
        second_lowest_score = unique_scores[1]
    else: 
        second_lowest_score = None
        
    
    if second_lowest_score is not None:
        names_with_second_score = [x[0] for x in sorted_score if x[1] == second_lowest_score]
    else:
        names_with_second_score = []
        
    # output
    names_with_second_score.sort()
    for name in names_with_second_score:
        print(name)
      