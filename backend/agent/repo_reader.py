"""
repo_reader.py

Reads GitHub repositories using the authenticated user's
GitHub OAuth access token.
"""

from github import Github, Auth
from github.GithubException import GithubException


class RepoReader:
    """
    Reads GitHub repositories using PyGithub.
    """

    MAX_FILES = 500

    def __init__(self, access_token: str):
        """
        Initialize the GitHub client.

        Args:
            access_token (str): GitHub OAuth access token.
        """
        if not access_token:
            raise ValueError("GitHub access token is required.")

        # Recommended authentication method for PyGithub 2.x
        auth = Auth.Token(access_token)
        self.gh = Github(auth=auth)

    def _extract_repo_name(self, repo_url: str) -> str:
        """
        Convert a GitHub repository URL into owner/repository format.

        Example:
            https://github.com/octocat/Hello-World
            -> octocat/Hello-World
        """
        prefix = "https://github.com/"

        if not repo_url.startswith(prefix):
            raise ValueError("Invalid GitHub repository URL.")

        return repo_url.replace(prefix, "").rstrip("/")

    def repository_exists(self, repo_url: str) -> bool:
        """
        Check whether a repository exists.

        Args:
            repo_url (str): GitHub repository URL.

        Returns:
            bool
        """
        repo_name = self._extract_repo_name(repo_url)

        try:
            self.gh.get_repo(repo_name)
            return True

        except GithubException:
            return False

    def get_file_tree(self, repo_url: str) -> dict:
        """
        Fetch the repository file tree.

        Returns:
            {
                "files": [...],
                "truncated": bool,
                "warning": str | None,
                "total_files": int,
                "returned_files": int
            }
        """

        repo_name = self._extract_repo_name(repo_url)

        try:
            repo = self.gh.get_repo(repo_name)

            tree = repo.get_git_tree(
                sha="HEAD",
                recursive=True,
            )

            files = [
                item.path
                for item in tree.tree
                if item.type == "blob"
            ]

            warning = None

            if tree.truncated:
                warning = (
                    "GitHub truncated the repository tree because "
                    "it exceeded GitHub's response size limit. "
                    "Only the first part of the repository "
                    "was analyzed."
                )

            return {
                "files": files[: self.MAX_FILES],
                "truncated": tree.truncated,
                "warning": warning,
                "total_files": len(files),
                "returned_files": min(len(files), self.MAX_FILES),
            }

        except GithubException as e:
            raise Exception(f"GitHub API Error: {e.data}") from e

    def get_file_content(self, repo_url: str, path: str) -> str:
        """
        Read the content of a file from a GitHub repository.

        Args:
            repo_url (str): GitHub repository URL.
            path (str): File path inside the repository.

        Returns:
            str
        """

        repo_name = self._extract_repo_name(repo_url)

        try:
            repo = self.gh.get_repo(repo_name)

            file = repo.get_contents(path)

            return file.decoded_content.decode(
                "utf-8",
                errors="replace",
            )

        except GithubException as e:
            raise Exception(
                f"Unable to read file '{path}': {e.data}"
            ) from e