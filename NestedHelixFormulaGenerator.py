"""
This script generates parametric equations for a secondary tapered helix that wraps around the tangent of a primary tapered helix.
The output equations are formatted for direct input into SolidWorks' Equation Driven Curve feature.

Usage:
- Run the script.
- Input the desired parameters when prompted.
- Copy the generated equations into SolidWorks.

Author: FREQ-EE
"""

import math

def generate_helix_formulas():
    # Introduction
    print("This script produces parametric equations to define a nested helix that wraps around the tangent of a primary tapered helix.")
    print("\nParameters to be entered:")
    print("{:<25} {:<50}".format("Parameter", "Description"))
    print("-" * 75)
    # Primary Helix parameters
    print("{:<25} {:<50}".format("Primary Helix Parameters", ""))
    print("{:<25} {:<50}".format("Initial Radius (r0)", "The starting radius of the primary helix."))
    print("{:<25} {:<50}".format("Final Radius (r1)", "The ending radius of the primary helix."))
    print("{:<25} {:<50}".format("Height (h)", "The vertical height of the primary helix."))
    print("{:<25} {:<50}".format("Number of Turns (N)", "The number of full rotations of the primary helix."))
    # Secondary Helix parameters
    print("\n{:<25} {:<50}".format("Secondary Helix Parameters", ""))
    print("{:<25} {:<50}".format("Initial Radius (rs0)", "The starting radius of the secondary helix."))
    print("{:<25} {:<50}".format("Final Radius (rs1)", "The ending radius of the secondary helix."))
    print("{:<25} {:<50}".format("Number of Turns (M)", "The number of full rotations of the secondary helix."))
    # Parameter Range
    print("\n{:<25} {:<50}".format("Parameter Range", ""))
    print("{:<25} {:<50}".format("Start of t (t1)", "The starting value of parameter t."))
    print("{:<25} {:<50}".format("End of t (t2)", "The ending value of parameter t."))

    # Prompt user for Primary Helix parameters
    print("\nEnter parameters for the Primary Helix:")
    r0 = float(input("Initial Radius (r0): "))
    r1 = float(input("Final Radius (r1): "))
    h = float(input("Height (h): "))
    N = float(input("Number of Turns (N): "))

    # Prompt user for Secondary Helix parameters
    print("\nEnter parameters for the Secondary Helix:")
    rs0 = float(input("Initial Radius (rs0): "))
    rs1 = float(input("Final Radius (rs1): "))
    M = float(input("Number of Turns (M): "))

    # Prompt user for parameter range
    print("\nEnter parameter range for t:")
    t1 = float(input("Start of t (t1): "))
    t2 = float(input("End of t (t2): "))

    # Compute constants for the equations
    # Primary Helix angular coefficient (theta(t) = theta_coeff * t)
    theta_coeff = (2 * N) / (t2 - t1)
    # Primary Helix radius increment per unit t (r(t) = r0 + r_slope * t)
    r_slope = (r1 - r0) / (t2 - t1)
    # Primary Helix height increment per unit t (Z_p(t) = h_slope * t)
    h_slope = h / (t2 - t1)
    # Secondary Helix radius increment per unit t (rs(t) = rs0 + rs_slope * t)
    rs_slope = (rs1 - rs0) / (t2 - t1)
    # Secondary Helix angular coefficient (phi(t) = phi_coeff * t)
    phi_coeff = (2 * M) / (t2 - t1)

    # Round constants to 3 decimal places
    theta_coeff = round(theta_coeff, 3)
    r_slope = round(r_slope, 3)
    h_slope = round(h_slope, 3)
    rs_slope = round(rs_slope, 3)
    phi_coeff = round(phi_coeff, 3)
        
    # Prepare equations in string format for SolidWorks
    # Note: 'pi' is used as a symbol for compatibility with SolidWorks

    # X(t) equation
    X_t = (
        f"(( {r0} + ({r_slope})*t + ( {rs0} + ({rs_slope})*t )*cos( ({phi_coeff}*pi*t) ))"
        f"*cos( ({theta_coeff}*pi*t) ))"
    )

    # Y(t) equation
    Y_t = (
        f"(( {r0} + ({r_slope})*t + ( {rs0} + ({rs_slope})*t )*cos( ({phi_coeff}*pi*t) ))"
        f"*sin( ({theta_coeff}*pi*t) ))"
    )

    # Z(t) equation
    Z_t = (
        f"( ({h_slope})*t + ( {rs0} + ({rs_slope})*t )*sin( ({phi_coeff}*pi*t) ) )"
    )

    # Output the equations
    print("\nSolidWorks Equations:")
    print(f"X(t) = {X_t}")
    print(f"Y(t) = {Y_t}")
    print(f"Z(t) = {Z_t}")

    # Instructions for SolidWorks
    print("\nInstructions:")
    print("1. Open a new 3D sketch in SolidWorks and select the 'Equation Driven Curve' feature.")
    print(f"2. Set the parameter 't' to vary from {t1} to {t2}.")
    print("3. Input the provided equations for X(t), Y(t), and Z(t).")
    print("4. Confirm and generate the curve.")

if __name__ == "__main__":
    while True:
        generate_helix_formulas()
        # Ask user whether to do another or exit
        choice = input("\nDo you want to generate another set of equations? (Y/N): ").strip().lower()
        if choice != 'y':
            print("Exiting the program.")
            break