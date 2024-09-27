# Nested Helix Formula Generator

This script generates parametric equations for a secondary tapered helix that wraps around the tangent of a primary tapered helix. The equations are formatted for direct input into SolidWorks' Equation Driven Curve feature.

## Overview

The **Nested Helix Formula Generator** produces equations to define a nested helix structure. By inputting specific parameters, you can model complex helical geometries where a secondary helix wraps around a primary tapered helix, both potentially varying in radius and number of turns.

## Parameters

| Parameter                 | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| **Primary Helix Parameters** |                                                               |
| Initial Radius (`r0`)     | The starting radius of the primary helix.                     |
| Final Radius (`r1`)       | The ending radius of the primary helix.                       |
| Height (`h`)              | The vertical height of the primary helix.                     |
| Number of Turns (`N`)     | The number of full rotations of the primary helix.            |
| **Secondary Helix Parameters** |                                                           |
| Initial Radius (`rs0`)    | The starting radius of the secondary helix.                   |
| Final Radius (`rs1`)      | The ending radius of the secondary helix.                     |
| Number of Turns (`M`)     | The number of full rotations of the secondary helix.          |
| **Parameter Range**       |                                                               |
| Start of `t` (`t1`)       | The starting value of the parameter `t`.                      |
| End of `t` (`t2`)         | The ending value of the parameter `t`.                        |

## Formulas

### Primary Helix


| **Primary Helix**                                      | **Secondary Helix**                                    |
|--------------------------------------------------------|--------------------------------------------------------|
| **Radius Function**:                                   | **Radius Function**:                                   |
| $r(t) = r_0 + \left( \dfrac{r_1 - r_0}{t_2 - t_1} \right) t$ | $r_s(t) = r_{s0} + \left( \dfrac{r_{s1} - r_{s0}}{t_2 - t_1} \right) t$ |
| **Angular Function**:                                  | **Angular Function**:                                  |
| $\theta(t) = \left( \dfrac{2N}{t_2 - t_1} \pi \right) t$ | $\phi(t) = \left( \dfrac{2M}{t_2 - t_1} \pi \right) t$ |
| **Height Function**:                                   | **(No height component)**                              |
| $Z_p(t) = \left( \dfrac{h}{t_2 - t_1} \right) t$       |                                                        |


### Combined Equations for SolidWorks

- **X(t)**:  
  $( X(t) = \left[ r(t) + r_s(t) \cos\left( \phi(t) \right) \right] \cos\left( \theta(t) \right) )$

- **Y(t)**:  
  $( Y(t) = \left[ r(t) + r_s(t) \cos\left( \phi(t) \right) \right] \sin\left( \theta(t) \right) )$

- **Z(t)**:  
  $( Z(t) = Z_p(t) + r_s(t) \sin\left( \phi(t) \right) )$

## Usage

1. **Run the Script**

   Execute the script in your Python environment:

   ```bash
   python NestedHelixFormulaGenerator.py
   ```

2. **Enter Parameters**

   When prompted, input the parameters as defined in the [Parameters](#parameters) section.

3. **Copy the Equations**

   After entering the parameters, the script will display the equations for `X(t)`, `Y(t)`, and `Z(t)`.

4. **Implement in SolidWorks**

   - Open a new **3D Sketch** in SolidWorks.
   - Select the **Equation Driven Curve** feature.
   - Set the parameter `t` to vary from your specified `t1` to `t2`.
   - Input the provided equations for `X(t)`, `Y(t)`, and `Z(t)`.
   - Confirm to generate the curve.

5. **Repeat or Exit**

   The script will ask if you want to generate another set of equations. Enter `Y` to continue or `N` to exit.

### Example

Here are example parameters and the resulting equations:

#### Parameters:

**Primary Helix:**
- Initial Radius (r0): 20  
- Final Radius (r1): 130  
- Height (h): 250  
- Number of Turns (N): 2.25  

**Secondary Helix:**
- Initial Radius (rs0): 15  
- Final Radius (rs1): 33  
- Number of Turns (M): 20  

**Parameter Range:**
- Start of t (t1): 0  
- End of t (t2): 15  

#### Resulting Equations:

- **X(t)**:  
  $X(t) = \left[ 20 + 7.33t + \left( 15 + 1.2t \right) \cos\left( 2.65 \pi t \right) \right] \cos\left( 0.3 \pi t \right)$

- **Y(t)**:  
  $Y(t) = \left[ 20 + 7.33t + \left( 15 + 1.2t \right) \cos\left( 2.65 \pi t \right) \right] \sin\left( 0.3 \pi t \right)$

- **Z(t)**:  
  $Z(t) = 16.68t + \left( 15 + 1.2t \right) \sin\left( 2.65 \pi t \right)$

#### Resulting Curve in SolidWorks

![Resulting Nested Helix Structure](./animation.gif)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
