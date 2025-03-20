from textual.app import App, ComposeResult
from textual.widgets import Label, Digits, Button
from textual.events import Key
import logging
from textual.logging import TextualHandler
from textual.containers import HorizontalGroup, VerticalScroll, VerticalGroup
from textual.reactive import reactive
from datetime import datetime, timedelta

class IncDecButtons(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield Button(label="Inc", variant="primary", id="btn_inc")
        yield Button(label="dec", variant="primary", id="btn_dec") 

class TimerOption(VerticalGroup):
    display_time = reactive("")  # Reactive variable for the timer display

    def __init__(self, default_length: int = 300, name:str = "") -> None:
        super().__init__()
        self.timer_length = default_length
        self.inc_dec_buttons = IncDecButtons()
        self.clock = Digits(value="None", id="display_time")
        self.display_name = str(name.replace("_", " "))
        self.clock_name = Label(self.display_name, id="clock_name")
        #self.clock_name.styles.text_align = "center"
        self.clock_name.styles.text_style = "bold underline"
        self.btn_start = Button("Start", variant="success", id=f"start_{name}")

    def compose(self) -> ComposeResult:
        # Dynamically create and yield widgets
        yield self.clock_name
        yield self.clock  # Make sure the Digits widget is part of the tree
        yield self.inc_dec_buttons
        yield self.btn_start

    async def on_mount(self) -> None:
        """Ensure the widget tree is fully initialized before interacting with it."""
        self.update_time()  # Safe to call here, as the widget tree is fully constructed

    def increase_time(self) -> None:
        """Add 30 seconds to the timer."""
        self.timer_length += 30
        print(self.timer_length)
        self.update_time()

    def decrease_time(self) -> None:
        """Remove 30 seconds from the timer."""
        if self.timer_length > 30:
            self.timer_length -= 30
        print(self.display_time)
        self.update_time()

    def update_time(self) -> None:
        """Update the reactive display_time variable."""
        self.display_time = str(timedelta(seconds=self.timer_length))  # Automatically triggers `watch_display_time`
        #self.query_one("#display_time", Digits).update(self.display_time)
        self.clock.update(self.display_time)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_inc":
            self.increase_time()
        elif event.button.id == "btn_dec":
            self.decrease_time()
