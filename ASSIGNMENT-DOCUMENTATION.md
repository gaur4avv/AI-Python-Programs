# Assignment 5: GitHub Documentation with AI

## 1. Objective

To upload Python programs to GitHub and use AI assistance to prepare a README file and meaningful Git commit messages.

## 2. Repository information

- **Repository name:** `AI-Python-Programs`
- **Suggested visibility:** Public (if permitted by the course instructions)
- **Platform:** GitHub
- **Language:** Python 3
- **Author:** Gaurav Kumar
- **Institution:** JECRC University

Replace `YOUR-GITHUB-USERNAME` in the clone URL and submission details with the actual GitHub username.

## 3. Programs uploaded

| S. No. | File name | Description |
|---:|---|---|
| 1 | `factorial.py` | Calculates the factorial of a non-negative integer using recursion. |
| 2 | `fibonacci.py` | Generates the Fibonacci sequence using a loop. |
| 3 | `student.py` | Stores and displays student details using a Python class. |

## 4. Technologies and concepts

- Python 3
- Git for version control
- GitHub for remote repository hosting
- AI assistance for documentation and commit-message drafting
- Recursion, loops, functions, classes, objects, and input validation

## 5. Repository structure

```text
AI-Python-Programs/
├── factorial.py
├── fibonacci.py
├── student.py
├── README.md
├── ASSIGNMENT-DOCUMENTATION.md
├── AI-PROMPTS.md
├── COMMIT-MESSAGES.md
├── .gitignore
└── LICENSE
```

## 6. Steps to upload the project

1. Sign in to GitHub and create a repository named `AI-Python-Programs`.
2. Choose the required visibility. Do not initialize it with another README if you plan to upload this project's files directly.
3. Extract this project folder on your computer.
4. Open a terminal inside the extracted folder.
5. Configure Git if it has not already been configured:

   ```bash
   git config --global user.name "Gaurav Kumar"
   git config --global user.email "YOUR-GITHUB-EMAIL"
   ```

6. Initialize and push the project:

   ```bash
   git init
   git add .
   git commit -m "feat: add beginner Python practice programs"
   git branch -M main
   git remote add origin https://github.com/YOUR-GITHUB-USERNAME/AI-Python-Programs.git
   git push -u origin main
   ```

7. Refresh the GitHub repository page and verify that the three Python files and documentation are visible.

If the repository already contains a README or other files, clone it first or pull and resolve the existing history instead of blindly repeating the initialization commands.

## 7. AI prompt used for README generation

The prompt used as a starting point for AI-assisted documentation is recorded in `AI-PROMPTS.md`.

## 8. Meaningful Git commit messages

Suggested commit messages are recorded in `COMMIT-MESSAGES.md`. Use a message that accurately describes the changes included in each commit. Do not claim a test or feature was completed unless it was actually done.

## 9. Testing and sample outputs

Run each script using Python 3:

```bash
python factorial.py
python fibonacci.py
python student.py
```

Expected examples:

- Factorial input `5` produces `5! = 120`.
- Fibonacci count `7` produces `0 1 1 2 3 5 8`.
- Student details are printed after valid name, roll number, and course inputs.

Also test invalid input, such as a negative factorial number or a negative Fibonacci count. The programs display an error instead of producing a valid result.

## 10. Conclusion

The assignment demonstrates how Python source files can be organized and published in a GitHub repository. AI assistance can help create clear project documentation and useful commit-message suggestions. The final repository should be checked manually to confirm that the uploaded files, README, and commit history are correct.

## 11. Submission checklist

- [ ] GitHub repository created with the name `AI-Python-Programs`
- [ ] `factorial.py` uploaded
- [ ] `fibonacci.py` uploaded
- [ ] `student.py` uploaded
- [ ] `README.md` visible on the repository home page
- [ ] Documentation and AI prompt files uploaded
- [ ] Commit history contains meaningful messages
- [ ] All three programs run successfully
- [ ] Repository URL added to the final submission
- [ ] Screenshots captured from the actual GitHub repository
