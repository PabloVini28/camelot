"""Test doubles shared by the test modules.

Kept apart from the test files so each test module sticks to one style
(plain test functions) instead of mixing module-level classes in.
"""


class PopplerBackendError:
    def convert(self, pdf_path, png_path, page=1):
        raise ValueError("Image conversion failed")


class GhostscriptBackendError:
    def convert(self, pdf_path, png_path, page=1):
        raise ValueError("Image conversion failed")


class GhostscriptBackendNoError:
    def convert(self, pdf_path, png_path, page=1):
        pass


class PdfiumBackendError:
    def convert(self, pdf_path, png_path, page=1):
        raise ValueError("Image conversion failed")
