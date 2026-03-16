from logic_utils import check_guess, parse_guess, update_score

# Regression: hint direction was swapped — "Too High" said "Go HIGHER!" and vice versa
def test_too_high_hint_direction():
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert "LOWER" in message

def test_too_low_hint_direction():
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert "HIGHER" in message

# Regression: secret was cast to str on even attempts, causing lexicographic comparison
# e.g. check_guess(9, "50") returned "Too High" because "9" > "50" lexicographically
def test_check_guess_string_secret():
    result, _ = check_guess(9, "50")
    assert result == "Too Low"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


# --- Edge case tests: parse_guess ---

def test_parse_guess_negative():
    # Negative numbers pass validation — no range check in parse_guess
    ok, value, _ = parse_guess("-5")
    assert ok is True
    assert value == -5

def test_parse_guess_decimal_truncates():
    # Decimals are silently truncated — "3.7" becomes 3
    ok, value, _ = parse_guess("3.7")
    assert ok is True
    assert value == 3

def test_parse_guess_scientific_notation():
    # "1e10" has no "." so int("1e10") raises ValueError — treated as non-numeric
    ok, _, _ = parse_guess("1e10")
    assert ok is False

def test_parse_guess_very_large_number():
    # Python ints are arbitrary precision — large numbers parse fine
    ok, value, _ = parse_guess("999999999999")
    assert ok is True
    assert value == 999999999999


# --- Edge case tests: check_guess ---

def test_check_guess_negative_guess():
    # Negative guess is always too low
    result, _ = check_guess(-1, 50)
    assert result == "Too Low"

def test_check_guess_very_large_guess():
    # Very large guess is always too high
    result, _ = check_guess(999999, 50)
    assert result == "Too High"

def test_check_guess_invalid_input():
    # Non-convertible input returns Error
    result, _ = check_guess("abc", 50)
    assert result == "Error"


# --- Edge case tests: update_score ---

def test_update_score_win_minimum():
    # Win on a very late attempt still awards at least 10 points
    score = update_score(0, "Win", 20)
    assert score == 10

def test_update_score_unknown_outcome():
    # Unknown outcome leaves score unchanged
    score = update_score(100, "Unknown", 1)
    assert score == 100

def test_update_score_can_go_negative():
    # Repeated wrong guesses can drive score below zero
    score = update_score(0, "Too Low", 1)
    assert score == -5

