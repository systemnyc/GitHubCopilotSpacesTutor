# 01_context_baseline: Learning Copilot Spaces Through Context Grounding

## Learning Objective

Understand how **curated context** in a Copilot Space improves the accuracy, relevance, and grounding of Copilot's responses. You will compare Copilot's answers in three scenarios:

1. **No project context** — Copilot responds from general knowledge
2. **Single-file context** — Copilot sees only `main.py`
3. **Curated multi-file context** — Copilot has access to requirements, behavior specs, sample data, and documentation

## Copilot Spaces Capability Being Practiced

**Context Grounding** — As explained in *Introducing Copilot Spaces*:

> "Spaces let you ground Copilot's knowledge in a curated set of specific code, documents, notes, and more. With this extra context, Copilot becomes an expert in the task at hand—from understanding how a system works, to why it was built in a particular way, or even best practice examples."

This project demonstrates that principle by showing measurable differences in Copilot's responses as context is added.

## What This Project Does

This is a **simple weather report generator** that reads local JSON data and formats a report. It has no external API calls—everything is grounded in files you can inspect, modify, and understand.

### Application Behavior

- **Input:** A city name (command-line argument)
- **Processing:** Loads `sample_weather.json`, finds the matching city
- **Output:** A formatted weather report (or error if city not found)
- **Example Output:**
  ```
  Weather Report for New York
  ================================
  Temperature: 72°F
  Condition: Partly Cloudy
  Humidity: 65%
  Wind Speed: 8 mph
  ```

## Prerequisites

- Python 3.9 or later
- `pytest` (for running tests)
- A text editor or IDE
- GitHub account with access to Copilot Chat at github.com

## How to Set Up

### 1. Install Dependencies

```bash
pip install pytest
```

### 2. Run the Application

```bash
python 01_context_baseline/main.py "New York"
```

Expected output:
```
Weather Report for New York
================================
Temperature: 72°F
Condition: Partly Cloudy
Humidity: 65%
Wind Speed: 8 mph
```

### 3. Run the Automated Tests

```bash
pytest 01_context_baseline/tests/test_main.py -v
```

All tests should pass.

## Files in This Project

| File | Purpose |
|------|----------|
| `main.py` | Weather report generator |
| `sample_weather.json` | Mock weather data for cities |
| `requirements.md` | Functional specification |
| `expected_behavior.md` | Input/output examples and error cases |
| `prompts.md` | Three Copilot Chat prompts to test |
| `tests/test_main.py` | Automated unit tests |
| `validation.md` | Validation checklist (completed after testing) |

## The Copilot Spaces Exercise

You will perform this exercise **in a Copilot Space** on github.com. The goal is to observe how Copilot's responses improve as you add project context.

### Setup: Create a Copilot Space

1. Go to https://github.com/copilot/spaces
2. Click **Create a new space**
3. Name it: `01_context_baseline_demo`
4. Description: `Testing how context improves Copilot's weather app responses`
5. Leave it as a **Personal** space for now
6. Click **Create**

### Scenario 1: No Context (Baseline)

**What to do:**

1. In Copilot Chat (inside the Space), ask the **first prompt** from `prompts.md` (see below)
2. Record Copilot's response
3. Note: Did it mention the specific output format? Did it cite the requirements?

**Expected observation:** Copilot will give a generic response based on general knowledge, without specific details about your project's requirements or behavior.

### Scenario 2: Single-File Context

**What to do:**

1. In the Space, add the `01_context_baseline/main.py` file as a source
   - Click the context menu (+ button) in the Space
   - Select **Add file or code**
   - Choose `main.py`
2. Ask the **same prompt** again
3. Record the response

**Expected observation:** Copilot can now see the implementation details and will give more specific answers, but it doesn't know the *intent* or broader context of the project.

### Scenario 3: Curated Multi-File Context

**What to do:**

1. Add these files to the Space:
   - `01_context_baseline/requirements.md`
   - `01_context_baseline/expected_behavior.md`
   - `01_context_baseline/sample_weather.json`
2. Ask the **same prompt** for a third time
3. Record the response

**Expected observation:** Copilot now has complete, curated context and can provide the most accurate, grounded, and well-cited response. It should reference specific files and requirements.

### Comparison Activity

After collecting all three responses, compare them:

| Question | Scenario 1 (No Context) | Scenario 2 (main.py only) | Scenario 3 (Curated Context) |
|----------|-------------------------|--------------------------|------------------------------|
| **Accuracy** | Generic/inaccurate | Partial | Complete and accurate |
| **Specificity** | General advice | Code-based | Grounded in requirements |
| **Citations** | Few or none | References code | References files and specs |
| **Unsupported claims** | Likely | Some | Minimal |

### Questions to Ask Yourself

1. How did the response change as you added context?
2. Which scenario produced the most useful answer?
3. Did Copilot cite the files it was using? Which files?
4. In Scenario 3, did Copilot make any claims that were NOT supported by the provided files?
5. What context would you add to this Space if you were sharing it with a teammate?

## Test Prompts (from `prompts.md`)

See the `prompts.md` file for the three exact prompts to use in each scenario.

## Running Tests

Before you perform the Copilot Spaces exercise, verify the application works:

```bash
pytest 01_context_baseline/tests/test_main.py -v
```

Example output:
```
================================ test session starts ==================================
platform linux -- Python 3.9.0, plugindir=
'.../pytest'
collected 5 items

01_context_baseline/tests/test_main.py::test_valid_city PASSED                 [ 20%]
01_context_baseline/tests/test_main.py::test_invalid_city PASSED               [ 40%]
01_context_baseline/tests/test_main.py::test_output_format PASSED              [ 60%]
01_context_baseline/tests/test_main.py::test_multiple_cities PASSED            [ 80%]
01_context_baseline/tests/test_main.py::test_json_loading PASSED              [100%]

============================== 5 passed in 0.05s ===============================
```

## Next Steps After Completion

1. ✅ Run the application and tests (you are here)
2. ✅ Create the Copilot Space and add this project
3. ✅ Perform the three-scenario comparison
4. ✅ Document your observations
5. ➡️ **Next Project:** Proceed to `02_documented_todo` to learn how requirements and documentation further improve Copilot's responses

## Troubleshooting

### "City not found" error

Verify the city name matches exactly (case-sensitive) in `sample_weather.json`. The available cities are listed in that file.

### Tests fail with "ModuleNotFoundError"

Run `pip install pytest` again and ensure Python can find the module:

```bash
python -m pytest 01_context_baseline/tests/test_main.py -v
```

### Copilot Chat not responding in the Space

Confirm:
- You have a valid Copilot subscription (Pro, Pro+, Business, or Enterprise)
- You are on https://github.com/copilot/spaces (not Codespaces)
- The Space was created successfully

---

**Source:** *Introducing Copilot Spaces* (May 29, 2025)
