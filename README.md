Name and surname: Jacek Kozakowski
Album number: 337248

The purpose of this project is to be able to simulate and track the movement of objects orbiting around a central object, e.g. the Moon's orbit around the Earth,
and save the results to a file that can be loaded later and based on the data contained therein, continue to simulate the movement in orbit starting
from the last step of the previous simulation period. The loaded data can also be edited from the program level before the next simulation.

The program has an interface that allows for the quick creation of new spaces for simulation, simulating their course, saving and
reading data, and sample simulations that allow for practical familiarization with the program's operation.

The program is divided into several classes:
    * Object - an object in space containing mass and its location.
    * CentralObject - a central object inheriting from the Object class, additionally containing its diameter.
    This is an object around which orbiting objects move and has a direct impact on the course of their movement in space.
    * OrbitalObject - an object orbiting around the central object, inherits from the Object class.
It also contains its id, mass, position (x, y), velocity vector values, position on the generated photo,
the color representing it on the generated photo.
Space - an object representing the space in which the simulation takes place. It contains its name, the size of the space (photo),
the scale of the photo (how many meters is one pixel), data of the central object, data of orbiting objects, a generated photo of the simulation progress,
any collisions of orbiting objects during the simulation. The most important method for the entire program is the simulation of a given space.
Based on the data contained by the Space class object and the given time unit and number of steps, it generates a simulation of the movement of orbiting objects
around the central object. The method uses formulas and physical laws for this purpose, such as:
    * The law of universal gravitation (Newton) - According to this law, any two bodies attract each other with a force proportional to the product of their masses and inversely
    proportional to the square of the distance between them. Mathematically, this is written as: F = G * M * m / r^2, where F is the force of attraction between bodies, G is
    the gravitational constant, m is the mass of the orbiting object, M is the mass of the central object, r is the distance between objects
    * Kepler's Laws: Describes the motion of planets around the Sun in an ellipse, which translates to other objects orbiting around bodies. This helps in understanding the
    problem and coincides with the simulations carried out.
If we know that F = G * M * m / r^2 and F = m * a where a is the acceleration, we get the equation: a = G * M / r^2. Thanks to this equation, it is possible to calculate
the gravitational acceleration that affects the object in orbit. In turn, thanks to this, it is possible to calculate the velocity of the body because here v = a * t, where v
is the velocity, and t is the time, then it is possible to calculate the displacement because s = v * t, where s is the distance. Knowing this, the path traveled by the body
should be represented as x and y, which can be achieved by representing acceleration and velocity as vectors. Then a = -G * M / r^2, ax = a * (x / r), where ax is the
horizontal value of the acceleration vector, and x is the component of the current position of the object, ay = a * (y / r), where ay is the vertical value of the acceleration
vector, and y is the component of the current position Then vx = vx + ax * t, where vx is the horizontal value of the velocity vector, ax is the horizontal value of the
acceleration vector, vy = vy + ay * t, where vy is the vertical value of the velocity vector, and ay is the vertical value of the acceleration vector. Then x = x + vx * t,
where x is the component of the current position on the OX axis, y = y + vy * t, where y is the component of the current position on the OY axis. In addition, the occurrence of
a collision is defined as the appearance of more than one orbital object on one pixel.

Instructions for use:
    * To properly run the program, the following versions of libraries and programs must be installed:
        * Python 3.13.1
        * Pillow 11.0.0
        * Pytest 8.3.4
        * Colorama 0.4.6
        * Iniconfig 2.0.0
        * Packaging 24.2
        * Pip 24.3.1
        * Pluggy 1.5.0
    * The program should be run from the main.py file
    * After running the program, an interface should be displayed in the console, which allows you to select the following options:
    * New simulation - allows you to enter new data for the simulation created based on the data provided by the user;
    * Load simulation - allows you to load a previously saved simulation, see its results and image, and start a new simulation;
    based on the last position of the bodies saved in the file.
    * Sample simulations - allows you to select one of the ready simulations existing in the program, this allows you to understand in practice how
    the program works. After selecting one of the simulations, I recommend that you familiarize yourself with the results and the image generated on their basis.
    The results are saved in json files. The program itself detects existing files saved in this format in a folder named 'simulations', which
    if it does not exist, you should create it manually, or perform any simulation, e.g. one of the example ones, and save it to a file, the program
    will then create a folder 'simulations' and a subfolder containing the simulation results. The images are saved in png format. Each folder and all files
    are named the same as the space (Space class) in which the simulation is performed. When there is already a file with a saved simulation with the same
    name as we created the new space, then we have the option of overwriting the files, or changing the name of the space, which will allow for safe
    saving of the file without losing the results of the previous simulation.

Creating the project began with separating all problems and tasks into subproblems and subtasks. This allowed for organizing the work in a
very effective way. At the beginning, I dealt with the interface itself, it was to redirect the user to the next program actions and options.
Then I dealt with building classes and their methods and testing them, at this stage I have not yet started writing the simulation algorithm.
Next, I dealt with entering the necessary data and handling files. I wanted the program to continue to function correctly regardless of the data entered by the user, so as part
of error handling I wrote a function so that when the wrong data format was entered, the program would not shut down showing what error was made, but would ask the user to
re-enter the correct data this time. I divided the function into groups dealing with displaying the program and handling the data and placed them in separate files. Finally, I
dealt with the simulation algorithm described above. It took me the most time, because at first I wanted to use the recommended Numpy library, which was well-matched with the
Pillow library, but after many attempts I was unable to present the calculated results in this format. I tackled the problem from the beginning and decided that I didn't need a
library that supports vectors and matrices, because I could represent the vectors in regular variables or tuples, then all I had to do was scale the results responsible for the
position and shift them by the displacement vector of the central object from the point on the Cartesian plane x=0 y=0 to the point x=(half the image size)/2, y=(half the image
size)/2.
