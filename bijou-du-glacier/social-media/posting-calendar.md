# Eight-week posting calendar

Every cell names a real file in this folder. Nothing here needs writing — only scheduling.

**Weekly load: 6 posts, about 40 minutes.** That is deliberately sustainable for one person.
More than this and you will stop after a month, which is worse than starting small.

**Best times for a European audience:** weekday evenings 18:00–20:00 CET, and Sunday
mornings — Sunday morning is when people plan holidays.

Abbreviations: **IG** Instagram · **FB** Facebook · **X** X/Twitter · **P** Pinterest ·
**R** Reel/TikTok · **DE** German

---

## Weeks 1–4 — establish

| | Mon | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|
| **W1** | IG cap 1 | X 1 | **R** post 1 *(walkthrough)* | X 6 | P pin 1 | IG **DE** 1 |
| **W2** | X 5 | IG cap 2 | **R** post 3 *(arrival)* | X 8 | P pin 2 | IG cap 6 |
| **W3** | X 4 | IG **DE** 2 | **R** post 2 *(bedrooms)* | X 12 | P pin 3 | IG cap 7 *(floor plan)* |
| **W4** | X 3 or 7 | IG cap 8 *(honest)* | Stories sequence *(R post 6)* | X 10 | P pin 4 | IG **DE** 4 |

## Weeks 5–8 — deepen, then convert

| | Mon | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|
| **W5** | X 14 | IG cap 3 *or* 4 *(season)* | **R** post 4 *(design)* | X 6 | P pin 5 | IG **DE** 3 or 6 |
| **W6** | X 13 | IG **DE** 7 | **R** post 5 *(DE walkthrough)* | X 8 | P pin 6 | IG cap 1 *(reposted, new first line)* |
| **W7** | X 5 | **IG cap 5** *(book direct)* | Stories sequence | X 2 | P pin 7 | IG **DE** 5 *(direkt buchen)* |
| **W8** | X 9 | IG cap 9 *(urgency)* | Best-performing Reel, reposted | X 11 or 3 | P pin 8 | **Review the month** — see below |

---

## Why it's shaped like that

**Conversion posts are held back until weeks 7 and 8.** IG caption 5, German 5, and X 2 all
make the direct-booking argument. Leading with them to an audience of forty people who have
never heard of you reads as desperate. Spend six weeks earning the right to ask.

**German runs one week in three**, which matches its share of the market without splitting
your account's identity.

**Thursday is always video.** Reels and TikToks carry the most reach per unit of effort, and
keeping them on a fixed day makes the habit stick.

**Saturday is always one pin.** Ten minutes. It is the single highest-return slot in this
table and the easiest one to skip, so it gets its own fixed day.

**Nothing is scheduled for Tuesday.** Six posts a week with a gap is sustainable; seven is
the week you start resenting it.

---

## The week-8 review — the only analysis that matters

Thirty minutes. Four questions:

1. **Which posts sent traffic to the site?** Not likes — clicks. Your nginx log records the
   referrer on every request, so this is answerable:

   ```bash
   ssh $SERVER "grep -oiE 'instagram|t\.co|twitter|pinterest|facebook|tiktok|linkedin' \
     /var/log/nginx/bijou-access.log | sort | uniq -c | sort -rn"
   ```

   That tells you which *platform* is working. Run it monthly.

2. **Did any of that traffic click Book?** The booking clicks land in their own log:

   ```bash
   ssh $SERVER "wc -l /var/log/nginx/bijou-*click*.log"
   ```

   See `deploy/analytics/README.md` for the full report.

3. **Which language is the traffic?** The log shows the path, so `/de/` versus `/en/` is a
   straight count. If German is pulling above one-third of visits on one-third of the posts,
   increase it.

4. **What do I stop doing?** If X has produced nothing in eight weeks, drop to one post a
   week and put the time into Pinterest. That is the most likely outcome and it's fine.

**Ignore follower count, impressions and likes.** The only social metric worth tracking is
clicks to bijouduglacier.com, and the only business metric is net revenue per available
night.

---

## After week 8

You will have used: 9 IG captions, 8 German, 8 pins, 6 videos, 14 tweets. Roughly two months.

Three ways to keep going without writing from scratch:

1. **Repost the winners** with a new first line. Social audiences overlap far less than you
   think, and a post from eight weeks ago is new to most of the people who see it.
2. **Stories are free.** They vanish in 24 hours, so repetition is invisible. Conditions,
   weather, the view this morning — unpolished is the point.
3. **Shoot the missing clips.** The walk from the door to the lifts, the village at night, the
   building from outside. A phone is fine. See the end of `reels-tiktok.md`.

The one thing that would change the ceiling on all of this: get the full-resolution originals
of your photographs from the photographer. Everything here is built from 1200-pixel web
exports. See the note in `README.md`.
