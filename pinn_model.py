# PINN - Physics loss + Data loss combine
# Loss = MSE_data + lambda * MSE_physics
# Physics: Q - U*A*LMTD = 0 hona chahida hai
# Eh hi cheez Siemens, GE, Honeywell use karde ne
def pinn_loss(y_true, y_pred, U_pred, A, LMTD, Q_true, lam=0.1):
    import numpy as np
    data_loss = np.mean((y_true - y_pred)**2)
    physics_residual = Q_true - U_pred * A * LMTD
    physics_loss = np.mean(physics_residual**2)
    return data_loss + lam * physics_loss