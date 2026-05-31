class ModeManager:

    def __init__(self):
        self.mode = "developer"

    def set_mode(self, mode):

        if mode not in ["user","developer"]:
            raise Exception("Invalid mode")

        self.mode = mode

    def get_mode(self):
        return self.mode


mode_manager = ModeManager()