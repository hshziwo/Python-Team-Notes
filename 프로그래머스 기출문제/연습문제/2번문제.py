# 성적이 배열로 주어질 때 각 성적의 등수를 배열로 반환, 동점은 같은 등수로 처리하고 그 다음 등수는 + 동점자수
# function solution2(grade) {
#     // 내림차순
#     const gradeInfo = [...grade].map((point, index) => ({point, index})).sort((a, b) => b.point - a.point || a.index - b.index);

#     const answer = [];
#     let sameRankCount = 0;
#     let curRank = 1;
#     for(let i = 0; i < gradeInfo.length; i++) {
#         // 동점자가 아닐 경우
#         if (i > 0 && gradeInfo[i].point < gradeInfo[i-1].point) {
#             curRank += sameRankCount;
#             sameRankCount = 0;
#         }
#         answer[gradeInfo[i].index] = curRank;
#         sameRankCount++;
#     }

#     console.log(answer);
# }

# const solution2Data = [30, 20, 30, 10, 100, 50, 60, 70, 50, 30, 20];

def solution2() :
    grade = [30, 20, 30, 10, 100, 50, 60, 70, 50, 30, 20]
    sorted_grade = sorted(grade, reverse=True)
    grade_rank = {}
    cur_rank = 0
    same_rank = 0
    for i in sorted_grade :
        if i not in grade_rank :
            cur_rank =  cur_rank + same_rank + 1
            same_rank = 0
            grade_rank[i] = cur_rank
        else :
            grade_rank[i] = cur_rank
            same_rank += 1
    
    answer = []
    for i in grade :
        answer.append(grade_rank[i])
    print(answer)

solution2()