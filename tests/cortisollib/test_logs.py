import unittest
from pathlib import Path
from cortisol.cortisollib.logs import render_locustfile, get_cost_estimate


class TestYourFunctions(unittest.TestCase):
    def setUp(self):
        # Create temporary files for testing
        self.cortisol_file = Path("test_cortisol.txt")
        self.log_file = Path("test_log.txt")

    def tearDown(self):
        # Clean up temporary files after testing
        self.cortisol_file.unlink(missing_ok=True)
        self.log_file.unlink(missing_ok=True)

    def test_render_locustfile(self):
        # Create a temporary cortisol input file for testing
        cortisol_input = "user_data: test"
        self.cortisol_file.write_text(cortisol_input)

        rendered_content = render_locustfile(self.cortisol_file)

        # Check if the rendered content contains the expected string
        self.assertIn("user_data: test", rendered_content)
