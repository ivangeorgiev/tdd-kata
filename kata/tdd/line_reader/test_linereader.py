from unittest import TestCase
from unittest.mock import MagicMock, patch
from .linereader import readFromFile

class TestReadFromFileFunction(TestCase):
    def test_returns_correct_string(self):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="first line")
        mock_open = MagicMock(return_value=mock_file)
        mock_open.return_value.__enter__.return_value = mock_file
        # .return_value = mock_file
        with patch("builtins.open", mock_open):
            result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r", encoding="utf8")
        self.assertEqual(result, "first line")

    def test_throws_exception_file_doesnt_exist(self):
        with self.assertRaises(FileNotFoundError):
            readFromFile(__file__ + 'IdoNotExist')
