from textual.app import ComposeResult
from textual.widgets import Checkbox, Label
from textual.containers import HorizontalGroup

class ShortView(HorizontalGroup):
    """Short View

    The view to be used when viewing top level tasks
    as a list
    """
    def __init__(self) -> None:
        super().__init__()
        # Initialize attributes to ensure they exist
        self.checkbox = None
        self.heading = None
        self.description = None

    def compose(self) -> ComposeResult:
        self.checkbox = Checkbox()
        self.heading = Label("Testing Text", id="task_title")
        self.description = Label("Sub Text", id="task_description")
        yield self.checkbox
        yield self.heading
        yield self.description

    def update_labels(self, title: str, desc: str) -> None:
        self.heading.update(title)
        self.description.update(desc)

    def toggle_checkbox(self) -> None:
        self.checkbox.value = not self.checkbox.value