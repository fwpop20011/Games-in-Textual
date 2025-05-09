from textual.css.query import NoMatches
from textual.widgets import ListView, Label, ListItem
from textual.app import ComposeResult

class GameList(ListView):
    """A list of games."""
    def compose(self) -> ComposeResult:
        yield ListItem(Label("TicTacToe"), id="list-game-tictactoe")
        yield ListItem(Label("test"))

    def action_select_cursor(self) -> None:
        """Opens selected game."""
        from Games.TicTacToe.TicTacToeWidget import Board3x3

        highlighted = self.highlighted_child
        if highlighted and highlighted.id == "list-game-tictactoe":
            try:
                if not self.app.query_one(Board3x3):
                    self.app.mount(Board3x3())
                else:
                    self.app.query_one(Board3x3).remove()
            except NoMatches:
                self.app.mount(Board3x3())