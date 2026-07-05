"""
tests/test_stack_detector.py

Unit tests for the AuraVerify stack detector.

Run:
    pytest backend/tests/
"""

from agent.stack_detector import detect_stack


def test_django_project():
    """Should detect a Django project."""

    file_tree = [
        "manage.py",
        "requirements.txt",
        "blog/settings.py",
        "blog/urls.py",
        "blog/models.py",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "python"
    assert result["framework"] == "django"


def test_flask_project():
    """Should detect a Flask project."""

    file_tree = [
        "requirements.txt",
        "app.py",
        "templates/index.html",
        "static/style.css",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "python"
    assert result["framework"] == "flask"


def test_fastapi_project():
    """Should detect a FastAPI project."""

    file_tree = [
        "requirements.txt",
        "pyproject.toml",
        "fastapi/main.py",
        "routers/users.py",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "python"
    assert result["framework"] == "fastapi"


def test_express_project():
    """Should detect an Express.js project."""

    file_tree = [
        "package.json",
        "express.js",
        "routes/users.js",
        "controllers/auth.js",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "nodejs"
    assert result["framework"] == "express"


def test_nextjs_project():
    """Should detect a Next.js project."""

    file_tree = [
        "package.json",
        "next.config.js",
        "pages/index.tsx",
        "app/layout.tsx",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "nodejs"
    assert result["framework"] == "nextjs"


def test_spring_project():
    """Should detect a Spring Boot project."""

    file_tree = [
        "pom.xml",
        "src/main/java/Application.java",
        "SpringApplication.java",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "java"
    assert result["framework"] == "spring"


def test_plain_python_project():
    """Should detect plain Python without a framework."""

    file_tree = [
        "requirements.txt",
        "main.py",
        "utils.py",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "python"
    assert result["framework"] == "unknown"


def test_unknown_project():
    """Should return unknown when no stack is detected."""

    file_tree = [
        "README.md",
        "LICENSE",
        "notes.txt",
        "image.png",
    ]

    result = detect_stack(file_tree)

    assert result["stack"] == "unknown"
    assert result["framework"] == "unknown"