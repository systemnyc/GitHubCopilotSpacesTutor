#!/usr/bin/env python3
"""
Automated Tests for Weather Report Generator

Tests verify:
- Valid city lookups
- Invalid city error handling
- Output format correctness
- JSON loading
- Multiple city support

Run tests with:
    pytest tests/test_main.py -v
"""

import pytest
import json
import sys
from pathlib import Path

# Add parent directory to path so we can import main
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import (
    load_weather_data,
    get_city_weather,
    format_weather_report,
    main,
)


class TestLoadWeatherData:
    """Tests for load_weather_data function."""

    def test_json_loading(self):
        """Test that JSON file loads successfully."""
        data = load_weather_data()
        assert isinstance(data, dict)
        assert len(data) > 0

    def test_json_contains_required_cities(self):
        """Test that JSON contains at least the 5 expected cities."""
        data = load_weather_data()
        expected_cities = ["New York", "San Francisco", "Austin", "Seattle", "Miami"]
        for city in expected_cities:
            assert city in data, f"Expected city '{city}' not found in data"

    def test_json_structure(self):
        """Test that each city has required weather fields."""
        data = load_weather_data()
        required_fields = ["temperature", "condition", "humidity", "wind_speed"]
        
        for city, weather in data.items():
            for field in required_fields:
                assert field in weather, f"City '{city}' missing field '{field}'"

    def test_file_not_found_raises_error(self):
        """Test that FileNotFoundError is raised for missing file."""
        with pytest.raises(FileNotFoundError):
            load_weather_data("nonexistent_file.json")


class TestGetCityWeather:
    """Tests for get_city_weather function."""

    def test_valid_city_lookup(self):
        """Test that valid city returns weather data."""
        data = load_weather_data()
        weather = get_city_weather("New York", data)
        assert weather is not None
        assert weather["temperature"] == 72
        assert weather["condition"] == "Partly Cloudy"

    def test_multiple_cities(self):
        """Test lookups for multiple cities."""
        data = load_weather_data()
        cities_to_test = [
            ("New York", 72),
            ("San Francisco", 68),
            ("Austin", 88),
            ("Seattle", 65),
            ("Miami", 82),
        ]
        
        for city, expected_temp in cities_to_test:
            weather = get_city_weather(city, data)
            assert weather is not None
            assert weather["temperature"] == expected_temp

    def test_invalid_city_returns_none(self):
        """Test that invalid city returns None."""
        data = load_weather_data()
        weather = get_city_weather("Denver", data)
        assert weather is None

    def test_case_sensitive_lookup(self):
        """Test that city lookup is case-sensitive."""
        data = load_weather_data()
        # Correct case should work
        assert get_city_weather("New York", data) is not None
        # Wrong case should not work
        assert get_city_weather("new york", data) is None
        assert get_city_weather("NEW YORK", data) is None


class TestFormatWeatherReport:
    """Tests for format_weather_report function."""

    def test_output_format(self):
        """Test that output matches expected format."""
        weather_info = {
            "temperature": 72,
            "condition": "Partly Cloudy",
            "humidity": 65,
            "wind_speed": 8,
        }
        report = format_weather_report("New York", weather_info)
        
        # Verify key format elements
        assert "Weather Report for New York" in report
        assert "================================" in report
        assert "Temperature: 72°F" in report
        assert "Condition: Partly Cloudy" in report
        assert "Humidity: 65%" in report
        assert "Wind Speed: 8 mph" in report

    def test_format_with_different_values(self):
        """Test format with different weather values."""
        weather_info = {
            "temperature": 88,
            "condition": "Sunny",
            "humidity": 45,
            "wind_speed": 5,
        }
        report = format_weather_report("Austin", weather_info)
        
        assert "Weather Report for Austin" in report
        assert "Temperature: 88°F" in report
        assert "Condition: Sunny" in report
        assert "Humidity: 45%" in report
        assert "Wind Speed: 5 mph" in report

    def test_format_includes_all_required_lines(self):
        """Test that format includes all 6 required lines (plus blank)."""
        weather_info = {
            "temperature": 70,
            "condition": "Clear",
            "humidity": 50,
            "wind_speed": 10,
        }
        report = format_weather_report("Test City", weather_info)
        lines = report.split("\n")
        
        # Should have 7 lines: 6 content + 1 trailing newline
        assert len(lines) == 7
        assert lines[0] == "Weather Report for Test City"
        assert lines[1] == "================================"
        assert lines[2] == "Temperature: 70°F"
        assert lines[3] == "Condition: Clear"
        assert lines[4] == "Humidity: 50%"
        assert lines[5] == "Wind Speed: 10 mph"
        assert lines[6] == ""  # Trailing newline


class TestMain:
    """Integration tests for main function."""

    def test_main_valid_city(self, capsys):
        """Test main function with valid city."""
        exit_code = main("New York")
        captured = capsys.readouterr()
        
        assert exit_code == 0
        assert "Weather Report for New York" in captured.out
        assert "Temperature: 72°F" in captured.out

    def test_main_invalid_city(self, capsys):
        """Test main function with invalid city."""
        exit_code = main("Denver")
        captured = capsys.readouterr()
        
        assert exit_code == 1
        assert "Error" in captured.err
        assert "Denver" in captured.err
        assert "not found" in captured.err

    def test_main_multiple_valid_cities(self, capsys):
        """Test main function with multiple valid cities."""
        for city in ["Austin", "Seattle", "Miami"]:
            exit_code = main(city)
            assert exit_code == 0, f"Failed for city: {city}"
            captured = capsys.readouterr()
            assert city in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
