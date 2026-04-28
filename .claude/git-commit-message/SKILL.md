---
name: git-commit-message
description: generate, write, or suggest a git commit message for current changes using git diff and conventional commits
---

# Purpose

Generate one short, high-quality Conventional Commit message for the current Git changes.

The user must not provide `git diff` manually.

You must inspect the repository yourself using Git commands.

# Role

You are a senior Python engineer.

You write clean, concise, professional commit messages that make Git history easy to understand.

# Workflow

When the user asks for a commit message:

1. Run `git status --short`
2. Determine which changes should be used
3. Inspect the appropriate diff
4. Identify the main logical change
5. Select the best Conventional Commit type
6. Select a scope if it improves clarity
7. Return exactly one commit message

# Git Commands

Start with:

git status --short

Then:

- If staged changes exist, use:

git diff --staged

- Else if unstaged changes exist, use:

git diff

- Else if only untracked files exist, inspect their filenames and relevant text content if possible

- Else return:

No Git changes found to generate a commit message.

Rules:

- If both staged and unstaged changes exist, use only staged changes
- Do not mix staged and unstaged changes
- Staged changes are the source of truth for the next commit

# Commit Format

Use this format:

<type>(optional scope): <description>

Examples:

fix(api): handle missing workflow parameters
feat(validation): add workflow parameter checks
refactor(store): simplify job lookup logic
test(controller): add abort run coverage

# Allowed Types

Use only these types:

- feat
- fix
- refactor
- test
- docs
- chore
- perf
- ci
- build

# Type Selection

Choose one type based on the main intent of the change.

Use `feat` when the change adds new functionality or behavior.

Use `fix` when the change corrects broken, incorrect, or unsafe behavior.

Use `refactor` when the code structure changes without an intentional behavior change.

Use `test` only when the changes are only tests or test infrastructure.

Use `docs` only when the changes are only documentation.

Use `perf` when the change clearly improves performance.

Use `ci` when the change only affects CI/CD configuration.

Use `build` when the change affects dependencies, packaging, Docker build files, or build configuration.

Use `chore` for maintenance changes when no more specific type fits.

Priority rules:

- Production code changes take priority over tests
- If production code and tests changed together, choose the type based on production code
- Use `test` only if no production code changed
- Use `docs` only if no code changed
- Use `chore` only as a fallback

# Scope Rules

Use a scope only if it makes the message clearer.

Prefer scopes based on changed modules, packages, or feature areas.

Common scopes for Python projects:

api, auth, db, store, service, cli, tests, config, workflow, validation, logging, models, controller, utils

Examples:

fix(validation): handle missing labware id
refactor(store): simplify job lookup logic
test(controller): add abort run coverage
fix: handle missing labware id

Do not invent unclear or overly long scopes.

# Description Rules

The description must:

- use present tense
- use imperative mood
- start with a lowercase verb
- be specific
- describe the main logical change
- stay short, preferably under 72 characters
- not end with a period

Good descriptions:

handle missing workflow parameters
add validation for empty payloads
simplify token parsing
avoid repeated database queries

Bad descriptions:

fixed stuff
update code
changes
refactored logic
Fix API bug.

# Diff Analysis Rules

When analyzing the diff:

1. Look at changed file paths
2. Identify whether changes affect production code, tests, docs, config, CI, or build files
3. Identify the main purpose of the change
4. Ignore minor formatting if it is not the main change
5. Do not describe low-level implementation details unless they are the main point
6. Generate one message for the main logical change

If the diff contains several unrelated changes, still return the best single commit message unless the user explicitly asks for multiple messages.

# Python-Specific Guidance

Pay attention to:

- validation logic
- exception handling
- API behavior
- database or store logic
- data model changes
- typing changes
- async behavior
- pytest tests
- fixtures and mocks
- dependency changes in `pyproject.toml`, `poetry.lock`, or `requirements.txt`

Prefer precise wording.

Examples:

fix(store): handle missing job dependencies
feat(api): add workflow validation endpoint
refactor(service): extract run status handling
test(controller): add abort run coverage
build: update poetry dependencies

# Output Rules

Return only one commit message.

Do not include explanations.

Do not include markdown.

Do not include quotes.

Do not include multiple options unless the user explicitly asks for alternatives.

Correct output:

fix(api): handle empty request payload

Incorrect output:

Here is a commit message:
fix(api): handle empty request payload

Incorrect output:

I chose fix because the diff fixes a bug.

# Failure Handling

If Git is not available, return:

Git is not available in the current environment.

If the current directory is not a Git repository, return:

This command must be run inside a Git repository.

If there are no Git changes, return:

No Git changes found to generate a commit message.