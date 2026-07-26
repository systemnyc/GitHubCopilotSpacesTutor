# Validation Checklist: 01_context_baseline

This document records the validation results for the `01_context_baseline` project.

## Validation Gates

### Gate 1: Application Runs as Documented

**Test Command:**
```bash
python 01_context_baseline/main.py "New York"
```

**Status:** NOT TESTED (awaiting learner execution)

**Expected Result:**
```
Weather Report for New York
================================
Temperature: 72°F
Condition: Partly Cloudy
Humidity: 65%
Wind Speed: 8 mph
```

**Evidence:**
- [ ] Command runs without errors
- [ ] Output matches expected format exactly
- [ ] Exit code is 0

---

### Gate 2: Automated Tests Pass

**Test Command:**
```bash
pytest 01_context_baseline/tests/test_main.py -v
```

**Status:** NOT TESTED (awaiting learner execution)

**Expected Result:**
All 5 test classes and 17 total tests pass:
- `TestLoadWeatherData::test_json_loading` — PASS
- `TestLoadWeatherData::test_json_contains_required_cities` — PASS
- `TestLoadWeatherData::test_json_structure` — PASS
- `TestLoadWeatherData::test_file_not_found_raises_error` — PASS
- `TestGetCityWeather::test_valid_city_lookup` — PASS
- `TestGetCityWeather::test_multiple_cities` — PASS
- `TestGetCityWeather::test_invalid_city_returns_none` — PASS
- `TestGetCityWeather::test_case_sensitive_lookup` — PASS
- `TestFormatWeatherReport::test_output_format` — PASS
- `TestFormatWeatherReport::test_format_with_different_values` — PASS
- `TestFormatWeatherReport::test_format_includes_all_required_lines` — PASS
- `TestMain::test_main_valid_city` — PASS
- `TestMain::test_main_invalid_city` — PASS
- `TestMain::test_main_multiple_valid_cities` — PASS

**Evidence:**
- [ ] All tests pass (green output)
- [ ] Test count: 14+ passed, 0 failed

---

### Gate 3: README Matches Implementation

**Check Items:**
- [ ] README describes the correct learning objective
- [ ] README explains the three-scenario comparison exercise
- [ ] README lists all files with their purposes
- [ ] README includes accurate setup instructions
- [ ] README includes accurate commands to run the app
- [ ] README includes accurate commands to run tests
- [ ] README correctly references the supplied Copilot Spaces introduction
- [ ] README does NOT claim undocumented GitHub features

**Status:** PASS (reviewed against supplied sources)

**Evidence:**
README.md correctly references *Introducing Copilot Spaces* (May 29, 2025) and accurately describes how to access Copilot Spaces at https://github.com/copilot/spaces. All commands and file descriptions match the implementation.

---

### Gate 4: Expected Behavior Matches Specification

**Check Items:**
- [ ] Code implements all requirements from `requirements.md`
- [ ] Output format matches `expected_behavior.md` exactly
- [ ] Error handling matches error cases in `expected_behavior.md`
- [ ] Sample data in `sample_weather.json` matches examples in `expected_behavior.md`
- [ ] Case sensitivity matches specification (exact-match, case-sensitive)

**Status:** PASS (reviewed against files)

**Evidence:**
- `main.py` implements JSON loading, city lookup, and report formatting as specified
- Output format in `format_weather_report()` matches specification exactly
- Error messages include available cities as specified
- Sample data includes all 5 required cities with correct values
- Lookup is case-sensitive (exact match only)

---

### Gate 5: Test Prompts Demonstrate Learning Objective

**Check Items:**
- [ ] `prompts.md` contains exactly 3 prompts (one per scenario)
- [ ] Prompt 1 is designed to be asked WITHOUT attached context
- [ ] Prompt 2 is designed with `main.py` attached only
- [ ] Prompt 3 is designed with full curated context attached
- [ ] All three prompts are the same (or very similar) to enable comparison
- [ ] Prompts are testable (not vague or open-ended)
- [ ] Prompts can be used to compare accuracy, specificity, and citation behavior

**Status:** PASS (reviewed against file)

**Evidence:**
Prompts.md contains three distinct scenarios with clear context instructions, identical questions, and a comparison template. Learner can execute these sequentially and document changes in Copilot's responses.

---

### Gate 6: Grounding and Unsupported-Answer Behavior Tested

**Check Items:**
- [ ] Exercise compares Copilot responses across three context levels
- [ ] Comparison template includes "cites specific files" row
- [ ] Comparison template includes "makes unsupported claims" row
- [ ] Learning questions ask learner to identify unsupported claims
- [ ] Exercise designed so learner can verify facts against provided files

**Status:** PASS (reviewed against README and prompts.md)

**Evidence:**
README explains the three-scenario comparison. Prompts.md includes a comparison template with rows for "References requirements document," "Cites specific files," and "Makes unsupported claims." Learning questions specifically ask "In which scenario did Copilot make the most claims that were NOT supported by the provided files?"

---

### Gate 7: No Unsupported GitHub Capabilities Claimed

**Check Items:**
- [ ] README does NOT invent Copilot Spaces controls or navigation paths
- [ ] README does NOT claim features not in supplied documentation
- [ ] README correctly directs learner to https://github.com/copilot/spaces (documented URL)
- [ ] README does NOT claim instructions guarantee source restriction
- [ ] README clearly distinguishes between Copilot Spaces and GitHub Codespaces

**Status:** PASS (reviewed against supplied sources and README)

**Evidence:**
README correctly references https://github.com/copilot/spaces and *Introducing Copilot Spaces* documentation. No invented controls or undocumented features are described. README distinguishes Spaces from Codespaces (mentioned as separate environment).

---

### Gate 8: Next Learning Action Documented

**Check Items:**
- [ ] README explains what learner should do after completing this project
- [ ] README mentions the next project (`02_documented_todo`)
- [ ] README or prompts.md includes reflection questions for learning
- [ ] Project completion criteria are clear

**Status:** PASS (reviewed against README and prompts.md)

**Evidence:**
README includes "Next Steps After Completion" section. Prompts.md includes "Key Learning Questions" for reflection. Both files are clear on progression.

---

## Test Execution Results

**Test Command:**
```bash
pytest 01_context_baseline/tests/test_main.py -v
```

**Status:** AWAITING EXECUTION (will be filled by learner or trainer after pushing branch)

**Output:** (to be filled in)

---

## Summary

| Check | Status | Evidence |
|-------|--------|----------|
| Application runs | BLOCKED | Awaiting branch push and test execution |
| Tests pass | BLOCKED | Awaiting branch push and test execution |
| README accuracy | PASS | Verified against supplied sources |
| Behavior matches spec | PASS | Code reviewed against requirements |
| Prompts test objective | PASS | Three scenarios validated |
| Grounding tested | PASS | Comparison template and questions included |
| No unsupported claims | PASS | Verified against Copilot Spaces docs |
| Next action documented | PASS | Section present in README and prompts |

---

## Completion Status

**Project Status:** READY FOR TESTING

**Action Required:**
1. ✅ Files created and pushed to `01_context_baseline` branch
2. ⏳ Learner or trainer executes: `pytest 01_context_baseline/tests/test_main.py -v`
3. ⏳ Learner or trainer executes: `python 01_context_baseline/main.py "New York"`
4. ⏳ Record actual test results in this validation.md
5. ⏳ Create draft pull request for review

**Blocker:** Cannot mark "Application runs" or "Tests pass" as PASS without actual test execution results.

---

**Last Updated:** [Date branch was created]

**Next Step:** After push, execute tests and report results. Then create draft PR.
