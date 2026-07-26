# Requirements: Weather Report Generator

## Functional Requirements

### 1. Data Loading
- The application MUST load weather data from a JSON file named `sample_weather.json`
- The JSON file MUST contain at least 5 cities
- Each city entry MUST include: `temperature`, `condition`, `humidity`, and `wind_speed`
- The application MUST handle missing or malformed JSON files gracefully with an error message

### 2. City Lookup
- The application MUST accept a city name as a command-line argument
- The application MUST perform an exact-match lookup (case-sensitive)
- If the city is not found, the application MUST display an error message and list available cities
- If no argument is provided, the application MUST display usage instructions

### 3. Report Generation
- The application MUST format the weather report in the standard format:
  ```
  Weather Report for {City Name}
  ================================
  Temperature: {temp}°F
  Condition: {condition}
  Humidity: {humidity}%
  Wind Speed: {wind_speed} mph
  ```
- The report MUST be printed to standard output (not a file)

### 4. Error Handling
- The application MUST exit with status code 0 on success
- The application MUST exit with status code 1 on any error
- Error messages MUST be printed to stderr, not stdout
- Error messages MUST be clear and actionable

## Non-Functional Requirements

### Code Quality
- Code MUST be documented with docstrings for all functions
- Code MUST follow PEP 8 style guidelines
- Functions MUST have single, clear responsibilities

### Testing
- A test suite MUST verify all core functionality
- Tests MUST validate valid city lookups
- Tests MUST validate invalid city error handling
- Tests MUST validate output format
- Tests MUST validate JSON loading and error handling
- All tests MUST pass

## Acceptance Criteria

- ✅ Application runs without errors for valid city names
- ✅ Application displays the correct formatted report
- ✅ Application handles invalid city names with helpful error messages
- ✅ All automated tests pass
- ✅ Code follows PEP 8 and includes docstrings
- ✅ Application can be run as: `python main.py "City Name"`
