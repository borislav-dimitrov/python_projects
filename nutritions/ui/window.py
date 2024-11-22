from PyQt6 import QtCore, QtGui, QtWidgets
from food import FoodManager
from food import Nutrition
from .auto_complete_input import AutoCompleteInput


class Window(QtWidgets.QWidget):
    def __init__(self, application: QtWidgets.QApplication) -> None:
        super().__init__()

        self._app = application
        self._food_mgr = FoodManager()
        self._added_products = []
        self._total_nutrition = Nutrition('Total')

        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle('Nutrition tracker')
        w = 1366
        h = 768
        x = self._app.primaryScreen().geometry().width()
        y = self._app.primaryScreen().geometry().height()

        self.resize(w, h)
        self.move((x // 2) - (w // 2), (y // 2) - (h // 2))

        self._create_widgets()

    def _create_widgets(self) -> None:
        self._products_input = AutoCompleteInput([p.name for p in self._food_mgr.get_all_products()])
        self._products_input.setPlaceholderText('Input product name...')
        self._amt_input = QtWidgets.QLineEdit()
        self._amt_input.setPlaceholderText('Amount [gr]')
        self._products_list = QtWidgets.QListWidget()
        self._add_product_btn = QtWidgets.QPushButton('+')
        self._add_product_btn.clicked.connect(self._on_add_press)
        self._clear_products_btn = QtWidgets.QPushButton('Clear')
        self._clear_products_btn.clicked.connect(self._on_clear_press)
        self._rem_product_btn = QtWidgets.QPushButton('-')
        self._rem_product_btn.clicked.connect(self._on_rem_press)
        self._products_list_lbl = QtWidgets.QLabel('Products')
        self._products_list_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._calories_lbl = QtWidgets.QLabel('Calories')
        self._calories_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._protein_lbl = QtWidgets.QLabel('Protein')
        self._protein_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._fat_lbl = QtWidgets.QLabel('Fat')
        self._fat_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._carbs_lbl = QtWidgets.QLabel('Carbs')
        self._carbs_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._calories_amt_lbl = QtWidgets.QLabel('0')
        self._calories_amt_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._protein_amt_lbl = QtWidgets.QLabel('0')
        self._protein_amt_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._fat_amt_lbl = QtWidgets.QLabel('0')
        self._fat_amt_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._carbs_amt_lbl = QtWidgets.QLabel('0')
        self._carbs_amt_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self._products_input, 0, 0)
        layout.addWidget(self._amt_input, 0, 2)
        layout.addWidget(self._add_product_btn, 0, 3)
        layout.addWidget(self._clear_products_btn, 0, 4)
        layout.addWidget(self._products_list_lbl, 1, 0)
        layout.addWidget(self._calories_lbl, 1, 1)
        layout.addWidget(self._protein_lbl, 1, 2)
        layout.addWidget(self._fat_lbl, 1, 3)
        layout.addWidget(self._carbs_lbl, 1, 4)
        layout.addWidget(self._rem_product_btn, 4, 0)
        layout.addWidget(self._calories_amt_lbl, 2, 1)
        layout.addWidget(self._protein_amt_lbl, 2, 2)
        layout.addWidget(self._fat_amt_lbl, 2, 3)
        layout.addWidget(self._carbs_amt_lbl, 2, 4)
        layout.addWidget(self._products_list, 2, 0, 2, 1)

        layout.setColumnStretch(0, 3)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 1)
        layout.setColumnStretch(5, 10)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 7)
        layout.setRowStretch(3, 7)
        layout.setRowStretch(4, 10)

    def _on_add_press(self):
        product_name = self._products_input.text()
        product_amt = self._amt_input.text()
        if not product_name or not product_amt:
            return

        new_product = self._food_mgr.get_product(product_name)
        amount = int(product_amt)
        self._add_total_nutrition(new_product.calc_nutrition(amount))

        self._added_products.append([new_product, amount])
        self._products_list.addItem(f'{self._products_input.text()} | {self._amt_input.text()}gr')
        self._products_input.setText('')
        self._amt_input.setText('')

    def _on_rem_press(self) -> None:
        selected_items = self._products_list.selectedItems()
        item = selected_items[0]
        self._products_list.takeItem(self._products_list.row(item))

        product_name, product_amt = item.text().split(' | ')
        nutrition = self._food_mgr.get_product(product_name).calc_nutrition(int(product_amt[:-2]))
        self._subtract_total_nutrition(nutrition)

    def _on_clear_press(self) -> None:
        self._products_list.clear()
        self._total_nutrition.calories = 0
        self._total_nutrition.protein = 0
        self._total_nutrition.fat = 0
        self._total_nutrition.carbs = 0

        self._refresh_total_nutrition_labels()

    def _add_total_nutrition(self, nutrition: Nutrition) -> None:
        self._total_nutrition.calories += nutrition.calories
        self._total_nutrition.protein += nutrition.protein
        self._total_nutrition.fat += nutrition.fat
        self._total_nutrition.carbs += nutrition.carbs

        self._refresh_total_nutrition_labels()

    def _subtract_total_nutrition(self, nutrition: Nutrition) -> None:
        self._total_nutrition.calories -= nutrition.calories
        self._total_nutrition.protein -= nutrition.protein
        self._total_nutrition.fat -= nutrition.fat
        self._total_nutrition.carbs -= nutrition.carbs

        if self._total_nutrition.calories < 0:
            self._total_nutrition.calories = 0
        if self._total_nutrition.protein < 0:
            self._total_nutrition.protein = 0
        if self._total_nutrition.fat < 0:
            self._total_nutrition.fat = 0
        if self._total_nutrition.carbs < 0:
            self._total_nutrition.carbs = 0

        self._refresh_total_nutrition_labels()

    def _refresh_total_nutrition_labels(self) -> None:
        self._calories_amt_lbl.setText(f'{self._total_nutrition.calories:.03f}')
        self._protein_amt_lbl.setText(f'{self._total_nutrition.protein:.03f}')
        self._fat_amt_lbl.setText(f'{self._total_nutrition.fat:.03f}')
        self._carbs_amt_lbl.setText(f'{self._total_nutrition.carbs:.03f}')