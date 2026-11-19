import numpy as np
def kern_shell_tube_design(m_hot, Th_in, Th_out, m_cold, Tc_in, Tc_out, Area):
    # Kern Method - Industrial Standard for Shell & Tube
    Cp = 4186
    Q = m_hot * Cp * (Th_in - Th_out)
    dT1 = max(Th_in - Tc_out, 0.1)
    dT2 = max(Th_out - Tc_in, 0.1)
    LMTD = (dT1 - dT2) / np.log(dT1/dT2)
    # Correction factor F for Shell & Tube (1 shell, 2 tube passes)
    R = (Th_in - Th_out) / (Tc_out - Tc_in + 1e-6)
    P = (Tc_out - Tc_in) / (Th_in - Tc_in + 1e-6)
    F = 0.95  # Simplified, real me Bell-Delaware use hunda
    U = Q / (Area * LMTD * F)
    return {'Q': Q, 'LMTD': LMTD, 'F_factor': F, 'U': U}

def pressure_drop(m, rho=1000, D=0.02, L=5, f=0.02):
    # Darcy-Weisbach - Pump sizing layi
    v = m / (rho * 3.14 * (D/2)**2)
    dp = f * (L/D) * (rho * v**2 / 2)
    return dp

def fouling_factor(U_clean, U_fouled):
    # Fouling Resistance - Industry ch sab to important
    return (1/U_fouled) - (1/U_clean)