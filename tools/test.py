import sys
from pathlib import Path

# Ensure the project root is on sys.path when running this script directly.
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tools.calculator import Calculator

tool = Calculator()

print(tool.name)
print(tool.description)
print(tool.execute("25 * 12"))
