from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Digits, Input, DirectoryTree, TextArea, Label
from textual.containers import HorizontalScroll, Horizontal, Vertical
from textual.screen import Screen


class EditMdFileScreen(Screen):

    BINDINGS = [
        ("escape", "app.pop_screen", "Pop screen"),
        #("ctrl+e", "app.pop_screen", "Exit"),
        ("ctrl+s", "save_file", 'Save'),
    ]

    def __init__(self, path:str, text: str):
        super().__init__()
        self.file_path = path
        self.text = text
        self.md_text = "No file currently loaded"
        #try:
        #    with open(self.file_path) as f:
        #        self.md_text = f.read()
        #except Exception as e:
        #    print("something went wrong")
        #    print(e)
        self.text_edit_area = TextArea.code_editor(id="edit_text_area")
        self.btn_save = Button("Save", variant="primary", id="save_btn")
        #self.file_name = self.get_file_name_from_path(self.file_path) 
        #self.lbl_txt = f"Editing {self.file_name}"
        self.lbl_title = Label(str(self.file_path), id="title_lbl")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        #print(str(type(self.lbl_title)))
        yield self.lbl_title
        #print(str(type(self.text_edit_area)))
        #self.code_editor_view = self.text_edit_area.code_editor(self.text, language="markdown")
        #yield self.code_editor_view
        yield self.text_edit_area.code_editor(self.text, language="markdown", id="code_edit_view")
        #print(str(type(self.btn_save)))
        yield self.btn_save
        #self.notify(str(self.file_path), severity="error")

    #def on_mount(self) -> None:
    #    self.set_focus(self.lbl_title)
        #self.get_file_text(self.file_path)

    #def _on_unmount(self) -> None:
    #    App.pop_screen()
    
    def get_file_text(self, path:str) -> None:
        try:
            with open(self.file_path) as f:
                self.md_text = f.read()
        except Exception as e:
            print("something went wrong")
            print(e)
            self.md_text = "Something went wrong"

    def set_new_file_path(self, path:str) -> None:
        self.file_path = path
        self.md_text = self.get_file_text(self.file_path)
        #self.text_edit_area.value = self.md_text
        #self.text_edit_area.code_editor(self.md_text, language="markdown")

    def get_file_name_from_path(self, path: str) -> str:
        str_path = str(path)
        if "/" in str_path:
            return str_path.rsplit("/", 1)[1]
        else:
            return "not_found.md"

    def save_file(self) -> None:
        print("Text found")
        print(self.text_edit_area)
        print(self.text_edit_area.text)
        edited_code = self.query_one("#code_edit_view")
        #print(type(x))
        #print("Get from x ")
        #print(x.text)
        with open(self.file_path, "w") as f:
            #self.notify("Saving file?")
            #print(self.text)
            f.write(edited_code.text)
        self.notify("File saved", severity="information")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save_btn":
            try:
                self.save_file()
            except Exception as e:
                print("Error")
                print(e)
                self.notify(str(f"Error saving file {e}"), severity="error")
