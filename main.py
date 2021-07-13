class System():

    def Build(self):
        import interface
        interfaceObj = interface.InterfaceApp()
        interfaceObj.run()


if __name__ == "__main__":

    main = System()
    main.Build()