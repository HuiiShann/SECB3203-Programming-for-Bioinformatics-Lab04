# AI USE LOG

- Course: SECB3203
- Assessment: Lab 4
- Student name: Tan Hui Shan
- Matric no: A24CS0197
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 6 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 6 November 2026 3:10PM
- Tool: Google (2026). Gemini. Retrieved 6 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "What is the different of sort() and sorted()"
- Output: Explained that `list.sort()` modifies the original list in-place and returns `None`, while `sorted(list)` leaves the original list untouched and returns a brand new sorted list.
- Verified by: read the docs and ran pytest for `sorted_copy`.
- My change: Chose `sorted()` to ensure the original list was not mutated.
- Used in: `src/panel.py` (`sorted_copy`)

## Entry 2

- Date: 6 November 2026 3:30PM
- Tool: Google (2026). Gemini. Retrieved 6 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "Explain sorted_copy(items) for me, what is the items?"
- Output: Clarified that `items` is just a variable name representing whatever list is passed into the function as an argument when it is called.
- Verified by: read the docs.
- My change: Used the explanation to understand function arguments better; no direct code changes needed.
- Used in: `src/panel.py` (`sorted_copy`)

## Entry 3

- Date: 6 November 2026 3:45PM
- Tool: Google (2026). Gemini. Retrieved 6 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "Explain this in detail: def helper(v: Variant) -> tuple: return (_chrom_key(v.chrom), v.pos) return sorted(variants, key=helper)"
- Output: Detailed how `sorted()` uses the `helper` function to extract the chromosome and position using dot notation (`v.chrom`), sorting variants first by chromosome order, then by position.
- Verified by: ran python -m pytest to test the sorting behavior.
- My change: Retained the NamedTuple dot notation instead of switching to dictionary bracket notation.
- Used in: `src/panel.py` (`sort_variants`)

## Entry 4

- Date: 6 November 2026 3:50PM
- Tool: Google (2026). Gemini. Retrieved 6 November 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "How to build 64-codon dictionary programmatically?"
- Output: Suggested using `itertools.product('ATCG', repeat=3)` to generate all possible 3-letter combinations instead of typing them out manually.
- Verified by: ran python -m pytest.
- My change: Used the concept to understand codon generation, but stuck to the provided `CODON_TABLE` logic for the assignment.
- Used in: Not used / conceptually applied to `src/lookup.py`

## Entry 5

- Date: 6 November 2026 4:10PM
- Tool: Google (2026). Gemini. Retrieved 6 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "Can I use count() to replace Counter?"
- Output: Explained that `.count()` only counts one specific string at a time, whereas `collections.Counter` efficiently tallies all unique k-mers in a sequence simultaneously.
- Verified by: read the docs and ran pytest.
- My change: Imported and used `Counter` from the `collections` module for efficiency.
- Used in: `src/lookup.py` (`kmer_counts`)

## Entry 6

- Date: 6 November 2026 4:30PM
- Tool: Google (2026). Gemini. Retrieved 6 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "Explain [i:i+k] for i in range(len(seq)-k+1)"
- Output: Described how this list comprehension uses a sliding window (looping with `range`) and string slicing (`[i:i+k]`) to extract all overlapping substrings of length `k`.
- Verified by: ran pytest with edge cases (empty strings, large k).
- My change: Implemented this exact slicing logic to feed data into `Counter`.
- Used in: `src/lookup.py` (`kmer_counts`)