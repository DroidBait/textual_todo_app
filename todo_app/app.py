from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Checkbox, Header, Footer, Label
from textual.events import Key
import logging
from textual.logging import TextualHandler
from textual.containers import HorizontalGroup, VerticalScroll
from shortview import ShortView

logging.basicConfig(
    level="NOTSET",
    handlers=[TextualHandler()],
)

class ChecklistApp(App):
    CSS_PATH = "todo.tcss"
    BINDINGS = [
        ("t", "toggle_dark", "Toggle dark mode"),
        ("q", "quit_app", "Quit"),
        ("d", "toggle_done", "Complete?"),
        ]

    def compose(self) -> ComposeResult:
        """Compose the layout of the app."""
        # Create an empty ListView
        yield Header()
        self.list_view = ListView()
        yield Footer()
        yield self.list_view

    async def on_mount(self) -> None:
        """Populate the ListView after it has been mounted."""
        #items = [f"Item {i}" for i in range(1, 21)]  # Example items
        #for item in items:
        #    self.list_view.append(ListItem(Checkbox(label=item)))
        data = [
            ("Title 1", "Description 1"),
            ("Title 2", "Description 2"),
        ]

        for title, description in data:
            task = ShortView()

            await self.list_view.append(ListItem(task))
            task.update_labels(title, description)

    def on_key(self, event: Key) -> None:
        """Handle key press events."""
        # if event.key == "d":  # If the 'd' key is pressed
        pass
    
    def action_toggle_done(self) -> None:
        # Check the currently selected index in the ListView
        selected_index = self.list_view.index

        if selected_index is not None:  # If there's a valid selected index
            # Get the corresponding ListItem
            selected_item = self.list_view.children[selected_index]

            if isinstance(selected_item, ListItem):
                # Access the ShortView inside the ListItem
                short_view = next(
                    (child for child in selected_item.children if isinstance(child, ShortView)),
                    None
                )

                if short_view:  # If a ShortView instance is found
                    short_view.toggle_checkbox()  # Toggle its checkbox

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    
    def action_quit_app(self) -> None:
        """Close the application"""
        exit()

if __name__ == "__main__":
    app = ChecklistApp()
    app.run()