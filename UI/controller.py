import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.soglia = None

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.crea_grafo()
        num_nodes, num_edges, minimo, massimo = self._model.crea_connessioni()
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di vertici: {num_nodes} Nnumero di archi: {num_edges}"))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Informazioni sui pesi degli archi - valore minimo: {minimo}, valore massimo: {massimo}"))
        self._view.btn_conta_edges.disabled = False
        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        self.soglia = self._view.txt_name.value

        try:
            if self.soglia.isdigit():
                if not (3 <= float(self.soglia) <= 7):
                    self._view.show_alert("Inserisci un valore compreso tra 3 e 7")
                    self.soglia = None

            if self.soglia:
                counter_min, counter_max = self._model.conta_archi_soglia(self.soglia)
                self._view.lista_visualizzazione_2.controls.clear()
                self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {counter_max}"))
                self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {counter_min}"))
                self._view.btn_ricerca.disabled = False
                self._view.update()

        except Exception:
            self._view.show_alert("Inserisci un valore compreso tra 3 e 7")

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        lista_archi_peso, peso_max = self._model.ricerca_percorso(self.soglia)
        self._view.lista_visualizzazione_3.controls.clear()
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Numero archi percorso più lungo: {len(lista_archi_peso)}"))
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Peso cammino massimo: {peso_max}"))
        for item in lista_archi_peso:
            self._view.lista_visualizzazione_3.controls.append(ft.Text(f"{item[0]} --> {item[1]}: {item[2]}"))
        self._view.update()