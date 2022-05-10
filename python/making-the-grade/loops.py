def round_scores(student_scores):
    """Round all the scores in a list

    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))

    return rounded_scores


def count_failed_students(student_scores):
    """calculate how many students failed

    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    number_of_failed_scores = 0
    for score in student_scores:
        if score <= 40:
            number_of_failed_scores += 1

    return number_of_failed_scores


def above_threshold(student_scores, threshold):
    """List the best scores according to a threshold

    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)

    return best_scores


def letter_grades(highest):
    """Return the relative value of letter grades

    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    span_between_grades = round((highest - 40) / 4)
    scores = [41]
    for i in range(3):
        scores.append(scores[i] + span_between_grades)

    return scores


def student_ranking(student_scores, student_names):
    """Create a list of student rank names and scores

    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """

    rank = 0
    ranking_list = []
    for score in student_scores:
        ranked_name = f"{rank + 1}. {student_names[rank]}: {score}"
        ranking_list.append(ranked_name)
        rank += 1

    return ranking_list


def perfect_score(student_info):
    """Find the students that scored a 100

    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    students_with_100 = []
    for student in student_info:
        if 100 in student:
            students_with_100.extend(student)
            return students_with_100

    return students_with_100
