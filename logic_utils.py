# FIX: refactored by moving logic-related functions into logic_utils.py. used claude code to copy each function over with fixes made previously

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""

    # FIX: range sizes were not in logical order, hard range (1-50) was smaller than normal (1-100). refactored using claude code
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """

    # FIX: incorrect error handling, converted secret and guess to strings instead of ints, causing incorrect lexicographical comparison. found by claude code, fixed by me.
    try:
        guess = int(guess)
        secret = int(secret)
    except (ValueError, TypeError):
        return "Error", "Invalid guess or secret value."

    if guess == secret:
        return "Win", "🎉 Correct!"
    
    # FIX: hint directions were swapped, Go HIGHER showed when guess was too high and vice versa. reported by me, found and fixed by claude code.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        # FIX: rewarded +5 points on even-numbered attempts instead of always subtracting 5. found and fixed by claude code.
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
