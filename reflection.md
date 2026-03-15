# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

There weren't any visible bugs in the game when I started it, but then I ran out of guesses, and the actual number was NOT being hinted at by the hints. I was narrowing down the secret number, and passed a point where the hint changed to the opposite direction, which gave a small range of possible numbers. But when the real secret number was revealed, it was nowhere near the possible range.

I also noticed that the "New Game" button is probably broken, as nothing happens after I enter another guess and submit it. No hint is given. 

The number of guesses also seems to be broken after starting a new game, since it started at 7 at the very beginning, but then started at 8 once I pressed New Game. For consistency, the number should start at 7, not 8.

Except block that handles string answers is bugged - lexicographical string comparison doesn't behave as desired. If the guess is always an int, the block is unreachable, so should probably not be kept.

Update on the wrong hints - the direction of the hints is also swapped.

The range of numbers and number of guesses are not consistent throughout difficulties. With increasing difficulty, the range of numbers should increase, and number of guesses should decrease. Also, the range is hardcoded in displayed info.

Switching difficulties does not reset the number of attempts left and other state info, like the range and score.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
