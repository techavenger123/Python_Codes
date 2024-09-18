from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.text_input = TextInput(hint_text="Type something here", font_size=30)
        self.label = Label(text="Your text will appear here", font_size=30)
        submit_button = Button(text="Display Text", font_size=30)
        submit_button.bind(on_press=self.display_text)
        layout.add_widget(self.text_input)
        layout.add_widget(submit_button)
        layout.add_widget(self.label)
        return layout
    def display_text(self, instance):
        entered_text = self.text_input.text
        self.label.text = entered_text
if __name__ == '__main__':
    TextInputApp().run()
