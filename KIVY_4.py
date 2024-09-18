from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.counter = 0
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text=str(self.counter), font_size=50)
        increment_button = Button(text="Increment", font_size=30)
        increment_button.bind(on_press=self.increment_counter)
        layout.add_widget(self.label)
        layout.add_widget(increment_button)
        return layout
    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = str(self.counter)
if __name__ == '__main__':
    CounterApp().run()
