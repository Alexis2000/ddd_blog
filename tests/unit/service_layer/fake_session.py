class FakeSession:
    committed = False

    def commit(self):
        self.committed = True
