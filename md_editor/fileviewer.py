import os

from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Input, Button
from textual.containers import HorizontalScroll, Vertical, VerticalScroll


class AddNewFile(Vertical):
    def __init__(self):
        super().__init__()
        self.input_file_name = Input(placeholder="Enter new file name", id="inp_file_name")
        self.btn_create_file = Button("Create File", variant="primary", id="btn_add_file")
        self.btn_create_dir = Button("Create Directory", variant="primary", id="btn_create_dir")

    def compose(self) -> ComposeResult:
        yield self.input_file_name
        yield self.btn_create_file
        yield self.btn_create_dir


class FileBrowser(VerticalScroll):

    def __init__(self, directory: str = "") -> None:
        super().__init__()
        self.directory = directory if directory else "./notes"
        self.file_viewer = DirectoryTree(self.directory, id="dt_file_viewer", classes="class_file_browser")
        self.add_new_file_ui = AddNewFile()
        #self.file_viewer.styles.width = "25%"
    
    def compose(self) -> ComposeResult:
        yield self.file_viewer
        yield self.add_new_file_ui
        
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn_add_file":
            new_file_name = self.add_new_file_ui.input_file_name.value
            if new_file_name == None or new_file_name == "":
                self.notify("Add a file name before clicking new file", severity="error")
            else:
                #print("add file button clicked")
                new_file_name = self.directory + "/" + new_file_name
                if os.path.exists(new_file_name):
                    self.notify("This file already exists", severity="error")
                else:
                    #print(new_file_name)
                    with open(new_file_name, "w") as f:
                        f.write("")
                    self.notify(f"New file created at {new_file_name}", severity="information")
                    self.file_viewer.reload()
        elif event.button.id == "btn_create_dir":
            new_dir = self.directory + "/" + self.add_new_file_ui.input_file_name.value
            #if "." in new_dir:
            #    self.notify("Remove all . characters from folder name")
            #else:
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
                self.notify("New directory created", severity="information")
                self.file_viewer.reload()
            else:
                self.notify("Directory already exists", severity="error")
