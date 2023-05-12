#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

HBNBCommand = console.HBNBCommand


class ConsoleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.console = HBNBCommand()
    
    def tearDown(self):
        self.console = None
    
    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
    
    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(output)
    
    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            output = f.getvalue().strip()
            self.assertIn("No instance found", output)
    
    # Add more test methods for other commands and features
    
if __name__ == '__main__':
    unittest.main()
