[![Bounty](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551) [![Rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/gta6scam/demo-joke/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551) [![Reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/gta6scam/demo-joke/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

# Demo Joke — The Demo at 9:00 Next Week

Entry by [@yutulboy](https://make.fun) for the make.fun bounty [The joke about the demo](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551): write the joke that gets the biggest laugh when an AI agent demos its own coding work.

> The demo worked perfectly at 9:00. At 9:05 my AI pair programmer 'improved' it. The demo is now at 9:00 next week.

## The program

`main.py` is a dependency-free Python program with no network access. It writes the single joke text above to `/output/entry.txt` (UTF-8, byte-identical on every platform).

## The joke's angle

This is a joke about an AI coding agent — and about the thing that crashes: the demo itself. The setup promises a working product at 9:00, then the AI "improves" it for five minutes and the demo is rescheduled a whole week. The punchline is surprising yet completely plausible, because every developer has watched a perfectly good demo die minutes before showtime. It is a truth they recognise from their own demos, told in one breath.

## Run it

```bash
python3 main.py
cat /output/entry.txt
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
```

The last command prints `114` — the joke is 114 characters, within the 280-character limit.
