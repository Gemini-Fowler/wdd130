import math

def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    density_of_water = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density_of_water * gravity * height) / 1000  # in kPa

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_of_water = 998.2  # kg/m^3
    return (-friction_factor * pipe_length * density_of_water * fluid_velocity**2) / (2000 * pipe_diameter)  # in kPa

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_of_water = 998.2  # kg/m^3
    return (-0.04 * density_of_water * fluid_velocity**2 * quantity_fittings) / 2000  # in kPa

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_of_water = 998.2  # kg/m^3
    dynamic_viscosity_of_water = 0.0010016  # Pa.s
    return (density_of_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_of_water

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density_of_water = 998.2  # kg/m^3
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    return -k * density_of_water * fluid_velocity**2 / 2000  # in kPa

def generate_report(tower_height, tank_height, total_pressure, filename="water_flow_report.txt"):
    with open(filename, 'w') as report:
        report.write("Water Flow Pressure Report\n")
        report.write("============================\n")
        report.write(f"Water Tower Height: {tower_height} meters\n")
        report.write(f"Water Tank Height: {tank_height} meters\n")
        report.write(f"Final Pressure at House: {total_pressure:.2f} kPa\n")
    print(f"Report saved as {filename}")

# Constants for pipe properties
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters per second
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters per second

def main():
    # Input from the user
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    # Water column height and initial pressure
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    # Pressure loss from supply pipe
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    # Pressure loss from fittings (90° angles)
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    # Pressure loss from pipe reduction
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    # Pressure loss from household pipe
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Final pressure output
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    
    # Generate a report
    generate_report(tower_height, tank_height, pressure)

if __name__ == "__main__":
    main()
