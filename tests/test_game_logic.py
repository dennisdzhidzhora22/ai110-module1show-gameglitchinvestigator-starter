from logic_utils import check_guess

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
