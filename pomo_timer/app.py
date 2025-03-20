
import asyncio

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Digits
from textual.containers import HorizontalScroll
from timer_option import TimerOption
from datetime import timedelta

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
        yield self.countdown_clock
        yield HorizontalScroll(
            
            self.short_break,
            self.work_time,
            self.long_break,
            id="option_set"
        )
        #yield self.timer_break

    async def run_countdown(self, time_to_run: int = 0) -> None:
        """
        Async function to countdown from time passed to function
        """
        for x in range(time_to_run):
            elapsed_time = time_to_run - x
            human_format_remaining = str(timedelta(seconds=elapsed_time))
            self.countdown_clock.update(human_format_remaining)
            #time.sleep(1)
            await asyncio.sleep(1)
        self.countdown_clock.update("0:00:00")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        print(event.button.id)
        if event.button.id == "start_Short_Break":
            print(str(self.short_break.timer_length))
            asyncio.create_task(self.run_countdown(self.short_break.timer_length))
        elif event.button.id == "start_Long_Break":
            print("Long break clicked")
            asyncio.create_task(self.run_countdown(self.long_break.timer_length))
        elif event.button.id == "start_Work_Time":
            print("Work time clicked")
            asyncio.create_task(self.run_countdown(self.work_time.timer_length))
        

if __name__ == "__main__":
    app = PomodoroTimerApp()
    app.run()