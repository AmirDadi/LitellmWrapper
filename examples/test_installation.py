"""
Test if liteToolLlm is installed correctly.

This script imports key components from the library to verify that
the installation is working properly.
"""

def test_imports():
    try:
        # Try importing directly from the top-level package

            # If that fails, try importing from the litetoolllm module
        from litetoolllm import structured_completion, astructured_completion, Tool
        from litetoolllm import UnifiedResponse, StructuredValidationError
        print("✅ Successfully imported from 'litetoolllm' module!")
        
        # If we get here, either import worked
        print("\nAvailable components:")
        print("  - structured_completion")
        print("  - astructured_completion")
        print("  - Tool")
        print("  - UnifiedResponse")
        print("  - StructuredValidationError")
        
        # Print installation instructions
        print("\nTo use liteToolLlm in your projects, add it to your requirements.txt:")
        print("git+https://github.com/AmirDadi/liteToolLlm.git")
        print("\nIn your code, import using:")
        print("from litetoolllm import structured_completion, astructured_completion")
        print("# OR")
        print("from litecallllm import structured_completion, astructured_completion  # if this works in your environment")
        
        return True
    except ImportError as e:
        print(f"❌ Error importing the library: {e}")
        print("\nMake sure you've installed the package with:")
        print("pip install git+https://github.com/AmirDadi/liteToolLlm.git")
        print("\nIf you've already installed it, try importing directly from the litetoolllm module:")
        print("from litetoolllm import structured_completion, astructured_completion")
        return False

if __name__ == "__main__":
    test_imports() 