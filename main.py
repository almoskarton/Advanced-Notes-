import webview
import json
import os
import sys


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# HTML
HTML_PATH = resource_path("html/index.html")

# ICON
ICON_PATH = resource_path("icon.ico")

# JSON AZ EXE MELLETT
EXE_DIR = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(EXE_DIR, "notes.json")


class Api:

    def load_notes(self):

        if not os.path.exists(DATA_PATH):

            with open(DATA_PATH, "w", encoding="utf-8") as f:
                json.dump([], f)

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_notes(self, notes):

        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(notes, f, indent=4, ensure_ascii=False)

        return True

    def close_app(self):

        webview.windows[0].destroy()

    def minimize_app(self):

        webview.windows[0].minimize()

    def toggle_maximize(self):

        window = webview.windows[0]

        if window.width >= 1400:
            window.restore()
        else:
            window.maximize()


api = Api()

window = webview.create_window(
    "Advanced Notes",
    HTML_PATH,
    js_api=api,
    frameless=True,
    easy_drag=True,
    width=1400,
    height=900,
    min_size=(900, 600),
    background_color="#050505"
)

webview.start(
    debug=False,
    icon=ICON_PATH
)