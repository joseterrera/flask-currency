"""Tests for currency converter"""

from unittest import TestCase
from app import app


class CurrencyConvertedTestCase(TextCase):
  def setUp(self):
    self.client = app.test_client()

  def test_from_shows(self):
    """Test that form aapears"""

    resp = self.client.get("/")
    self.assertIn(b'<form', resp.data)

  def test_form_failures(self):
    """Test conversion failures"""

    resp = self.client.get("/convert",
                          query_string={"code_from":"PROUST", "code_to": "JOYCE", "amt": "LADY"})
    self.assertIn(b'Not a valid amount', resp.data)
    self.assertIn(b'Not a valid code: PROUST', resp.data)
    self.assertIn(b'Not a valid code: JOYCE', resp.data)

  def test_conversion(self):
    """Test conversion"""

    resp = self.client.get("/convert", query_string={"code_from": "USD", "code_to": "USD", "amt": "1.55"})

    self.assertIn(b'$1.55', resp.data)