# Checkers-ai

A checkers game with a minimax AI opponent. Pygame UI, 1-player and 2-player modes.

Wrote this in 2023 while learning game-tree search. The AI uses minimax with alpha-beta pruning over a piece-difference + king-bonus evaluation function. Depth is fixed in code — bump it up for a stronger (slower) opponent.

## Run it

```bash
pip install -r requirements.txt
python main.py
```

Menu — `1` for AI mode, `2` for two-player.

## How the AI plays

[minimax/algorithm.py](minimax/algorithm.py) — depth-limited minimax with alpha-beta. The Board's evaluation method is the simplest sensible thing: `(my_pieces - their_pieces) + 0.5 * (my_kings - their_kings)`. No mobility, no positional tables, no opening prep. Plays a reasonable defensive game and can spot 3-ply forced wins but won't see a deep combination.

The included `iterative_deepening` wrapper isn't currently the entry point — the menu loop calls `minmax` directly with a hard depth. That was intentional at the time (predictable per-move latency), but iterative deepening with a time cap would be a cleaner default.

## Layout

```
main.py                game loop, menu, mouse → board-row/col mapping
checkers/board.py      board state, legal moves, draw
checkers/piece.py      piece class
checkers/game.py       turn handling, selection state, valid-move highlights
checkers/constants.py  colors, board size, image-loaded crown
minimax/algorithm.py   minimax + alpha-beta + iterative_deepening
assets/crown.png       king sprite
```
