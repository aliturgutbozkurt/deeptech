#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deeptech Reference Implementation: 3-Link Planar Robotic Manipulator Kinematics
Solves Forward Kinematics (FK) and Numerical Inverse Kinematics (IK)
using the Jacobian Transpose / Pseudo-Inverse algorithm for end-effector trajectory tracking.
"""

import math
import numpy as np

def print_header(title: str):
    print("\n" + "=" * 70)
    print(f"🤖 ROBOTICS & AUTONOMOUS SYSTEMS: {title}")
    print("=" * 70)

class RoboticArm3DOF:
    def __init__(self, link_lengths: list = [1.0, 0.8, 0.5]):
        self.lengths = link_lengths
        # Initial joint angles [theta1, theta2, theta3] in radians
        self.thetas = np.array([0.2, 0.4, -0.3], dtype=np.float64)

    def forward_kinematics(self, thetas: np.ndarray) -> np.ndarray:
        """Computes Cartesian (x, y) coordinates of end-effector from joint angles."""
        t1, t2, t3 = thetas
        l1, l2, l3 = self.lengths

        x = l1 * np.cos(t1) + l2 * np.cos(t1 + t2) + l3 * np.cos(t1 + t2 + t3)
        y = l1 * np.sin(t1) + l2 * np.sin(t1 + t2) + l3 * np.sin(t1 + t2 + t3)
        return np.array([x, y])

    def compute_jacobian(self, thetas: np.ndarray) -> np.ndarray:
        """Calculates 2x3 Geometric Jacobian matrix: J = d(x, y) / d(theta)."""
        t1, t2, t3 = thetas
        l1, l2, l3 = self.lengths

        dx_dt1 = -l1*np.sin(t1) - l2*np.sin(t1+t2) - l3*np.sin(t1+t2+t3)
        dx_dt2 = -l2*np.sin(t1+t2) - l3*np.sin(t1+t2+t3)
        dx_dt3 = -l3*np.sin(t1+t2+t3)

        dy_dt1 = l1*np.cos(t1) + l2*np.cos(t1+t2) + l3*np.cos(t1+t2+t3)
        dy_dt2 = l2*np.cos(t1+t2) + l3*np.cos(t1+t2+t3)
        dy_dt3 = l3*np.cos(t1+t2+t3)

        return np.array([
            [dx_dt1, dx_dt2, dx_dt3],
            [dy_dt1, dy_dt2, dy_dt3]
        ])

    def solve_inverse_kinematics(self, target_pos: np.ndarray, max_iterations: int = 100, tolerance: float = 1e-4):
        """
        Damped Least Squares / Pseudo-Inverse iterative solver:
        Δθ = J^† * e = J^T (J J^T + λ² I)^(-1) * e
        """
        current_thetas = self.thetas.copy()
        damping = 0.01

        for i in range(max_iterations):
            current_pos = self.forward_kinematics(current_thetas)
            error = target_pos - current_pos
            err_norm = np.linalg.norm(error)

            if err_norm < tolerance:
                return current_thetas, i, True

            J = self.compute_jacobian(current_thetas)
            # Damped pseudo-inverse
            JJt = np.dot(J, J.T) + (damping ** 2) * np.eye(2)
            J_pinv = np.dot(J.T, np.linalg.inv(JJt))

            # Joint update
            delta_theta = np.dot(J_pinv, error)
            current_thetas += 0.5 * delta_theta # Learning rate / damping step

        return current_thetas, max_iterations, False

def run_robotics_demo():
    print_header("3-DOF Manipulator Inverse Kinematics (IK) Solver")
    arm = RoboticArm3DOF(link_lengths=[1.2, 0.9, 0.6])

    current_pos = arm.forward_kinematics(arm.thetas)
    print(f"Current Joint Angles: {[f'{math.degrees(t):.1f}°' for t in arm.thetas]}")
    print(f"Current End-Effector: (X: {current_pos[0]:.3f} m, Y: {current_pos[1]:.3f} m)")

    # Define target goal point in operational workspace
    target = np.array([1.5, 1.2])
    print(f"\n🎯 Commanded Target Cartesian Coordinates: (X: {target[0]:.3f} m, Y: {target[1]:.3f} m)")

    solution_thetas, iterations, converged = arm.solve_inverse_kinematics(target)
    achieved_pos = arm.forward_kinematics(solution_thetas)
    final_error = np.linalg.norm(target - achieved_pos) * 1000.0 # in mm

    print(f"\nIK Solver Result:")
    print(f"   Converged   : {'✔ YES' if converged else '❌ NO'} in {iterations} iterations")
    print(f"   Solved Joint: {[f'{math.degrees(t):.2f}°' for t in solution_thetas]}")
    print(f"   Achieved Pos: (X: {achieved_pos[0]:.4f} m, Y: {achieved_pos[1]:.4f} m)")
    print(f"   Residual Err: {final_error:.3f} mm")
    print("\n💡 Deeptech Takeaway: Real-time closed-loop IK is vital for surgical & space robotics!")

if __name__ == "__main__":
    run_robotics_demo()
