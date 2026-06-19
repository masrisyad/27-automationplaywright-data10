# 🧪 Data-Driven Form Automation (Playwright Python)

A lightweight UI automation script built with **Python** and **Playwright**. This project demonstrates the core concept of **Data-Driven Testing (DDT)** by automatically iterating through a dataset and submitting multiple records into a web form in a single browser session.

---

## 📌 Overview

This script acts as a Proof of Concept (PoC) for automating repetitive data entry tasks. It targets the [DemoQA Text Box](https://demoqa.com/text-box) practice page.

**Workflow Summary:**

1. Launches a Chromium browser in headed mode (UI visible).
2. Navigates to the DemoQA target URL.
3. Loops through a predefined set of `mock_data` (dictionaries containing names and emails).
4. Injects the data into the respective input fields and clicks the submit button for each record.
5. Prints a success log to the terminal.
6. Closes the browser upon completion.

---

## 🛠️ Prerequisites

Before executing the script, ensure your system meets the following requirements:

* **Python:** Version 3.8 or higher.
* **pip:** Python's package installer.

---

## ⚙️ Installation & Setup

Follow these steps to set up your local execution environment cleanly:

**1. Clone or Create the Script**
Save the provided Python code into a file named `main.py` in your project folder.

**2. Establish a Virtual Environment (Highly Recommended)**
Using a virtual environment isolates your dependencies and prevents conflicts.

```bash
# Create the virtual environment
python -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows (Command Prompt):
venv\Scripts\activate

```

**3. Install Playwright**
Install the Playwright library via pip:

```bash
pip install playwright

```

**4. Install Browser Binaries**
Playwright requires its own browser binaries to interact with web pages. Install the Chromium engine by running:

```bash
playwright install chromium

```

---

## 🚀 Execution Guide

Run the script directly from your terminal using Python:

```bash
python main.py

```

### What to Expect:

Because the script uses `headless=False`, you will visually see the Google Chrome browser open, navigate to the site, rapidly fill in the data for "Budi" and "Siti", submit the forms, and close.

Check your terminal for the execution logs:

```text
Data Budi terinput.
Data Siti terinput.

```

---

## 🏗️ Best Practice

While this script is an excellent starting point for learning Playwright and DDT, scaling it into a robust test automation framework will require the following architectural improvements:

1. **Implement Assertions:** Currently, the script blindly fills and clicks without verifying if the submission was actually successful. Implement `expect(locator)` to assert that the UI reflects the submitted data after clicking submit.
2. **Externalize Test Data:** Hardcoding `mock_data` inside the script makes maintenance difficult. Move the test data into an external file format like **JSON**, **CSV**, or **YAML**, and write a helper function to read it.
3. **Use Pytest:** Wrap this execution inside `pytest` (using the `pytest-playwright` plugin). This will provide automatic parameterized testing, robust HTML reporting, and better exception handling.
4. **Headless Execution:** When migrating this script to a CI/CD pipeline (e.g., GitHub Actions, GitLab CI), change the browser launch argument to `headless=True` to run the tests securely in the background without needing a display server.
