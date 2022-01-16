from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

import random
from drawing import Biomorph

Config.set('graphics', 'width', 1500)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', 0)


class BiomorphsApp(App):

    # starting situation of images
    def build(self):
        self.gens = [1, 45, 1, 1, 1, 5, 1, 5, 1, 1, 2, 1]
        self.generate_biomorths()
        Biomorph(*self.gens).draw('_main')

        main_bl = BoxLayout(orientation='vertical', padding=[20])
        gl1 = GridLayout(cols=8, rows=1, spacing=15)

        self.img1 = Image(source='biomorth1.png')
        self.img2 = Image(source='biomorth2.png')
        self.img3 = Image(source='biomorth3.png')
        self.img4 = Image(source='biomorth4.png')
        self.img5 = Image(source='biomorth5.png')
        self.img6 = Image(source='biomorth6.png')
        self.img7 = Image(source='biomorth7.png')
        self.img8 = Image(source='biomorth8.png')

        self.img_main = Image(size_hint=(1, 0.8), source='biomorth_main.png')

        gl1.add_widget(self.img1)
        gl1.add_widget(self.img2)
        gl1.add_widget(self.img3)
        gl1.add_widget(self.img4)
        gl1.add_widget(self.img5)
        gl1.add_widget(self.img6)
        gl1.add_widget(self.img7)
        gl1.add_widget(self.img8)

        gl2 = GridLayout(cols=8, rows=1, size_hint=(1, 0.2), spacing=20, padding=[0, 10])
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_1, size_hint=(0.7, 0.25)))
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_2, size_hint=(0.7, 0.25)))
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_3, size_hint=(0.7, 0.25)))
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_4, size_hint=(0.7, 0.25)))
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_5, size_hint=(0.7, 0.25)))
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_6, size_hint=(0.7, 0.25)))
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_7, size_hint=(0.7, 0.25)))
        gl2.add_widget(Button(text='Choose it', on_press=self.choose_8, size_hint=(0.7, 0.25)))

        main_bl.add_widget(self.img_main)
        main_bl.add_widget(gl1)
        main_bl.add_widget(gl2)
        return main_bl

    # the processing of generating of new images and choosing from them
    def generate_biomorths(self):
        self.list_of_gens = []

        for i in range(1, 9):
            add_gens = self.gens.copy()
            x = random.randint(0, 11)

            if x in [0, 6, 7, 10, 11]:
                add_gens[x] = add_gens[x] + random.choice([-1, 1])
                if add_gens[x] == 0:
                    add_gens[x] = 1

            elif x in [1, 4, 5]:
                prev = add_gens[x]
                add_gens[x] = add_gens[x] + random.choice([-1, 1])
                if add_gens[x] == 0:
                    if prev == 1:
                        add_gens[x] = -1
                    elif prev == -1:
                        add_gens[x] = 1

            elif x in [2, 3, 8, 9]:
                add_gens[x] = random.choice(list(set([1, 2, 3, 4]) - set([add_gens[x]])))

            Biomorph(*add_gens).draw(i)
            self.list_of_gens.append(add_gens)

    def choose_1(self, instance):
        self.gens = self.list_of_gens[0]
        self.update()

    def choose_2(self, instance):
        self.gens = self.list_of_gens[1]
        self.update()

    def choose_3(self, instance):
        self.gens = self.list_of_gens[2]
        self.update()

    def choose_4(self, instance):
        self.gens = self.list_of_gens[3]
        self.update()

    def choose_5(self, instance):
        self.gens = self.list_of_gens[4]
        self.update()

    def choose_6(self, instance):
        self.gens = self.list_of_gens[5]
        self.update()

    def choose_7(self, instance):
        self.gens = self.list_of_gens[6]
        self.update()

    def choose_8(self, instance):
        self.gens = self.list_of_gens[7]
        self.update()
        print(1)

    def update(self):
        self.generate_biomorths()
        Biomorph(*self.gens).draw('_main')
        self.img1.reload()
        self.img2.reload()
        self.img3.reload()
        self.img4.reload()
        self.img5.reload()
        self.img6.reload()
        self.img7.reload()
        self.img8.reload()
        self.img_main.reload()

if __name__ == "__main__":
    BiomorphsApp().run()