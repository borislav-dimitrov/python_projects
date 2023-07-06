from views import MainView


class View:
    def __init__(self, name, view):
        self.name = name
        self._view = view

    def show(self):
        self._view.show()

    def hide(self):
        self._view.hide()

    @property
    def view(self):
        return self._view


class ViewsController:
    def __init__(self, main_controller):
        self.main_controller = main_controller

        # Hooks
        self._get_all_programs = None

        self.main_view = View(name='main', view=MainView())

        self._all_views = [self.main_view, ]
        self.current_view = None

    def initialize(self):
        self.change_view(self.main_view)

    def change_view(self, view: View):
        if view == self.current_view:
            raise Exception(f'View {view.name} is already shown!')

        if self.current_view:
            self.current_view.hide()

        self.current_view = view
        self.current_view.show()

    def refresh_main_tree_items(self, programs):
        for program in programs:
            self.main_view.view.main_tree.addItem(program.name)

    # region HOOK CALLS
    def on_get_all_programs(self):
        if self._get_all_programs:
            self.refresh_main_tree_items(self._get_all_programs())

    def set_get_all_programs(self, callback):
        if callable(callback):
            self._get_all_programs = callback
        else:
            raise Exception('Invalid callback function!')

    # endregion
