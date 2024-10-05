import sqlite3

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

Window.image='ironman.jpeg'  # Dark blue background

# Database initialization
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Create the users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(username, email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, email, password) VALUES',
                       (username, email, password))
        conn.commit()
        return True  # User added successfully
    except sqlite3.IntegrityError:
        return False  # Username already exists
    finally:
        conn.close()

# Function to verify login credentials
def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user  # None if not found, user details if found


# Custom TextInput with Rounded Background
class RoundedTextInput(TextInput):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 0.2)  # Light transparent white color for input background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


# Login Screen
class LoginScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Vibrant Header
        header = Label(text='Login', color=(1, 1, 0, 1), font_size=36, bold=True)
        layout.add_widget(header)

        # Username and Password input fields
        layout.add_widget(Label(text='Username', color=(1, 1, 1, 1), font_size=24))
        self.username = RoundedTextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.username)

        layout.add_widget(Label(text='Password', color=(1, 1, 1, 1), font_size=24))
        self.password = RoundedTextInput(password=True, multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.password)

        # Login button
        login_button = Button(text='Login', size_hint=(1, 0.15), background_color=(0.2, 0.8, 0.2, 1), bold=True)
        login_button.bind(on_press=self.login_action)
        layout.add_widget(login_button)

        # Sign Up toggle button
        signup_button = Button(text='Go to Sign Up', size_hint=(1, 0.15), background_color=(0.1, 0.5, 0.8, 1), bold=True)
        signup_button.bind(on_press=self.go_to_signup)
        layout.add_widget(signup_button)

        # Label for showing error or success messages
        self.message_label = Label(text='', color=(1, 0, 0, 1), font_size=18)  # Red text for errors
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def login_action(self, instance):
        # Get the username and password
        username = self.username.text.strip()
        password = self.password.text.strip()

        # Check if fields are empty
        if not username or not password:
            self.message_label.text = "Please fill in both username and password."
            return

        # Verify the credentials
        user = verify_user(username, password)
        if user:
            self.message_label.color = (0, 1, 0, 1)  # Green color for success
            self.message_label.text = f"Welcome back, {username}!"
        else:
            self.message_label.color = (1, 0, 0, 1)  # Red color for errors
            self.message_label.text = "Incorrect username or password."

    def go_to_signup(self, instance):
        self.manager.current = 'signup'


# Sign-Up Screen
class SignUpScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Vibrant Header
        header = Label(text='Sign Up', color=(1, 1, 0, 1), font_size=36, bold=True)
        layout.add_widget(header)

        # Username, Email, and Password input fields
        layout.add_widget(Label(text='Username', color=(1, 1, 1, 1), font_size=24))
        self.username = RoundedTextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.username)

        layout.add_widget(Label(text='Email', color=(1, 1, 1, 1), font_size=24))
        self.email = RoundedTextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.email)

        layout.add_widget(Label(text='Password', color=(1, 1, 1, 1), font_size=24))
        self.password = RoundedTextInput(password=True, multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.password)

        # Sign Up button
        signup_button = Button(text='Sign Up', size_hint=(1, 0.15), background_color=(0.8, 0.2, 0.2, 1), bold=True)
        signup_button.bind(on_press=self.signup_action)
        layout.add_widget(signup_button)

        # Go to Login screen
        login_button = Button(text='Go to Login', size_hint=(1, 0.15), background_color=(0.1, 0.5, 0.8, 1), bold=True)
        login_button.bind(on_press=self.go_to_login)
        layout.add_widget(login_button)

        # Label for showing error or success messages
        self.message_label = Label(text='', color=(1, 0, 0, 1), font_size=18)  # Red text for errors
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def signup_action(self, instance):
        # Get the username, email, and password
        username = self.username.text.strip()
        email = self.email.text.strip()
        password = self.password.text.strip()

        # Check if fields are empty
        if not username or not email or not password:
            self.message_label.text = "All fields are required."
            return

        # Check if the username is taken
        if add_user(username, email, password):
            self.message_label.color = (0, 1, 0, 1)  # Green color for success
            self.message_label.text = f"Account created successfully! Welcome, {username}."
            # Clear fields for another sign-up
            self.username.text = ''
            self.email.text = ''
            self.password.text = ''
        else:
            self.message_label.color = (1, 0, 0, 1)  # Red color for errors
            self.message_label.text = "Username already exists. Please choose another."

    def go_to_login(self, instance):
        self.manager.current = 'login'


# Main App
class MyApp(App):
    def build(self):
        # Initialize the database
        init_db()

        # ScreenManager to handle switching between login and sign-up screens
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignUpScreen(name='signup'))

        return sm


# Run the app
if _name_ == '_main_':
    MyApp().run()