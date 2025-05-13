import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        colori = self._model.getColori()
        self._listYear.extend([2015, 2016, 2017, 2018])
        self._listColor.extend(colori)
        for anno in self._listYear:
            self._view._ddyear.options.append(ft.dropdown.Option(anno))
        for colore in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(colore["Product_color"]))
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        anno = self._view._ddyear.value
        colore = self._view._ddcolor.value
        if anno is None or anno == "":
            self._view.create_alert(f"Devi inserire un anno!")
            return
        if colore is None or colore == "":
            self._view.create_alert(f"Devi inserire un colore!")
            return
        self._model.buildGraph(anno, colore)
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodi()} Numero di archi: {self._model.getNumArchi()}"))
        archi, duplicati = self._model.getArchiPesoMaggiore()
        for u, v, weight in archi:
            self._view.txtOut.controls.append(ft.Text(f"Arco da {u} a {v}, peso={weight}"))
        nodi = []
        for duplicato in duplicati:
            nodi.append(str(duplicato))
        self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono: {nodi}"))
        self._view.update_page()

    def fillDDProduct(self):
        pass

    def handle_search(self, e):
        pass
