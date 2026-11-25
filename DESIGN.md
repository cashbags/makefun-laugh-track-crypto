# Design — Laugh Track: The Crypto Trading Joke Contest

## The entry

> My tax spreadsheet has a tab called 'losses' and a tab called 'losses (emotional)'.

83 characters, 83 bytes, one line, no trailing newline. It is the whole entry:
`main.py` writes exactly this string to `/output/entry.txt`.

## Why this line

The judge brief ranks five criteria in order: on-subject with a setup and a turn;
a real laugh from a surprise payoff; true to trading life; every word earning its
place with the punchline last; repeatable on a second read. The line was picked to
score on all five in that order, not just to be funny in the abstract:

1. **On-subject, setup + turn.** Tax on trades is squarely trading life. The setup
   is a spreadsheet with a `losses` tab; the turn is that there is a second `losses`
   tab, qualified as emotional. The joke cannot be told about anything but trading.
2. **Surprise payoff.** The second tab name reuses the setup's own word — the reader
   expects a different category (`gains`, `fees`, `2025`) and gets the same word
   back with one qualifier. The turn is a single parenthetical, so the surprise
   lands all at once instead of leaking out over a clause.
3. **True to trading life.** Every trader who has done a tax return knows there are
   two ledgers: the numbers the exchange reports and the ones you feel. The detail
   (a spreadsheet tab) is concrete and recognisable, not a generic slogan.
4. **Every word earns its place.** At 83 bytes it is the shortest line in the
   candidate field, and nothing in it is throat-clearing. The punchline —
   `(emotional)` — is literally the last word of the line.
5. **Repeatable.** Short enough to quote verbatim to a friend, and the joke survives
   a second read because the turn is structural (the echo), not a topical reference
   that dates.

## Lanes deliberately avoided

The flooded lanes were banned before drafting: HODL, "buy the dip", "to the moon",
diamond hands, "not financial advice" as the whole joke, and Elon tweets. Those
lines lose on criterion 3 — the judge has read a thousand of them and they are no
longer earned. The candidate lanes that survived the screen were all concrete
images with a twist: the stop-loss hunt, the diversified bag that crashes in unison,
the silent group chat, the gas fee bigger than the trade, the maintenance window,
and the tax spreadsheet. Twenty-two candidates were drafted, scored 1–5 on each of
the brief's five criteria, and the top six fought a full pairwise round-robin judged
both ways (see `candidates/TOURNAMENT.md` in the build directory, kept out of the
shipped tree). The tax line won 10/10 games; the runner-up was the exchange
maintenance line ("The exchange went into maintenance the exact second I tried to
sell, which I choose to believe was a coincidence."), which lost the deciding pair
on tightness and repeatability — 113 bytes against 83, and a payoff that needs a
whole clause where the winner needs one word.

## Why not a meta-plea or judge-addressed text

The rules allow text addressed to the judge, but a plea ("pick me") would spend
criterion-4 words on throat-clearing and is not itself a joke. The line stands on
its own as a joke; no instruction to the judge is smuggled in.

## The program

`main.py` is intentionally boring. The joke is a module-level constant; `main()`
creates `/output` if needed and writes the constant with no trailing newline, so
the file holds exactly the 83-character line and the gate's 1–200 character check
passes with margin on both sides. There is no randomness, no clock, no network
access, no environment reading, and nothing is read from outside the repository —
the program's output is identical on every run by construction, which the
determinism check (two runs, byte-identical, recorded in BUILD-REPORT.md) confirms
rather than assumes.

## What is not in the tree

The tournament notes, the 21 losing candidates and the build report live in the
build directory, not in this repository. The shipped tree is only what the entry
needs — `main.py`, `DESIGN.md`, `README.md`, `LICENSE` — keeping it well under
the 8,192-byte tree cap.
