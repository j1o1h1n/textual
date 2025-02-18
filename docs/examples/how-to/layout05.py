from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder


class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """


class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """


class Tweet(Placeholder):
    pass


class Column(VerticalScroll):
    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 20):
            yield Tweet(id=f"Tweet{tweet_no}")


class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")
        with HorizontalScroll():
            yield Column()
            yield Column()
            yield Column()
            yield Column()


class LayoutApp(App):
    CSS_PATH = "layout.css"

    def on_ready(self) -> None:
        self.push_screen(TweetScreen())


if __name__ == "__main__":
    app = LayoutApp()
    app.run()
