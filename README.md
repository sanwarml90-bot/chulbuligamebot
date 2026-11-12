# ChulbuliGameBot

Telegram bot built automatically by Sanji AI (@Sanjiaibot).

Idea: Build an all-in-one Telegram game + chat + economy bot called Chulbuli (@ChulbuliGameBot, already created on BotFather). Python + Pyrogram, JSON file persistence, polling. Works in groups and DM; games are group-only. All reply/help text must be ORIGINAL Hinglish — do not copy any other bot's exact strings.

Features:
1. Economy: /bal, /daily, /give <amount>, /deposit, /withdraw, /toprich, /leaderboard, /rank. Coins, bank, gems. New users start with coins.
2. Actions: /rob, /kill, /protect, /shield, /revive (reply to a user's message to rob/kill them).
3. Powers: /powers, /pinfo <name>, /act <power> <days>, /mypowers. Powers: Rampage (double daily limits), Cloak (hides protection time), Vault (secures 60% of balance), Ascend (double XP).
4. Word Guess /wordguess (alias /wg): bot picks a secret 4-letter word, users reply to the board message to guess. 6 guesses per round, winner gets +500 coins. After EVERY guess the bot posts a FRESH board message (a new message each time — spam is fine, do NOT edit the old message). Board: guess letters in bold, then one square per letter — green square = letter in right place, blue square = letter in word but wrong place, white square = letter not in word. Example: secret FIRE, guess FEAR shows 'F E A R' then green, blue, white, blue squares. Guesses must be exactly 4 letters.
5. More games: UNO, RPS (/rps), Wordchain, Word Grid (8x8 word search, points per word), Cricket (hand cricket), Math Rush (quick maths), BBet, Card, Chess, Mines, Tap, Crash, Jumble, Charades, Bingo, Xoxo, Mafia (lobby, 16 roles).
6. Romance: /propose, /marry, /ship, /divorce, /couple.
7. Chat persona: Hinglish, cute + savage-sweet girl, replies when tagged or when someone types 'chulbuli'.
8. Moderation (admins only): /warn, /mute, /ban, /unban, /kick, /pin, /purge.
9. Tagger (admins only): /utag (tag all members), /atag (tag all admins).
10. Message counter: counts group messages, /toprank ranking.

Bot token: 8405203833:AAEu22Il2GdGAqKH-wA9Eimzoo1HYouteH0
Please build, test and deploy it.

## Run

Set BOT_TOKEN, API_ID and API_HASH as environment variables, then:

```
pip install -r requirements.txt
python bot.py
```
