from mongoengine import Document, StringField, IntField, ListField, BooleanField


class Game(Document):
    player = StringField(max_length=40)
    complete = BooleanField(required=True, default=False)
    difficulty_level = StringField(choices=['Easy', 'Medium', 'Hard'])
    solution_word = StringField(max_length=255)
    num_guesses = IntField(min_value=0, max_value=10)
    guessed_letters = ListField(StringField(max_length=1))
    num_hints_used = IntField(min_value=0, max_value=3)
