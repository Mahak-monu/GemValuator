import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Here's a **detailed explanation** of your logger file in the context of your **Gem Evaluator project**:

# ---

# ### 🔶 **Code Overview**

# This script sets up **automatic logging** for your project. Logging helps track the behavior and execution of the program — especially useful for debugging, tracking errors, or understanding flow.

# ---

# ### 🔹 Line-by-Line Explanation:

# #### ✅ `import logging`

# * Imports Python’s built-in `logging` module.
# * This module allows you to record events (info, warnings, errors, etc.).

# ---

# #### ✅ `import os`

# * Imports the `os` module to interact with the file system (like paths and directories).

# ---

# #### ✅ `from datetime import datetime`

# * Used to get the current date and time. Helpful to create **timestamped log files**.

# ---

# #### ✅ `LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"`

# * Creates a unique log file name using the **current date and time**.

#   * Example file name: `07_18_2025_16_45_22.log`
#   * This ensures each run has a separate log file and prevents overwriting.

# ---

# #### ✅ `logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)`

# * Builds the path where the log file will be saved:

#   * `os.getcwd()` gives the **current working directory**.
#   * Then, `"logs"` is a folder inside it.
#   * And inside it, a subfolder named after the log file name (this part is unusual, explained below).

#   ❗ **Important Note:** Here, you're creating a **folder named like the log file**, which may not be intended. Usually, we want:

#   ```python
#   logs_path = os.path.join(os.getcwd(), "logs")
#   ```

#   and then:

#   ```python
#   LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
#   ```

# ---

# #### ✅ `os.makedirs(logs_path, exist_ok=True)`

# * Creates the directory (and parent directories) if it doesn't exist.
# * `exist_ok=True` prevents an error if the directory already exists.

# ---

# #### ✅ `LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)`

# * This creates the **full path to the log file** inside the logs directory.

# ⚠️ But again, due to earlier mistake, your log path becomes something like:

# ```
# project_folder/logs/07_18_2025_16_45_22.log/07_18_2025_16_45_22.log
# ```

# which is **wrong**, because you're treating a file as a folder.

# ---

# #### ✅ `logging.basicConfig(...)`

# This sets up how logging will work for your whole project.

# **Parameters used:**

# * `filename=LOG_FILE_PATH`
#   ➤ Tells logging where to write the logs (path to the `.log` file).

# * `format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"`
#   ➤ Sets the format of each log message:

#   * `%(asctime)s` → Time of log
#   * `%(lineno)d` → Line number where the log was triggered
#   * `%(name)s` → Name of the logger
#   * `%(levelname)s` → Log level (INFO, WARNING, ERROR)
#   * `%(message)s` → The actual log message

# * `level=logging.INFO`
#   ➤ Only logs **INFO level and above** (INFO, WARNING, ERROR, CRITICAL)

# ---

# ### ✅ Suggested Fix for Directory Structure

# To **correct the structure**, update:

# ```python
# logs_path = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_path, exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# ```

# ---

# ### ✅ Example Log Entry

# ```log
# [ 2025-07-18 16:45:22,123 ] 45 root - INFO - Gem data loaded successfully
# ```

# ---

# ### ✅ Usage in Your Code

# Whenever you want to log something in your project:

# ```python
# import logging

# logging.info("Gem data loaded successfully")
# logging.warning("Invalid price format")
# logging.error("Failed to connect to API")
# ```

# These logs will now be saved with full detail in your `.log` file for debugging and review.

# ---

# If you want, I can also help you write a utility logger module (`logger.py`) to import easily in other files. Let me know!
