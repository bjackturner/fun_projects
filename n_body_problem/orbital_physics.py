import numpy as np

# Contains all values and function to compute orbital trajectories of bodies
class Planet:
    def __init__(self) -> None:
        
        ## Physics variables
        self.radius = None
        self.density = None
        self.mass = None

        ## True state variables (value at time steps)
        self.position = None
        self.velocity = None
        self.acceleration = None

        ## Partial state variables (value between time steps)
        self.par_position = None
        self.par_velocity = None
        
        ## Runge Kutta 4 full step weighted sum (k1 + 2k2 + 2k3 + k4)
        self.full_velocity = None
        self.full_acceleration = None
        
        # Display variables 
        self.color = None

    # Returns gravitational acceleration acting on planet for use in RK4 time integration 
    def compute_gravitational_acceleration(self, planets):

        # Define local acceleration vector for sum
        acceleration = np.zeros_like(self.acceleration)

        # Loop through each planet, but current planet, to compute acceleration
        for planet in planets:
            if planet != self:

                # Sum of gravitional forces on current planet by other planets (Newtons equation)
                acceleration -= (planet.mass / np.linalg.norm(self.par_position - planet.par_position)**3) * (self.par_position - planet.par_position)

        return 6.6743e-11 * acceleration
    
    # Computes the intermediate steps of Runge Kutta time integration 
    def compute_partial_step(self, planets, dt, weight):

        # Compute the gravitional force on the current planet which gives motion
        acceleration = self.compute_gravitational_acceleration(planets)

        # Add updated mid step partial values to weight vector for final partial step
        self.full_velocity += self.par_velocity * weight
        self.full_acceleration += acceleration * weight

        # Update the partial position (RK 4 partial step data) for both position and velocity
        self.par_position = self.position + self.par_velocity * dt
        self.par_velocity = self.velocity + acceleration * dt
        
    # Computes only the final full step of Runge Kutta time integration 
    def compute_full_step(self, planets, dt):

        # Compute the gravitional force on the current planet which gives motion
        acceleration = self.compute_gravitational_acceleration(planets)
        self.par_velocity = self.velocity + acceleration * dt

        # Update the true acceleration to object. velocity is depended on acceleration so it remains partial
        self.acceleration = (self.full_acceleration + acceleration)/6
        self.par_velocity = (self.full_velocity + self.par_velocity)/6

        # Update true position and velocity of next time step
        self.position += self.par_velocity * dt
        self.velocity += self.acceleration * dt

        # Set partial position and velocity equal to true values for next time step
        self.par_position = self.position
        self.par_velocity = self.velocity

        # Reset weight vectors to 0 for next time step
        self.full_velocity = np.zeros_like(self.full_acceleration)
        self.full_acceleration = np.zeros_like(self.full_acceleration)