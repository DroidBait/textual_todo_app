from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Digits, Input, DirectoryTree, TextArea, Label
from textual.containers import HorizontalScroll, Horizontal
from textual.screen import Screen


class EditMdFileScreen(Screen):

    BINDINGS = [
        ("escape", "app.pop_screen", "Pop screen"),
        #("ctrl+e", "app.pop_screen", "Exit"),
        ("ctrl+s", "save_file", 'Save'),
    ]

    def __init__(self, path:str):
        super().__init__()
        self.file_path = path
        self.md_text = ""
        try:
            with open(self.file_path) as f:
                self.md_text = f.read()
        except Exception as e:
            print("something went wrong")
            print(e)
        self.text_edit_area = TextArea(id="edit_text_area")
        self.btn_save = Button("Save", variant="primary", id="save_btn")
        self.file_name = self.get_file_name_from_path(self.file_path) 
        self.lbl_txt = f"Editing {self.file_name}"
        self.lbl_title = Label(self.lbl_txt, id="title_lbl")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield self.lbl_title
        yield self.text_edit_area.code_editor(self.md_text, language="markdown")
        yield self.btn_save

    def on_mount(self) -> None:
        self.set_focus(self.lbl_title)
        self.get_file_text(self.file_path)

    def _on_unmount(self) -> None:
        App.pop_screen()
    
    def get_file_text(self, path:str) -> None:
        try:
            with open(self.file_path) as f:
                self.md_text = f.read()
        except Exception as e:
            print("something went wrong")
            print(e)

    def set_new_file_path(self, path:str) -> None:
        self.file_path = path
        self.md_text = self.get_file_text(self.file_path)
        self.text_edit_area.value = self.md_text
        #self.text_edit_area.code_editor(self.md_text, language="markdown")

    def get_file_name_from_path(self, path: str) -> str:
        str_path = str(path)
        if "/" in str_path:
            return str_path.rsplit("/", 1)[1]
        else:
            return "not_found.md"

   # def action_exit_edit(self) -> None:
        
