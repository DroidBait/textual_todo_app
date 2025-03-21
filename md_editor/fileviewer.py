from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree
from textual.containers import HorizontalScroll

class FileBrowser(HorizontalScroll):

    def __init__(self, directory: str = "") -> None:
        super().__init__()
        self.file_viewer = DirectoryTree(directory if directory else "./notes", id="dt_file_viewer", classes="class_file_browser")
        #self.file_viewer.styles.width = "25%"
    
    def compose(self) -> ComposeResult:
        yield self.file_viewer
