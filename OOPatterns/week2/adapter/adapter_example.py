from abc import ABC, abstractmethod


class AbstractMapper(ABC):
    @abstractmethod
    def lighten(self, grid):
        pass


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper: AbstractMapper):
        self.lightmap = light_mapper.lighten(self.map)
        return self.lightmap.copy()


class MappingAdapter(AbstractMapper):
    def __init__(self, adaptee: Light):
        self.adaptee = adaptee
        self.lights = []
        self.obstacles = []

    def lighten(self, grid): # FIXME
        self.adaptee.set_dim([len(grid), len(grid[0])])
        for x, l in enumerate(grid):
            for y, k in enumerate(l):
                if k == 1:
                    self.lights.append((x, y))
                elif k == -1:
                    self.obstacles.append((x, y))

        self.adaptee.set_lights(self.lights)
        self.adaptee.set_obstacles(self.obstacles)
        return self.adaptee.generate_lights()


if __name__ == '__main__':
    system = System()
    light = Light([10, 10])
    adapter = MappingAdapter(light)
    print(system.get_lightening(adapter))
