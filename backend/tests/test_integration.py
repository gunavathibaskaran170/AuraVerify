"""
Integration Test

RepoReader
        +
StackDetector
"""

import os

import pytest
from dotenv import load_dotenv

from agent.repo_reader import RepoReader
from agent.stack_detector import detect_stack

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

REPO_URL = "https://github.com/tiangolo/fastapi"


@pytest.mark.skipif(TOKEN is None, reason="GITHUB_TOKEN not configured")
def test_fastapi_repository():

    reader = RepoReader(TOKEN)

    tree = reader.get_file_tree(REPO_URL)

    result = detect_stack(tree["files"])

    assert result["stack"] == "python"
    assert result["framework"] == "fastapi"