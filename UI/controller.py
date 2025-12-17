import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.G.clear()
        self._view.lista_visualizzazione_1.controls.clear()
        num_nodes, num_edges, max_weight, min_weight = self._model.crea_grafo()
        riga_1 = f"Numero di vertici: {num_nodes} Numero di archi: {num_edges}"
        riga_2 = f"Informazioni sui pesi degli archi - valore minimo: {min_weight} e valore massimo: {max_weight}"
        self._view.lista_visualizzazione_1.controls.append(ft.Text(riga_1))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(riga_2))
        self._view.update()

        # TERMINATO FUNZIONA

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        soglia = self._view.txt_name.value
        self._view.lista_visualizzazione_2.controls.clear()
        if soglia is not None:
            if soglia.isdigit():
                if int(soglia) >= 3 and int(soglia) <= 7:
                    counter_minus, counter_plus = self._model.conta_edges(int(soglia))
                    riga_1 = f"Numero di archi con peso maggiore della soglia: {counter_plus}"
                    riga_2 = f"Numero di archi con peso minore della soglia: {counter_minus}"
                    self._view.lista_visualizzazione_2.controls.append(ft.Text(riga_1))
                    self._view.lista_visualizzazione_2.controls.append(ft.Text(riga_2))
                    self._view.update()
                else:
                    self._view.show_alert("Inserire un valore compreso tra 3 e 7!")
            else:
                self._view.show_alert("Inserire un valore numerico valido!")
        else:
            self._view.show_alert("Inserire un valore numerico ""soglia""!")


    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO