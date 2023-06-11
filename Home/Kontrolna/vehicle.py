class Vehicle:
    def __init__(self,type_engine, type_transportation):
        self.type_engine = type_engine 
        self.type_transportation = type_transportation

    def show_info(self):
        print('Тип двигуна:')
        return self.type_engine
    