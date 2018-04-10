"""
Kivy GUI program to convert miles to kilometres
matthew lewandowski
Started 04/04/2018
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
MILES_TO_KM = 1.60934

__author__ = 'Lindsay Ward'


class ConvertMilesApp(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def convert_miles(self):
        result = self.check_miles()
        result = result * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        result = self.check_miles() + increment
        self.root.ids.input_number.text = str(result)
        self.convert_miles()

    def check_miles(self):
        try:
            number = float(self.root.ids.input_number.text)
            return number
        except ValueError:
            return 0


ConvertMilesApp().run()