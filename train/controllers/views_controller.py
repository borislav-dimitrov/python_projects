from views import MainView, CreateEditProgramView


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
        self.current_program = None

        self.main_view = View(name='main', view=MainView(self))
        self.create_edit_program_view = View(name='create_edit_program', view=CreateEditProgramView(self))

        self._all_views = [self.main_view, self.create_edit_program_view]
        self.current_view = None

    def initialize(self):
        self.show_main_view()

    def change_view(self, view: View):
        if view == self.current_view:
            raise Exception(f'View {view.name} is already shown!')

        if self.current_view:
            self.current_view.hide()

        self.current_view = view
        self.current_view.show()

    def refresh_main_tree_items(self):
        for program in self.main_controller.get_all_programs():
            self.main_view.view.main_tree.addItem(program.name)

    def show_main_view(self):
        self.change_view(self.main_view)
        self.main_view.view.refresh_main_tree_items()

    def create_program(self):
        self.create_edit_program_view.view.create = True
        self.change_view(self.create_edit_program_view)

    def delete_program(self):
        print('Delete')

    def edit_program(self):
        self.create_edit_program_view.view.create = False
        self.create_edit_program_view.view.program = self.current_program
        self.change_view(self.create_edit_program_view)

    def quit(self):
        print('Quit')
        exit()
