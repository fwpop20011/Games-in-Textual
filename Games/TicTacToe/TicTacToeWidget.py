from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import HorizontalGroup, VerticalGroup
from textual.widget import Widget
from textual.widgets import Button

from Games.TicTacToe import TicTacToeGame


class Board3x3(HorizontalGroup):
    """3x3 board widget"""

    BUTTON_POSITION_MAP = {
        "t0": (0, 0), "t1": (0, 1), "t2": (0, 2),
        "t3": (1, 0), "t4": (1, 1), "t5": (1, 2),
        "t6": (2, 0), "t7": (2, 1), "t8": (2, 2)
    }

    BINDINGS = [
        ("r", "reset_game", "reset game"),
        Binding("up", "move_focus('up')", "Up", show=False),
        Binding("down", "move_focus('down')", "Down", show=False),
        Binding("left", "move_focus('left')", "Left", show=False),
        Binding("right", "move_focus('right')", "Right", show=False),
        ("q", "quit_game", "quit game"),
    ]

    def __init__(self, *children: Widget):
        super().__init__(*children)
        self.game_TicTacToe = TicTacToeGame.Game()

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            with HorizontalGroup():
                yield Button(" ", id = "t0")
                yield Button(" ", id = "t1")
                yield Button(" ", id = "t2")
            with HorizontalGroup():
                yield Button(" ", id = "t3")
                yield Button(" ", id = "t4")
                yield Button(" ", id = "t5")
            with HorizontalGroup():
                yield Button(" ", id = "t6")
                yield Button(" ", id = "t7")
                yield Button(" ", id = "t8")

    def action_reset_game(self) -> None:
        """Reset the game"""
        self.game_TicTacToe = TicTacToeGame.Game()

        # Reset all buttons to their initial state
        for button in self.query("Button"):
            button.label = " "
            button.styles.background = None
            button.add_class("default-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events"""
        button = event.button

        if button.label != " ":
            return

        if button.id in self.BUTTON_POSITION_MAP:
            row, col = self.BUTTON_POSITION_MAP[button.id]
            self.game_TicTacToe.place(row, col)
            button.label = self.game_TicTacToe.player_turn()

            if button.label == "X":
                button.styles.background = "red"
            else:
                button.styles.background = "blue"

        if self.game_TicTacToe.winner == 1:
            for btn in self.query("Button"):
                btn.styles.background = "blue"
        elif self.game_TicTacToe.winner == -1:
            for btn in self.query("Button"):
                btn.styles.background = "red"
        elif self.game_TicTacToe.winner == 0 and self.game_TicTacToe.turns == 9:
            for btn in self.query("Button"):
                btn.styles.background = "yellow"

    def on_mount(self) -> None:
        """Set initial focus to the first button when the app starts."""
        self.app.query_one("#t0").focus()

    def action_move_focus(self, direction: str) -> None:
        """Handle arrow key navigation between buttons."""
        # Map of button positions and where focus should move based on direction
        focus_map = {
            "t0": {"up": "t6", "down": "t3", "left": "t2", "right": "t1"},
            "t1": {"up": "t7", "down": "t4", "left": "t0", "right": "t2"},
            "t2": {"up": "t8", "down": "t5", "left": "t1", "right": "t0"},
            "t3": {"up": "t0", "down": "t6", "left": "t5", "right": "t4"},
            "t4": {"up": "t1", "down": "t7", "left": "t3", "right": "t5"},
            "t5": {"up": "t2", "down": "t8", "left": "t4", "right": "t3"},
            "t6": {"up": "t3", "down": "t0", "left": "t8", "right": "t7"},
            "t7": {"up": "t4", "down": "t1", "left": "t6", "right": "t8"},
            "t8": {"up": "t5", "down": "t2", "left": "t7", "right": "t6"},
        }

        # Get the ID of the currently focused button
        focused = self.app.focused
        if focused is None or not hasattr(focused, "id"):
            self.query_one("#t0").focus()
            return

        current_id = focused.id
        if current_id in focus_map and direction in focus_map[current_id]:
            # Focus the button in the specified direction
            next_id = focus_map[current_id][direction]
            self.query_one(f"#{next_id}").focus()

    def action_quit_game(self) -> None:
        """Close the TicTacToe board widget"""
        board = self.app.query_one(Board3x3)
        board.remove()