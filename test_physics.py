import math
from physics import conduction, convection, radiation, lmtd, heat_duty
from kern_method import kern_shell_tube_design, pressure_drop, fouling_factor
from cost import total_cost


def test_conduction():
    assert conduction(50, 2, 30, 0.01) == 300000


def test_convection():
    assert convection(10, 2, 80, 30) == 1000


def test_radiation_zero_at_equal_temp():
    assert radiation(0.9, 1, 300, 300) == 0


def test_lmtd_and_duty():
    assert math.isclose(lmtd(50, 50), 50)
    assert lmtd(60, 30) > 0
    assert heat_duty(1000, 2, 40) == 80000


def test_kern():
    r = kern_shell_tube_design(1.2, 90, 50, 1.0, 25, 45, 3.0)
    assert r['Q'] > 0 and r['U'] > 0


def test_fouling_and_pressure_drop():
    assert fouling_factor(1500, 1200) > 0
    assert pressure_drop(1.0) > 0


def test_cost():
    assert total_cost(3, 1400, 50000, 20000, 15000)['Capital_Cost_USD'] > 0
