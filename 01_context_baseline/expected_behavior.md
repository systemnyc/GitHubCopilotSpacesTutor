# Expected Behavior: Weather Report Generator

## Input/Output Examples

### Example 1: Valid City (New York)

**Command:**
```bash
python main.py "New York"
```

**Expected Output (stdout):**
```
Weather Report for New York
================================
Temperature: 72°F
Condition: Partly Cloudy
Humidity: 65%
Wind Speed: 8 mph
```

**Exit Code:** `0` (success)

---

### Example 2: Valid City (San Francisco)

**Command:**
```bash
python main.py "San Francisco"
```

**Expected Output (stdout):**
```
Weather Report for San Francisco
================================
Temperature: 68°F
Condition: Foggy
Humidity: 78%
Wind Speed: 12 mph
```

**Exit Code:** `0` (success)

---

### Example 3: Invalid City (Not in Data)

**Command:**
```bash
python main.py "Denver"
```

**Expected Output (stderr):**
```
Error: City 'Denver' not found in weather data.
Available cities: New York, San Francisco, Austin, Seattle, Miami
```

**Exit Code:** `1` (error)

---

### Example 4: Missing Argument

**Command:**
```bash
python main.py
```

**Expected Output (stdout):**
```
Usage: python main.py "City Name"
Example: python main.py "New York"
```

**Exit Code:** `1` (error)

---

### Example 5: Case Sensitivity (Wrong Case)

**Command:**
```bash
python main.py "new york"
```

**Expected Output (stderr):**
```
Error: City 'new york' not found in weather data.
Available cities: New York, San Francisco, Austin, Seattle, Miami
```

**Exit Code:** `1` (error)

**Note:** Lookup is case-sensitive. The city must match exactly as it appears in `sample_weather.json`.

---

## Error Cases

### Missing `sample_weather.json`

**If the file does not exist:**

**Expected Output (stderr):**
```
Error loading weather data: Weather data file not found: /path/to/sample_weather.json
```

**Exit Code:** `1` (error)

---

### Malformed JSON

**If the JSON file contains invalid JSON:**

**Expected Output (stderr):**
```
Error loading weather data: [JSON decode error details]
```

**Exit Code:** `1` (error)

---

## Output Format Specification

The weather report follows this exact format:

```
Weather Report for {CITY_NAME}
================================
Temperature: {TEMP}°F
Condition: {CONDITION}
Humidity: {HUMIDITY}%
Wind Speed: {WIND_SPEED} mph
```

**Format Details:**
- Line 1: "Weather Report for " + city name (as provided in JSON)
- Line 2: Exactly 32 equals signs (=)
- Line 3: "Temperature: " + temperature value + "°F"
- Line 4: "Condition: " + condition string
- Line 5: "Humidity: " + humidity value + "%"
- Line 6: "Wind Speed: " + wind speed value + " mph"
- Line 7: Blank line (newline at end)

---

## Test Data (sample_weather.json)

The application uses this sample data:

| City | Temperature | Condition | Humidity | Wind Speed |
|------|-------------|-----------|----------|------------|
| New York | 72 | Partly Cloudy | 65 | 8 |
| San Francisco | 68 | Foggy | 78 | 12 |
| Austin | 88 | Sunny | 45 | 5 |
| Seattle | 65 | Rainy | 85 | 15 |
| Miami | 82 | Clear | 70 | 10 |

All cities MUST be queryable with exact-case matching.
