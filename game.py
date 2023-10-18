from typing import List
import typer

from computer_player import computer
from key_generator import hmac

app = typer.Typer()


@app.command()
def main(moves: List[str]):
    computer_player = computer.Computer(moves)
    secure_key = computer_player.get_initial_token()
    move = computer_player.get_move()
    move_hmac = hmac.HMAC(secure_key, move).generate()
    print(move_hmac, move, secure_key)


if __name__ == "__main__":
    app()
