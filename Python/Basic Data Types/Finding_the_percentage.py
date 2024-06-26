if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sc_sum = 0
    for score in student_marks[query_name]:
        sc_sum += score
    print("%.2f" % (sc_sum/len(student_marks[query_name])))