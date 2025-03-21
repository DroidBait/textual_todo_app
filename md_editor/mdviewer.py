from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Digits, Input, DirectoryTree, MarkdownViewer
from textual.containers import HorizontalScroll, VerticalScroll

class MdViewer(VerticalScroll):

    def __init__(self, path: str) -> None:
        super().__init__()
        self.view_markdown_file = MarkdownViewer("", show_table_of_contents=True, id="md_view_file")
        #self.view_markdown_file.update("Hello")
        self.path = path

    def compose(self) -> ComposeResult:
        yield self.view_markdown_file

    async def change_to_new_file(self, path: str) -> None:
        #self.view_markdown_file.go(path)
        print("Change file funcion is running")
        #self.notify(str(path), severity="error")
        print(path)
        #await self.view_markdown_file.load(path)
        await self.view_markdown_file.go(path)
        self.refresh()