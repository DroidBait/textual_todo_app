from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Digits, Input, DirectoryTree
from textual.containers import HorizontalScroll, Horizontal
from fileviewer import FileBrowser
from mdviewer import MdViewer
from editscreen import EditMdFileScreen


class MarkDownEditor(App):

    BINDINGS = [
        ("q", "close_app", "Quit"),
        ("e", "edit_file", "Edit"),
    ]
    CSS_PATH = "mdview.css"

    def __init__(self) -> None:
        super().__init__()
        self.lhs_file_browser = FileBrowser()
        self.lhs_file_browser.id = "lhs_fb"
        self.view_file = MdViewer("")
        self.view_file.id = "rhs_vf"
        self.path_current_viewing_file = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Horizontal(
            self.lhs_file_browser,
            self.view_file
        )

    def on_mount(self) -> None:
        app.install_screen(EditMdFileScreen(self.path_current_viewing_file), name="edit_screen")

    def action_close_app(self) -> None:
        self.exit()

    async def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected):
        await self.view_file.change_to_new_file(event.path)
        self.path_current_viewing_file = event.path
        #self.notify(str(event.path))

    def action_edit_file(self) -> None:
        app.push_screen("edit_screen")

if __name__ == "__main__":
    app = MarkDownEditor()
    app.run()