#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import random

class WrappedLabel(Label):
    # https://stackoverflow.com/a/58227983
    def __init__(self, **kwargs):
        # the next line changes in python3
        super(WrappedLabel,self).__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class MainScreen(AnchorLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        b = Button(text="Take a cookie", size_hint=[0.5,0.2])
        b.bind(on_release = self.show_popup)
        self.add_widget(b)

    def show_popup(self, event):
        c = WrappedLabel(text=random.choice(cookies))
        p = Popup(title="Here is your fortune cookie...",
                content=c,
                size_hint=(0.6,0.6),
                auto_dismiss=True)
        c.bind(on_touch_down = p.dismiss)
        p.open()

class ButtonApp(App):

    def build(self):
        self.title = 'Fortune cookie'
        return MainScreen()

if __name__ == '__main__':
    cookies = [ "The fortune you seek is in another cookie.",
            "A closed mouth gathers no feet.",
            "Tomorrow is another day.",
            "We don't know the future, but here's a cookie.",
            "Help! I am being held prisoner in a fortune cookie factory.",
            "Don't eat the paper." ]
    ButtonApp().run()


