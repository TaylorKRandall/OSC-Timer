import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import threading
import random

# Check Kivy required version
kivy.require("1.9.1")


class MainApp(App):
    use_kivy_settings = False

    def build(self,):
        self.root.start()
        # MainWidget is created automatically

    def on_stop(self):
        if self.root is not None:
            self.root.stop()

class MainWidget(BoxLayout):
    screen_manager = ObjectProperty(None)
    numeric_value = NumericProperty(0)

    def __init__(self,):
        super(MainWidget, self).__init__()
        self._thread = None
        self.stop_request = False

    def run(self,):
        while not self.stop_request:
            self.numeric_value = random.randrange(0, 1500)
            time.sleep(0.2)

    def start(self,):
        self._thread = threading.Thread(target=self.run)
        self._thread.start()

    def stop(self,):
        self.stop_request = True

        if self._thread is not None and self._thread.is_alive():
            if threading.current_thread() != self._thread:
                self._thread.join()

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class SliderScreen(BoxLayout):
    pass

if __name__ == "__main__":
    MainApp().run()