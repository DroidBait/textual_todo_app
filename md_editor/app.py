from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Digits, Input, DirectoryTree
from textual.containers import HorizontalScroll, Horizontal, Vertical
from fileviewer import FileBrowser
from mdviewer import MdViewer
from editscreen import EditMdFileScreen

class AddNewFile(Vertical):
    def __init__(self):
        super().__init__()
        self.input_file_name = Input(placeholder="Enter new file name", id="inp_file_name")
        self.btn_create_file = Button("Create", variant="primary", id="btn_add_file")

    def compose(self) -> ComposeResult:
        yield self.input_file_name
        yield self.btn_create_file


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
        self.view_file = MdViewer("Empty File")
        self.view_file.id = "rhs_vf"
        self.path_current_viewing_file = ""
        self.edit_screen_view = EditMdFileScreen(self.path_current_viewing_file, "")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Horizontal(
            self.lhs_file_browser,
            self.view_file
        )

    #def on_mount(self) -> None:
        #app.install_screen(EditMdFileScreen(self.path_current_viewing_file), name="edit_screen")
        #app.install_screen(self.edit_screen_view, name="edit_screen")

    def action_close_app(self) -> None:
        self.exit()

    async def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected):
        await self.view_file.change_to_new_file(event.path)
        self.path_current_viewing_file = event.path
        #self.notify(str(event.path))

    async def action_edit_file(self) -> None:
        file_text = ""
        with open(self.path_current_viewing_file) as f:
            file_text = f.read()
        try:
            screen_found = app.get_screen("edit_screen")
            print(type(screen_found))
            if screen_found:
                app.uninstall_screen("edit_screen")
                app.install_screen(EditMdFileScreen(self.path_current_viewing_file, file_text), name="edit_screen")
        except KeyError as e:
            app.install_screen(EditMdFileScreen(self.path_current_viewing_file, file_text), name="edit_screen")
        self.edit_screen_view.set_new_file_path(self.path_current_viewing_file)
        app.push_screen("edit_screen")
        #self.notify("Testing when this appears")

if __name__ == "__main__":
    app = MarkDownEditor()
    app.run()