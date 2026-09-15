from krita import *

class MultipleSelectionTools(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        # 1. Multiple Lasso Action
        lasso_action = window.createAction(
            "multiple_lasso",
            "Multiple Lasso",
            "tools"
        )
        lasso_action.triggered.connect(self.multiple_lasso)

        # 2. Multiple Magic Wand Action
        wand_action = window.createAction(
            "multiple_magic_wand",
            "Multiple Magic Wand",
            "tools"
        )
        wand_action.triggered.connect(self.multiple_magic_wand)

    def multiple_lasso(self):
        app = Krita.instance()
        
        # Switch to Lasso
        lasso_action = app.action("KisToolSelectOutline")
        if lasso_action:
            lasso_action.trigger()

        # Switch mode to 'Add'
        add_mode_action = app.action("selection_tool_mode_add")
        if add_mode_action:
            add_mode_action.trigger()

    def multiple_magic_wand(self):
        app = Krita.instance()
        
        # Switch to Magic Wand (Contiguous Area Selection)
        wand_action = app.action("KisToolSelectContiguous")
        if wand_action:
            wand_action.trigger()
        else:
            print("KisToolSelectContiguous NOT FOUND")

        # Switch mode to 'Add'
        add_mode_action = app.action("selection_tool_mode_add")
        if add_mode_action:
            add_mode_action.trigger()


Krita.instance().addExtension(MultipleSelectionTools(Krita.instance()))