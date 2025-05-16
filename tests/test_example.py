"""Tests for the example module."""

from my_package import example

def test_hello_world():
    """Test the hello_world function."""
    assert example.hello_world() == "Hello, World!"

def test_add():
    """Test the add function."""
    assert example.add(1, 2) == 3
    assert example.add(-1, 1) == 0
    assert example.add(0, 0) == 0
