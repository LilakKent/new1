from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexer import HtmlLexer
class NewApp(App):
    def build(self):
        return CodeInput(lexer = HtmlLexer())

        # return Button(text = 'my button',
        #               font_size = 30,
        #               on_press = self.btn_press,
        #               background_color = [1, 1, 0, 1],
        #               background_normal = '')

    def btn_press(self, instance):
        print('Button is pressed')
        instance.text = 'I`m pressed'
        instance.font_size = 10

if __name__ == '__main__':
    NewApp().run()
