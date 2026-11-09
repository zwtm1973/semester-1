# Week 1.7, Session 1: Task 2 - unit test for comfort_level() 

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

def test_cold():
    assert comfort_level(3.4) == "COLD"
    assert comfort_level(0) == "COLD"
    assert comfort_level(-1.0) == "COLD"

def test_hot():
    assert comfort_level(100.0) == "HOT"
    assert comfort_level(25.2) == "HOT"
    assert comfort_level(31.0) == "HOT"

def test_ok():
    assert comfort_level(25.0) == "OK"
    assert comfort_level(18.9) == "OK"
    assert comfort_level(22.1) == "OK"
