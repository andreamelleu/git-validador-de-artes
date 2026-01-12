# Mock pyiceberg package to avoid import errors from supabase dependencies
__version__ = "0.0.1"

# Mock common imports that might be needed
class MockCatalog:
    pass

class MockRestCatalog:
    pass
