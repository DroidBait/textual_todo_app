from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Checkbox, Header, Footer, Label, Button, Digits
from textual.events import Key
import logging
from textual.logging import TextualHandler
from textual.containers import HorizontalGroup, VerticalScroll, Container, Vertical, Horizontal, HorizontalScroll
from timer_option import TimerOption

class PomodoroTimerApp(App):

    CSS_PATH="pomo.css"

    def __init__(self) -> None:
        super().__init__()
        self.short_break = TimerOption(default_length=300, name="Short_Break")
        self.work_time = TimerOption(default_length=25*60, name="Work_Time")
        self.long_break = TimerOption(default_length=600, name="Long_Break")
        self.countdown_clock = Digits("00:00:00", id="countdown_clock")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield HorizontalScroll(
            
            self.short_break,
            self.work_time,
            self.long_break,
            id="option_set"
        )
        #yield self.timer_break

    def on_button_pressed(self, event: Button.Pressed) -> None:
        print(event.button.id)
        if event.button.id == "start_Short_Break":
            print("Short break start clicked")
        elif event.button.id == "start_long_break":
            print("Long break clicked")
        

if __name__ == "__main__":
    app = PomodoroTimerApp()
    app.run()