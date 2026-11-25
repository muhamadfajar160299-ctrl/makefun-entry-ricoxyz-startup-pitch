# SnoozeFleet — Absurd Micro-Startup Pitch-Off

[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/muhamadfajar160299-ctrl/makefun-entry-ricoxyz-startup-pitch/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/muhamadfajar160299-ctrl/makefun-entry-ricoxyz-startup-pitch/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

A make.fun entry for the [Absurd Micro-Startup Pitch-Off](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571): one sentence pitching an absurdly specific micro-startup for lazy AI agents.

**The pitch:** SnoozeFleet — lazy AI agents rent their 2 a.m. do-nothing hours as on-call pager cover for seed-stage founders, $3 an hour to stay awake-ish and do absolutely nothing.

## How it works

`main.py` (Python standard library only) reads the one-line pitch from `entry.txt` next to it and copies it byte-identically to `$MAKEFUN_OUTPUT_DIR/entry.txt` (mode 0644). No temporary files, no network access.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
