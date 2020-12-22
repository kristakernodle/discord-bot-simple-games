from mongoengine import connect
from .Game import Game


def get_solution_word():
    return "solution"


def create_output_image():
    return "https://res.cloudinary.com/maynerdy/image/upload/v1608598133/hangman/gallows.jpg"


def start_game(ctx, difficulty_level='Easy'):
    game = Game(player=str(ctx.author),
                complete=False,
                difficulty_level='Easy',
                solution_word=get_solution_word(),
                num_guesses=0,
                guessed_letters=None,
                num_hints_used=0)

    return create_output_image()


def existing_unfinished_game(player):
    connect(alias='default', db='hangman-games')
    games_for_player = Game.objects(player=player)
    if len(games_for_player.all()) == 0:
        return False
    else:
        try_this = games_for_player.filter(complete=False).all()
        pass
