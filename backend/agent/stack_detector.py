"""
stack_detector.py

Detects the programming language stack and framework
used by a GitHub repository.
"""

from typing import List, Dict

# -----------------------------
# Stack Detection Signals
# -----------------------------

STACK_SIGNALS = {
    "python": [
        "requirements.txt",
        "setup.py",
        "pipfile",
        "pyproject.toml",
        ".py",
    ],

    "nodejs": [
        "package.json",
        ".js",
        ".ts",
    ],

    "java": [
        "pom.xml",
        "build.gradle",
        ".java",
    ],

    "go": [
        "go.mod",
        ".go",
    ],

    "php": [
        "composer.json",
        ".php",
    ],
}

# -----------------------------
# Framework Detection Signals
# -----------------------------

FRAMEWORK_SIGNALS = {

    "django": [
        "manage.py",
        "settings.py",
        "urls.py",
    ],

    "flask": [
        "app.py",
        "wsgi.py",
    ],

    "fastapi": [
        "fastapi",
    ],

    "express": [
        "express",
    ],

    "nextjs": [
        "next.config",
        "pages/",
        "app/",
    ],

    "spring": [
        "springapplication",
        "@springbootapplication",
    ],
}


def detect_stack(file_tree: List[str]) -> Dict[str, str]:
    """
    Detect the project's stack and framework.

    Parameters
    ----------
    file_tree : list[str]

    Returns
    -------
    {
        "stack": "...",
        "framework": "..."
    }
    """

    flat = " ".join(file_tree).lower()

    stack_scores = {}

    for stack, signals in STACK_SIGNALS.items():

        score = 0

        for signal in signals:

            if signal.lower() in flat:
                score += 1

        stack_scores[stack] = score

    framework_scores = {}

    for framework, signals in FRAMEWORK_SIGNALS.items():

        score = 0

        for signal in signals:

            if signal.lower() in flat:
                score += 1

        framework_scores[framework] = score

    stack = max(stack_scores, key=stack_scores.get)

    if stack_scores[stack] == 0:
        stack = "unknown"

    framework = max(
        framework_scores,
        key=framework_scores.get
    )

    if framework_scores[framework] == 0:
        framework = "unknown"

    return {
        "stack": stack,
        "framework": framework,
    }


def print_detection(result: Dict[str, str]) -> None:
    """
    Pretty print detection result.
    """

    print("\n========== Detection ==========")

    print(f"Stack      : {result['stack']}")

    print(f"Framework  : {result['framework']}")

    print("===============================\n")