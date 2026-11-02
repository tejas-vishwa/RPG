"""
Unit tests for the Random Password Generator core logic and GUI behavior.
"""

import string
import unittest
import tkinter as tk
from unittest.mock import patch

from app import generate_secure_password, PasswordGeneratorApp


class TestSecurePasswordGenerator(unittest.TestCase):
    """Test suite for core password generation logic."""

    def test_default_generation(self):
        """Test default length 12 with all categories enabled."""
        for _ in range(50):
            pwd = generate_secure_password(
                length=12,
                use_upper=True,
                use_lower=True,
                use_digits=True,
                use_symbols=True
            )
            self.assertEqual(len(pwd), 12)
            self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
            self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
            self.assertTrue(any(c in string.digits for c in pwd))
            self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_minimum_length_with_all_categories(self):
        """Test minimum valid length 4 when all 4 categories are selected."""
        for _ in range(20):
            pwd = generate_secure_password(
                length=4,
                use_upper=True,
                use_lower=True,
                use_digits=True,
                use_symbols=True
            )
            self.assertEqual(len(pwd), 4)
            self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
            self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
            self.assertTrue(any(c in string.digits for c in pwd))
            self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_single_category_uppercase_only(self):
        """Ensure only uppercase characters appear when only uppercase is enabled."""
        for _ in range(20):
            pwd = generate_secure_password(
                length=16,
                use_upper=True,
                use_lower=False,
                use_digits=False,
                use_symbols=False
            )
            self.assertEqual(len(pwd), 16)
            self.assertTrue(all(c in string.ascii_uppercase for c in pwd))

    def test_subset_categories(self):
        """Ensure only selected categories (digits and lowercase) appear."""
        for _ in range(20):
            pwd = generate_secure_password(
                length=20,
                use_upper=False,
                use_lower=True,
                use_digits=True,
                use_symbols=False
            )
            self.assertEqual(len(pwd), 20)
            self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
            self.assertTrue(any(c in string.digits for c in pwd))
            self.assertFalse(any(c in string.ascii_uppercase for c in pwd))
            self.assertFalse(any(c in string.punctuation for c in pwd))

    def test_no_categories_selected_raises_error(self):
        """Should raise ValueError if no categories are enabled."""
        with self.assertRaises(ValueError):
            generate_secure_password(
                length=10,
                use_upper=False,
                use_lower=False,
                use_digits=False,
                use_symbols=False
            )

    def test_length_less_than_categories_raises_error(self):
        """Should raise ValueError if requested length is shorter than category count."""
        with self.assertRaises(ValueError):
            generate_secure_password(
                length=3,
                use_upper=True,
                use_lower=True,
                use_digits=True,
                use_symbols=True
            )


class TestGUIComponents(unittest.TestCase):
    """Test suite for Tkinter GUI widgets and interactions."""

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide window during test execution
        self.app = PasswordGeneratorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        """Verify initial defaults: length 12, all 4 checkboxes True, status Ready."""
        self.assertEqual(self.app.length_var.get(), "12")
        self.assertTrue(self.app.upper_var.get())
        self.assertTrue(self.app.lower_var.get())
        self.assertTrue(self.app.digits_var.get())
        self.assertTrue(self.app.symbols_var.get())
        self.assertEqual(self.app.status_var.get(), "Ready.")
        self.assertEqual(self.app.output_entry.get(), "")

    @patch("tkinter.messagebox.showwarning")
    def test_invalid_length_string(self, mock_warn):
        """Test non-numeric length validation."""
        self.app.length_var.set("invalid")
        self.app.on_generate()
        mock_warn.assert_called_once()
        self.assertIn("Error", self.app.status_var.get())

    @patch("tkinter.messagebox.showwarning")
    def test_length_less_than_four(self, mock_warn):
        """Test length < 4 warning."""
        self.app.length_var.set("3")
        self.app.on_generate()
        mock_warn.assert_called_once()
        self.assertIn("Error", self.app.status_var.get())

    @patch("tkinter.messagebox.showwarning")
    def test_no_options_warning(self, mock_warn):
        """Test zero options warning."""
        self.app.length_var.set("10")
        self.app.upper_var.set(False)
        self.app.lower_var.set(False)
        self.app.digits_var.set(False)
        self.app.symbols_var.set(False)
        self.app.on_generate()
        mock_warn.assert_called_once()
        self.assertIn("Error", self.app.status_var.get())

    def test_generate_and_clear(self):
        """Test generate button populates output, and clear resets it."""
        self.app.length_var.set("16")
        self.app.on_generate()
        generated = self.app.output_entry.get()
        self.assertEqual(len(generated), 16)
        self.assertEqual(self.app.status_var.get(), "Password generated successfully!")

        # Clear
        self.app.on_clear()
        self.assertEqual(self.app.length_var.get(), "12")
        self.assertEqual(self.app.output_entry.get(), "")
        self.assertEqual(self.app.status_var.get(), "Ready.")

    def test_clipboard_copy(self):
        """Test copying generated password."""
        self.app.length_var.set("14")
        self.app.on_generate()
        pwd = self.app.output_entry.get()

        self.app.on_copy()
        clipboard_content = self.root.clipboard_get()
        self.assertEqual(clipboard_content, pwd)
        self.assertEqual(self.app.status_var.get(), "Password copied to clipboard!")


if __name__ == "__main__":
    unittest.main()
