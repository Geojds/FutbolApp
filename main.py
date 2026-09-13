import requests
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard

class TabPartidos(MDBoxLayout, MDTabsBase):
    pass

class TabPredicciones(MDBoxLayout, MDTabsBase):
    pass

class TabAjustes(MDBoxLayout, MDTabsBase):
    pass

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout_principal = MDBoxLayout(orientation='vertical')
        
        self.lbl_top = MDLabel(
            text="⚽ AI Football Stats & Predictions",
            font_style="H6",
            halign="center",
            size_hint_y=None,
            height=50
        )
        layout_principal.add_widget(self.lbl_top)

        self.tabs = MDTabs()
        
        self.tab_partidos = TabPartidos(title="Partidos")
        self.setup_partidos_tab()
        self.tabs.add_widget(self.tab_partidos)

        self.tab_pred = TabPredicciones(title="Predicción IA")
        self.setup_predicciones_tab()
        self.tabs.add_widget(self.tab_pred)

        self.tab_ajustes = TabAjustes(title="Notificaciones")
        self.setup_ajustes_tab()
        self.tabs.add_widget(self.tab_ajustes)

        layout_principal.add_widget(self.tabs)
        self.add_widget(layout_principal)

    def setup_partidos_tab(self):
        scroll = MDScrollView()
        self.lista_partidos = MDList()
        scroll.add_widget(self.lista_partidos)
        
        item1 = OneLineIconListItem(text="Real Madrid vs Barcelona — 21:00")
        item1.add_widget(IconLeftWidget(icon="soccer"))
        item2 = OneLineIconListItem(text="Man City vs Arsenal — 18:30")
        item2.add_widget(IconLeftWidget(icon="soccer"))
        
        self.lista_partidos.add_widget(item1)
        self.lista_partidos.add_widget(item2)
        self.tab_partidos.add_widget(scroll)

    def setup_predicciones_tab(self):
        box = MDBoxLayout(orientation='vertical', padding=15, spacing=10)
        card = MDCard(orientation='vertical', padding=15, size_hint_y=None, height=180)
        card.add_widget(MDLabel(text="🔥 Análisis IA: Real Madrid vs Barcelona", font_style="Subtitle1"))
        card.add_widget(MDLabel(text="• Predicción: Ambos Marcan (SÍ)", theme_text_color="Secondary"))
        card.add_widget(MDLabel(text="• Línea de Goles: Más de 2.5 goles (78% prob.)", theme_text_color="Secondary"))
        card.add_widget(MDLabel(text="• Ganador probable: Real Madrid", theme_text_color="Secondary"))
        box.add_widget(card)
        self.tab_pred.add_widget(box)

    def setup_ajustes_tab(self):
        box = MDBoxLayout(orientation='vertical', padding=15, spacing=15)
        box.add_widget(MDLabel(text="Configurar Alertas Personalizadas", font_style="Subtitle1", size_hint_y=None, height=30))
        
        sw_goles = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        sw_goles.add_widget(MDLabel(text="Notificar Goles"))
        sw_goles.add_widget(MDSwitch(active=True))
        
        sw_tarjetas = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        sw_tarjetas.add_widget(MDLabel(text="Notificar Tarjetas Rojas/Amarillas"))
        sw_tarjetas.add_widget(MDSwitch(active=False))
        
        sw_inicio = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        sw_inicio.add_widget(MDLabel(text="Inicio / Fin del partido"))
        sw_inicio.add_widget(MDSwitch(active=True))

        box.add_widget(sw_goles)
        box.add_widget(sw_tarjetas)
        box.add_widget(sw_inicio)
        self.tab_ajustes.add_widget(box)

class FootballApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return MainScreen()

if __name__ == '__main__':
    FootballApp().run()