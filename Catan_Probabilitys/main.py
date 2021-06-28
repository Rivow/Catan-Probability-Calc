from unittest import main
import Catan_Probabilitys


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.popup import Popup

from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.lang import Builder



Builder.load_string("""
#:import Factory kivy.factory.Factory
<MainPage>:
	orientation: 'vertical'


	BoxLayout:
		size_hint: 1, .15
		Button:
			size_hint: .20, 1
			text: 'N.G.'

		Label:
			text: 'yeet'

		Button:
			size_hint: .20, 1
			text: 'info'

	ScrollView:
		Label:
			font_size: 90

			size: self.texture_size
			text: app.list_str

    StackNumber:
            


<MainScreen>
    BoxLayout:
        orientation: 'vertical'
        MainPage:

        BottomLayout:
            size_hint: 1, .15
            Button:
                text: 'End Game?'
                on_press: Factory.EndPopup().open()

<EndScreen>:
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
		    Label:
			    size_hint: None, None
			    font_size: 60
			    size: self.texture_size
                text: app.end_statistics

			    
        Button:
            size_hint: 1, .15
            text: 'New Game'
            on_press: Factory.NewGamePopup().open()

<EndPopup>:
    size_hint: .75 , .75
    auto_dismiss: False
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint: 1, .8
            text: 'Are you sure you want to end the Game?'

        BoxLayout:
            size_hint: 1, .2
            Button:
                text: 'Yes'
                on_press:
                    root.end_game()
                    app.sm.transition.direction = 'left'
                    app.sm.transition.duration = 0.3
                    app.sm.current = 'end_screen'
                    root.dismiss()
            Button:
                text: 'No'
                on_press: root.dismiss()

<NewGamePopup>:
    size_hint: .75 , .75
    auto_dismiss: False
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint: 1, .8
            text: 'Are you sure you want to start a new Game?'

        BoxLayout:
            size_hint: 1, .2
            Button:
                text: 'Yes'
                on_press:
                    root.new_game()
                    app.sm.transition.direction = 'left'
                    app.sm.transition.duration = 0.3
                    app.sm.current = 'main_screen'
                    root.dismiss()
            Button:
                text: 'No'
                on_press: root.dismiss()



""")

class MainScreen(Screen):
    pass
            

class EndScreen(Screen):
    pass

class MainPage(BoxLayout):
    pass


class StackNumber(StackLayout):
    def __init__(self, **kwargs):
        super(StackNumber, self).__init__(**kwargs)
        self.size_hint = (1, .55)
        for number in range (2, 13):
            btn = Button(text = str(number), size_hint=(.25, .33))
            btn.bind(on_press = self.on_number_button_click)
            self.add_widget(btn)
        btn = Button(text = u"\u2190", size_hint = (.25, .33))
        btn.bind(on_press = self.on_delete_click)
        self.add_widget(btn)


    def on_number_button_click(self, instance):
        app = App.get_running_app()
        app.roll_list.append(int(instance.text))
        app.list_str = ''
        for n in range(-5, 0):
            try:
                app.list_str += str(app.roll_list[n]) + '\n'

            except:
                pass

    def on_delete_click(self, instance):
        try:
            app = App.get_running_app()
            app.list_str = app.list_str.removesuffix(str(app.roll_list[-1]) + '\n')
            app.roll_list.pop()
        except:
           pass


class BottomLayout(AnchorLayout):
    pass

    
class EndPopup(Popup):
    pass

    def end_game(self):
        app = App.get_running_app()
        probs = Catan_Probabilitys.create_average_probability_dic()
        rolled_list = Catan_Probabilitys.rolled_dic(app.roll_list)
        amount_rolls = Catan_Probabilitys.expected_amount_rolls(probs, len(app.roll_list))
        actual_game_prob = Catan_Probabilitys.calculate_game_prob(rolled_list, len(app.roll_list))
        app.end_statistics = ''
        for rolls in rolled_list:
            if int(rolls) < 10:
                    app.end_statistics += f'{rolls}  Expected: {amount_rolls[int(rolls)]}   Actual In Game: {rolled_list[int(rolls)]}\n{rolls}  Probability: {actual_game_prob[int(rolls)] * 100}%\n'
            else:
                    app.end_statistics += f'{rolls} Expected: {amount_rolls[int(rolls)]}  Actual In Game: {rolled_list[int(rolls)]}\n{rolls}  Probability: {actual_game_prob[int(rolls)] * 100}%\n'
        app.end_statistics += f'Total Rolls: {len(app.roll_list)}'


class NewGamePopup(Popup):
    pass

    def new_game(self):
        app = App.get_running_app()
        app.roll_list = []
        app.list_str = ''


class CatanApp(App):
    roll_list = ListProperty([])
    list_str = StringProperty('')
    end_statistics = StringProperty ('')

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name = 'main_screen'))
        self.sm.add_widget(EndScreen(name = 'end_screen'))
        return self.sm




if __name__ == '__main__':
    
    CatanApp().run()
    main(module='Test_Module', exit=False)
