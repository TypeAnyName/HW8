import json
import random


class Question:
    def __init__(self, question_, difficulty, correct_ans):
        self.question_ = question_
        self.difficulty = difficulty
        self.correct_ans = correct_ans

    def __repr__(self):
        return "Вопрос"

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.difficulty) * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if user_input == self.correct_ans:
            return True
        else:
            return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде"""
        print(self.question_)
        print(f"Сложность {self.difficulty}/5")

    def build_feedback(self):
        if check_question is True:
            print(f"Ответ верный, получено {points} баллов")
            correct.append(1)
        else:
            print(f"Ответ неверный, верный ответ {self.correct_ans}")


total_points = 0
questions = []
correct = []


def build_list():
    with open("questionshw8.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            questions.append(Question(i["q"], i['d'], i['a']))


def print_statistic():
    return f"Вот и всё!\nПравильных ответов: {len(correct)} из 10\nБаллов набранно: {total_points}"


if __name__ == "__main__":
    print("Здравствуйте! Вам Будет предложено 10 вопросов разной сложности.\nНачнаем!\n")
    add_to_list = build_list()
    for i in range(10):
        quest = random.choice(questions)
        quest.build_question()
        user_input = input()
        check_question = quest.is_correct()
        points = quest.get_points()
        quest.build_feedback()
        if check_question is True:
            total_points += points
        questions.remove(quest)
        print("")
    print(print_statistic())
