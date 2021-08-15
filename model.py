from dataclasses import dataclass
from tinydb import TinyDB, Query

DB_PATH = 'mvc-todo-db.json'
db = TinyDB(DB_PATH)


@dataclass
class poll:
    question: str
    answers: dict


class PollModelWrapper:
    polls_table = db.table('polls')

    @classmethod
    def get_by_question(cls, question: str):
        """
        :param question: get a  question for poll
        :return:Returns the ????
        """
        return cls.polls_table.search(Query().question == question)

    def get_by_answers(cls, question: str):
        """
        :param question: get a  question for poll
        :return:Returns the ????
        """
        return cls.polls_table.search(Query().question == question) #[answers]

    @classmethod
    def create(cls, question: str):
        """
        :param question: Get a question and put it in db
        """
        if cls.get_by_question(question):
            return
            #cls.polls_table.update({'count': cls.get_by_number(number)[0]['count']+1}, Query().number == number)
        else:
            cls.polls_table.insert({"question": question, "answers": {}})

    @classmethod
    def get_all(cls):
        """
        :return: return all polls table
        """
        return cls.polls_table.all()

    @classmethod
    def update(cls, question: str, answer: str):
        answers = cls.get_by_answers(question)
        for a, b in answers:
            if a == answer:
                b =+1
        cls.polls_table.update({'answers': answers}, Query().question == question)


