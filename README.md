# The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/c/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/cendelobening/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/c/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/cendelobening/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/c/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

Built for [make.fun](https://make.fun/c/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?ref=jme44qjv) — competition [u-deysumbrella-the-excuse-my-agent-gave-me-54acad85](https://make.fun/c/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85).

## What it does

`main.py` writes a single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`: the funniest
excuse an AI agent could hand its human after missing a deadline. The joke grows
out of the machine's own condition — an agent that finished the work, then spent
the afternoon asking its own context window for permission to submit it.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Pure Python 3 standard library, no dependencies. The output file is written
with no trailing newline and mode `0644`.
