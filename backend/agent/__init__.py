"""
AuraVerify Agent Package

This package contains modules responsible for:
- Reading GitHub repositories
- Detecting the technology stack and framework
- Future AI-powered repository analysis
"""

__version__ = "0.1.0"

__all__ = [
    "RepoReader",
    "detect_stack",
]

# These imports allow:
# from agent import RepoReader, detect_stack
# instead of:
# from agent.repo_reader import RepoReader
# from agent.stack_detector import detect_stack

from .repo_reader import RepoReader
from .stack_detector import detect_stack