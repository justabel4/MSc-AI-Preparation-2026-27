# MSc AI Preparation — Command Cheat Sheet

A quick reminder of the terminal commands used so far during setup and Python/Git practice.

## 1. Miniconda / Conda

### Check Miniconda directly
```powershell
& "$env:USERPROFILE\miniconda3\Scripts\conda.exe" --version
```

### Initialise Conda for PowerShell
```powershell
& "$env:USERPROFILE\miniconda3\Scripts\conda.exe" init powershell
```

After running this, close PowerShell completely and open it again.

### Check Conda normally
```powershell
conda --version
```

### Create the AI environment with Python 3.12
```powershell
conda create -n ai-foundations python=3.12
```

When asked `Proceed ([y]/n)?`, type:
```text
y
```

### Activate the AI environment
```powershell
conda activate ai-foundations
```

You should see `(ai-foundations)` at the start of the terminal prompt.

### Check the Python version
```powershell
python --version
```

Expected: Python 3.12.x

### Install the first Python libraries
```powershell
python -m pip install numpy pandas matplotlib jupyter
```

### Test that the libraries import correctly
```powershell
python -c "import numpy, pandas, matplotlib; print('AI environment ready')"
```

---

## 2. PowerShell PATH troubleshooting

These were used when Conda activation failed because of a malformed PATH entry.

### Show User PATH entries one per line
```powershell
[Environment]::GetEnvironmentVariable("Path", "User") -split ";"
```

### Show System/Machine PATH entries one per line
```powershell
[Environment]::GetEnvironmentVariable("Path", "Machine") -split ";"
```

### Search the Machine PATH for Opera or stray quotation marks
```powershell
[Environment]::GetEnvironmentVariable("Path", "Machine") -split ";" | Where-Object { $_ -match 'Opera|"' }
```

### Search the currently loaded PATH for Opera or stray quotation marks
```powershell
$env:Path -split ";" | Where-Object { $_ -match 'Opera|"' }
```

---

## 3. Git setup and checks

### Check Git is installed
```powershell
git --version
```

### Check the Git username configured on the computer
```powershell
git config --global user.name
```

### Check the Git email configured on the computer
```powershell
git config --global user.email
```

### Set Git username if needed
```powershell
git config --global user.name "Your Name"
```

### Set Git email if needed
```powershell
git config --global user.email "your-github-email@example.com"
```

---

## 4. Starting a Git repository

Run these from the project folder.

### Initialise Git
```powershell
git init
```

### Check repository status
```powershell
git status
```

### Stage all changes
```powershell
git add .
```

### Create a commit
```powershell
git commit -m "Describe what you changed"
```

### Rename the branch to main
```powershell
git branch -M main
```

---

## 5. Connecting the local project to GitHub

### Add the GitHub repository as `origin`
Only do this once for the repository.

```powershell
git remote add origin https://github.com/justabel4/MSc-AI-Preparation-2026-27.git
```

If you run it again and see:
```text
error: remote origin already exists.
```
that is fine — it means the remote is already configured.

### First push to GitHub
```powershell
git push -u origin main
```

The `-u` makes the local `main` branch track the GitHub `main` branch.

### Normal pushes after the first one
```powershell
git push
```

---

## 6. GitHub authentication troubleshooting

GitHub does not accept account passwords for HTTPS Git operations.

### Tell Git to use Git Credential Manager
```powershell
git config --global credential.helper manager
```

Then retry:
```powershell
git push -u origin main
```

Complete the GitHub sign-in in the browser if prompted.

### Remove an old/bad cached GitHub credential if needed
```powershell
cmdkey /delete:git:https://github.com
```

Then retry the push.

---

## 7. Normal Git workflow from now on

After editing or creating files:

```powershell
git status
git add .
git commit -m "Describe the change"
git push
```

Think of the workflow as:

```text
Edit files
   ↓
git status
   ↓
git add .
   ↓
git commit
   ↓
git push
   ↓
GitHub
```

- `git status` = see what changed
- `git add .` = choose/stage changes for the next snapshot
- `git commit` = save the snapshot locally
- `git push` = upload committed changes to GitHub

---

## 8. Useful checks when something feels wrong

### Am I in the correct Conda environment?
```powershell
conda activate ai-foundations
python --version
```

### Does Git see my changes?
```powershell
git status
```

### Did I already configure the GitHub remote?
```powershell
git remote -v
```

### Is my branch connected to GitHub?
```powershell
git status
```

A healthy result should say something similar to:
```text
On branch main
Your branch is up to date with 'origin/main'.
```

---

## Project details

- Local project folder: `D:\Documents\MSc AI 2027`
- Conda environment: `ai-foundations`
- Python target: `3.12`
- GitHub repository: `justabel4/MSc-AI-Preparation-2026-27`
