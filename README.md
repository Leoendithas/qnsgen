# QnsGen

A Python project for using LLMs to generate follow-up questions for teachers based on the identified learning gaps of students. 
This is a project for Govtech AI Champion's Bootcamp 2024.

<img width="1841" height="901" alt="image" src="https://github.com/user-attachments/assets/efd1cb12-0181-48ba-a861-ddce7be90f2c" />
<img width="1220" height="866" alt="image" src="https://github.com/user-attachments/assets/32ddfaa9-e072-4670-ad46-cb79ecbc4fca" />

This repo includes a Streamlit app (`app.py`) plus supporting configuration for Streamlit and devcontainers. 

---

## What this project is for

- Quickly generate questions (e.g., for facilitation, reflection, checks-for-understanding, or group discussion)
- Run locally as a simple web app (Streamlit)
- Keep the setup lightweight so it’s easy to use in workshops/classes

> If you’re using OpenAI/LLM APIs inside `app.py`, treat any learner-provided content as potentially sensitive and follow your org/school data handling rules.

---

## Repository contents

- `app.py` — main Streamlit application 
- `requirements.txt` — Python dependencies :  
- `.streamlit/` — Streamlit configuration (and typically where `secrets.toml` lives locally)
- `.devcontainer/` — VS Code devcontainer config (optional, for a consistent dev environment)
- `images/` — screenshots / assets 

---

## Quick start (local)

### 1) Install

```bash
git clone https://github.com/Leoendithas/qnsgen.git
cd qnsgen

python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```
### 2) Configure API keys (if required)

If `app.py` uses Streamlit secrets, create:

* `.streamlit/secrets.toml`

Example:

```toml
[api_keys]
openai = "YOUR_OPENAI_API_KEY"
```

> Don’t commit `secrets.toml`. Add `.streamlit/secrets.toml` to `.gitignore`.

### 3) Run the app

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints in your terminal.

---

## Using the devcontainer (optional)

If you use VS Code:

1. Install the **Dev Containers** extension
2. Open the repo folder in VS Code
3. Choose **Reopen in Container**

This uses the repo’s `.devcontainer/` config.

---

## Customization

Common places to customize (depending on how `app.py` is written):

* Default question style / difficulty
* Number of questions generated
* Output formatting (copy-friendly, worksheet-friendly, etc.)
* Any rubric or bootcamp-aligned criteria

---

## Troubleshooting

* **`streamlit: command not found`**
  Install it (if it isn’t already included in `requirements.txt`):
  `pip install streamlit`

* **Secrets/key errors**
  Ensure `.streamlit/secrets.toml` exists and matches what `app.py` expects.

* **Module import errors**
  Double-check your venv is activated and rerun: `pip install -r requirements.txt`

---

## License

Licensed under the **Apache License 2.0**. See the `LICENSE` file for details.


