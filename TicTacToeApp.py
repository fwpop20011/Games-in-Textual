from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from GameList import GameList

class TicTacToeApp(App):
    """A Textual app for tictactoe."""
    CSS_PATH = "TicTacToe.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield GameList()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"

if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
