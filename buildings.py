from typing_extensions import override


class Building:
    def __init__(self, name: str, x: int, y: int, prefix=None) -> None:
        self.name = name
        self.x = x
        self.y = y
        if prefix:
            self.prefix = prefix

    def after_init(self, buildings) -> None:
        pass

    def update(self, tick: int) -> None:
        pass

    def get_prefix(self) -> str:
        return self.prefix
    
    def __str__(self):
        return f"{self.name} at ({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


class OreFactory(Building):
    
    def __init__(self, name: str, x, y, prefix=None):
        super().__init__(name, x, y, prefix=None)
        self.size = 3
        self.output = None
        self.prefix = "[x]"
    
    def after_init(self, buildings: list[Building]):
        super().after_init(buildings)
        neighbor = buildings[self.x + 1]
        if isinstance(neighbor, Conveyor):
            print(f"Connected {self} to {neighbor}")
            neighbor.input = self
            self.output = neighbor
            neighbor.after_init(buildings)

    @override
    def update(self, tick: int) -> None:
        if not self.output:
            return
        
        if tick % 3 == 0:
            self.output.item = "."


class Conveyor(Building):
    def __init__(self, name, x, y, prefix=None):
        super().__init__(name, x, y, prefix=None)
        if prefix:
            self.prefix = prefix
        self.size: int = 1
        self.input: Building | None = None
        self.output: Building | None = None
        self.item: str | None = None

    def after_init(self, buildings) -> None:

        if (self.x + 1) >= len(buildings):
            return
        
        neighbor = buildings[self.x + 1]
        if isinstance(neighbor, Conveyor):
            print(f"Connected {self} to {neighbor}")
            neighbor.input = self
            self.output = neighbor
            neighbor.after_init(buildings)

    @override
    def get_prefix(self) -> str:
        if self.item:
            return "."
        return self.prefix
    
    @override
    def update(self, tick):
        pass
