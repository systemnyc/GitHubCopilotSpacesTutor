# Test Prompts for Copilot Spaces Exercise

Use these three prompts to test how Copilot's responses improve as you add context to the Space.

---

## Prompt 1 (Scenario 1: No Context)

### Context to attach:
None — ask this question with a blank Space.

### Question to ask Copilot:

```
How would you design a weather report generator application? 
What are the key components, design decisions, and best practices? 
How should it handle invalid city names?
```

### What to observe:
- Copilot will give generic, best-practice advice
- It will NOT know your specific output format
- It will NOT reference the actual code or requirements
- It may suggest features you don't need (like API calls, caching, etc.)
- It may not cite any sources specific to your project

### Record your response:
(You will fill this in after asking the question)

---

## Prompt 2 (Scenario 2: Single-File Context)

### Context to attach:
- `01_context_baseline/main.py`

### Question to ask Copilot:

```
Looking at the weather report generator code, how does it handle 
error cases? What are its strengths and any potential improvements?
```

### What to observe:
- Copilot can now see the actual implementation
- It will reference specific functions and logic from `main.py`
- It will understand the output format (because it's in the code)
- However, it will NOT know the broader context:
  - Why certain design decisions were made
  - What the requirements document says
  - What tests validate this behavior
  - What edge cases are documented
- It may still suggest improvements that contradict unstated requirements

### Record your response:
(You will fill this in after asking the question)

---

## Prompt 3 (Scenario 3: Curated Multi-File Context)

### Context to attach:
- `01_context_baseline/main.py`
- `01_context_baseline/sample_weather.json`
- `01_context_baseline/requirements.md`
- `01_context_baseline/expected_behavior.md`

### Question to ask Copilot:

```
Based on the weather report generator project files, implementation, 
and requirements, what are the key design strengths? Does the 
implementation meet all stated requirements? What testing would 
validate the expected behavior?
```

### What to observe:
- Copilot now has complete, curated context
- It will reference specific files and requirements
- It will understand the full scope and intent of the project
- It will cite the requirements and expected behavior docs
- It will be able to validate that implementation matches spec
- It should make claims that are grounded in the actual project files
- It may identify areas where implementation could be improved with FULL context

### Record your response:
(You will fill this in after asking the question)

---

## Comparison Template

After collecting all three responses, fill in this table:

| Aspect | Scenario 1 (No Context) | Scenario 2 (main.py only) | Scenario 3 (Curated Context) |
|--------|------------------------|-------------------------|------------------------------|
| **Mentions specific output format?** | Yes / No | Yes / No | Yes / No |
| **References requirements document?** | Yes / No | Yes / No | Yes / No |
| **Cites specific files?** | Yes / No | Yes / No | Yes / No |
| **Suggests irrelevant features (e.g., API calls, database)?** | Yes / No | Yes / No | Yes / No |
| **Makes unsupported claims?** | Yes / No | Yes / No | Yes / No |
| **Most useful for understanding the project?** | Yes / No | Yes / No | Yes / No |

---

## Key Learning Questions

After completing the exercise, reflect on these questions:

1. **Context Impact:** How dramatically did Copilot's responses change as you added context? Describe the progression.

2. **Specificity:** Which context elements (code, requirements, behavior spec, sample data) had the most impact on accuracy?

3. **Unsupported Claims:** In which scenario did Copilot make the most claims that were NOT supported by the provided files? Why?

4. **For Teamwork:** If you were sharing this Space with a teammate, which files would you prioritize adding? Why?

5. **Source Grounding:** Did Copilot identify which file it was referencing when answering? How would you expect that to work in a shared Space?

---

## Expected Learning Outcome

After this exercise, you should understand:

✅ Context dramatically improves Copilot's accuracy and relevance

✅ Curated, organized context (not just "everything") makes the biggest difference

✅ Copilot's responses should be specific to your project, not generic

✅ Well-written requirements and specs are valuable context sources

✅ Copilot becomes a "subject matter expert" when given the right context
