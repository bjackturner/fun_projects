import numpy as np

#
class PlanetManager:
    def __init__(self) -> None:
        self.planets = []
        self.dt

    # Performs Runge Kutta 4 time integration for each planet simultaneously
    def runge_kutta_4(self):

        # Vector containing weights for first three time steps of RK4
        weights = [1, 2, 2]

        # Loop through each each planet for each partial step of RK4 applying correct weights
        for i, weight in enumerate(weights):
            for planet in self.planets:
                planet.compute_gravitational_partial_step(self.planets, self.dt/weights[2-i] , weight)

        # Loop through each planet for the final step of RK4
        for planet in self.planets:
            planet.compute_full_step(self.planets, self.dt)

    def simulate(self, dt):

    def random_init_states(num_planets):

        pass
