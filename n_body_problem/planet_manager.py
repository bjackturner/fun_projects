import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time as tm

from orbital_physics import Planet

#
class PlanetManager:
    def __init__(self) -> None:
        self.planets = []

    # Performs Runge Kutta 4 time integration for each planet simultaneously
    def _runge_kutta_4(self, dt):

        # Vector containing weights for first three time steps of RK4
        weights = [1, 2, 2]

        # Loop through each each planet for each partial step of RK4 applying correct weights
        for i, weight in enumerate(weights):
            for planet in self.planets:
                planet.compute_partial_step(self.planets, dt/weights[2-i] , weight)

        # Loop through each planet for the final step of RK4
        for planet in self.planets:
            planet.compute_full_step(self.planets, dt)

            

    def _plot_2d(self):
        plt.clf()  # Clear the previous plot to refresh the display

        weight = 0
        center = np.zeros(2)

        for planet in self.planets:
            theta = np.linspace(0, 2 * np.pi, 40)
            x = planet.radius * np.cos(theta) + planet.position[0]
            y = planet.radius * np.sin(theta) + planet.position[1]
            plt.plot(x, y, color=planet.color)

            center += planet.position * planet.mass
            weight += planet.mass

        center = center/weight

        plt.xlim(center[0] - 10, center[0] + 10)  # Set x-axis limits
        plt.ylim(center[1] - 10, center[1] + 10)  # Set y-axis limits
        plt.gca().set_aspect('equal', adjustable='box')  # Keep aspect ratio
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.title('2D Planet Animation')
        plt.grid()
        plt.pause(0.01)  # Pause to create animation effect

    # Simulate three body problem using the following
    def simulate(self, dt, stop_time):

        # Setup animation window
        time = 0
        time_start = tm.time()

        while time <= stop_time:

            time += dt

            # Runge Kutta time integration for each planet in the system
            self._runge_kutta_4(dt)

            self._plot_2d()
            
        plt.show()

    def random_init_states(self, num_planets, two_d=None):

        # Build n number of planets and place them in the planet manger
        for i in range(num_planets):
            planet = Planet()

            planet.planet_ID = i

            ## Create physics variables
            planet.radius = np.random.uniform(0.05, 0.5)
            planet.density = np.random.uniform(0.5e11, 5e11)

            ## Create true state variables (value at time steps)
            planet.position = np.random.uniform(-5, 5, size=(2 if two_d is True else 3,))
            planet.velocity = np.random.uniform(-1, 1, size=(2 if two_d is True else 3,))

            # Create display variables 
            planet.color = np.random.uniform(0, 1, size=(3,))

            # Finish configuring planet 
            planet.config()
            
            # Save to the planet manager
            self.planets.append(planet)

manger = PlanetManager()
manger.random_init_states(2, two_d=True)
manger.simulate(0.05, 160)