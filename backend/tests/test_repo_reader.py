"""
tests/test_repo_reader.py

Unit tests for RepoReader.

Run:
    pytest backend/tests/test_repo_reader.py
"""

import os

import pytest
from dotenv import load_dotenv

from agent.repo_reader import RepoReader

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
REPO_URL = "https://github.com/tiangolo/fastapi"


@pytest.mark.skipif(TOKEN is None, reason="GITHUB_TOKEN not configured")
def test_repository_exists():
    reader = RepoReader(TOKEN)

    assert reader.repository_exists(REPO_URL) is True


@pytest.mark.skipif(TOKEN is None, reason="GITHUB_TOKEN not configured")
def test_get_file_tree():

    reader = RepoReader(TOKEN)

    result = reader.get_file_tree(REPO_URL)

    assert "files" in result
    assert isinstance(result["files"], list)
    assert len(result["files"]) > 0


@pytest.mark.skipif(TOKEN is None, reason="GITHUB_TOKEN not configured")
def test_get_file_content():

    reader = RepoReader(TOKEN)

    content = reader.get_file_content(
        REPO_URL,
        "README.md"
    )

    assert isinstance(content, str)
    assert len(content) > 0