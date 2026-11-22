# Suggested Git Commit Messages

Use the message that matches the changes actually staged in Git.

| Situation | Suggested commit message |
|---|---|
| Add the three Python programs | `feat: add factorial, fibonacci, and student programs` |
| Add project overview and usage instructions | `docs: add project README with setup and examples` |
| Add assignment report and AI prompts | `docs: document assignment workflow and AI prompts` |
| Improve input validation | `fix: handle invalid numeric inputs` |
| Improve code comments and formatting | `style: improve readability of Python scripts` |

## Recommended first commit

```bash
git add factorial.py fibonacci.py student.py README.md
git commit -m "feat: add beginner Python practice programs"
```

## Recommended documentation commit

```bash
git add ASSIGNMENT-DOCUMENTATION.md AI-PROMPTS.md COMMIT-MESSAGES.md
git commit -m "docs: add assignment report and AI documentation"
```

A commit message should describe the staged changes, not the entire project in general.
