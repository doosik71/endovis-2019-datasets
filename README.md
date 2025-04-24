# EndoVis 2019 Datasets

## 🧪 Step 1: Create and Activate Python Environment

```bash
python -m venv venv
```

### Activate the environment

- **Linux/macOS:**

```bash
source venv/bin/activate
```

- **Windows (CMD):**

```cmd
venv\Scripts\activate
```

- **Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

> 💡 Ensure you're using Python 3.8+ for compatibility.

## 📦 Step 2: Install Dependencies

- Before installing packages, upgrade `pip`:

```bash
pip install --upgrade pip
```

- Then install the required Python libraries:

```bash
pip install -r requirements.txt
```

## 🔑 Step 3: Create a Synapse Account and Access Token

1. Go to [Synapse EndoVis 2019 page](https://www.synapse.org/#!Synapse:syn18779624/wiki/592660).
2. Create a Synapse account if you don’t have one.
3. Navigate to `Your Account` → `Account Setting` → `Personal Access Tokens` → `Manage Personal Access Tokens`.
4. Create a new token with `Read` and `Downlaod` permissions.
5. Save the token securely.

## 🔐 Step 4: Create a `.env` File

In the project root directory, create a file named `.env` with the following content:

```env
SYNAPSE_ACCESS_TOKEN=your_access_token
```

> ⚠️ Make sure **not to share** this file or commit it to version control (`.gitignore` it).

## ⬇️ Step 5: Download the EndoVis 2019 Dataset

- Run the download script:

```bash
python download.py
```

- This script will use your Synapse credentials from the `.env` file to authenticate and download the dataset.

## ℹ️ More Information

- For more details about the dataset and challenge, visit the official Synapse page:
  - <https://www.synapse.org/#!Synapse:syn18779624/wiki/592660>
