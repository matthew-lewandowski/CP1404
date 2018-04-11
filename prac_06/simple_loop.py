from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class LoopWidgetApp(App):

    def __init__(self):
        super().__init__()
        self.names = ["matt", "kyle", "tom", "jake"]

    def build(self):
        self.title = "Simple Loop"
        self.root = Builder.load_file('simple_loop.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name)
            self.root.ids.entries_box.add_widget(temp_button)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


LoopWidgetApp().run()
