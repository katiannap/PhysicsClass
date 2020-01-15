train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c-temp

def f100_in_celsius(f_to_c):
 f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f-temp

c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)

def get_force(mass, acceleration):
 force = mass * acceleration
 return force

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

c = 3*10**8
bomb_mass = 1
def get_energy():
  energy = bomb_mass * (c**2)
  return energy

bomb_energy = get_energy()
print("A 1kg bomb supplies " + str(bomb_energy) + "Joules")

## CONSOLE

37.77777777777778
32.0
The GE train supplies 226800 Newtons of force.
A 1kg bomb supplies 90000000000000000Joules