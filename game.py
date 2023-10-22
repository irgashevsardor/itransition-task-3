from typing import List
import typer
from rich import print
from rich.prompt import Prompt, Confirm

# from rich.console import Console
# from rich.table import Table
from computer import move
from key_generator import hmac
from game import rules
app = typer.Typer()


@app.command()
def main(moves: List[str]):
    """
    Generates HELP table
    """
    computer_move = move.Move(moves)
    init_secure_key = computer_move.get_initial_token()
    computer_move_choice = computer_move.get_move()
    computer_move_hmac = hmac.HMAC(
        init_secure_key, computer_move_choice).generate()
    print(f"HMAC: {computer_move_hmac}")
    user_move = Prompt.ask("Enter your move (0 to exit):",
                           choices=moves, default=0)

    game_rules = rules.Rule(moves, user_move, computer_move_choice)
    print(game_rules.define_winner())

    # if user_move == "0":
    #     is_user_exits = Confirm.ask(
    #         "[bold]Do you really want to exit the game?[/bold]")
    #     if is_user_exits:
    #         print("[bold red]Exiting the game. Goodbye![/bold red]")
    #         exit()
    print(f"Your move: {user_move}")
    print(f"Computer move: {computer_move_choice}")
    print(f"HMAC key: {init_secure_key}")


# @app.command()
# def colorful():
#     print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


# console = Console()


# @app.command()
# def table():
#     table = Table("Name", "Item")
#     table.add_row("Rick", "Portal Gun")
#     table.add_row("Morty", "Plumbus")
#     console.print(table)


if __name__ == "__main__":
    app()
