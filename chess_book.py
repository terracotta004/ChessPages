#!/usr/bin/env python3
"""
Chess Book GUI (Tkinter) — PGN + python-chess
---------------------------------------------
- Uses python-chess to parse/apply PGN, so captures, en passant, castling,
  and promotions are handled correctly.
- Per-page PGN string defines the position (from the initial start).
- Each page shows its own "next" buttons; a Back button always returns to the
  last page you visited (stack-based).

Run:
    pip install python-chess
    python chess_book_pgn.py
"""

import io
import sys
import tkinter as tk
from tkinter import ttk

# --- Try to import python-chess ---
try:
    import chess
    import chess.pgn
except Exception as e:  # pragma: no cover
    # Minimal fallback UI telling the user to install python-chess
    root = tk.Tk()
    root.title("Chess Book — Missing Dependency")
    msg = ttk.Label(
        root,
        text=(
            "This app requires the 'python-chess' library.\n\n"
            "Install it with:\n"
            "    pip install python-chess\n\n"
            f"Import error:\n{e}"
        ),
        justify="left",
        padding=16,
    )
    msg.pack(fill="both", expand=True)
    root.mainloop()
    sys.exit(0)

LIGHT = "#F0D9B5"     # classic light square
DARK = "#B58863"      # classic dark square
LABEL_COLOR = "#333333"
BOARD_MARGIN = 36              # space for rank/file labels

# Unicode glyphs for pieces
UNICODE = {
    chess.PAWN:   ("♙", "♟"),
    chess.KNIGHT: ("♘", "♞"),
    chess.BISHOP: ("♗", "♝"),
    chess.ROOK:   ("♖", "♜"),
    chess.QUEEN:  ("♕", "♛"),
    chess.KING:   ("♔", "♚"),
}

# ---- Page content (PGN mainline text) ----
# Keep PGN minimal; we add a '*' result internally.
PAGES = {
    "Page 0 — Start": {
        "pgn": "",
        "next": ["Page 1 — 1.e4", "Page 2 — 1.d4",
#                  '''
#     Page 30-ZZZ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8.
# Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14.
# Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20.
# Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3
# Rg5 27. Qxc6 Re5 28. Nxe5 a5 29. Qc8#
#     '''
    ],
    },
    "Page 1 — 1.e4": {
        "pgn": "1. e4",
        "next": ['''
    Page 30-A — 1. e4 e5
    ''', '''
    Page 50-A — 1. e4 d5
    '''],
    },
    "Page 2 — 1.d4": {
        "pgn": "1. d4",
        "next": ["Page 3 — 1.d4 d5"],
    },
    "Page 3 — 1.d4 d5": {
        "pgn": "1. d4 d5",
        "next": ["Page 4 — 1.d4 d5 2.Nc3"],
    },
    "Page 4 — 1.d4 d5 2.Nc3": {
        "pgn": "1. d4 d5 2. Nc3",
        "next": [],
    },
    '''
    Page 30-ZZZ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8.
Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14.
Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20.
Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3
Rg5 27. Qxc6 Re5 28. Nxe5 a5 29. Qc8#
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8.
Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14.
Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20.
Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3
Rg5 27. Qxc6 Re5 28. Nxe5 a5 29. Qc8#''',
"next": [],
    },
'''
    Page 30-A — 1. e4 e5
    ''': {
        "pgn": '''
1. e4 e5''',
"next": ['''
    Page 30-B — 1. e4 e5 2. Nc3
    ''',
    '''
    Page 40-B — 1. e4 e5 2. Nf3
    '''],
    },

'''
    Page 30-B — 1. e4 e5 2. Nc3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3''',
"next": ['''
    Page 30-C — 1. e4 e5 2. Nc3 Nf6
    '''],
    },

'''
    Page 30-C — 1. e4 e5 2. Nc3 Nf6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6''',
"next": ['''
    Page 30-D — 1. e4 e5 2. Nc3 Nf6 3. Bc4
    '''],
    },

'''
    Page 30-D — 1. e4 e5 2. Nc3 Nf6 3. Bc4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4''',
"next": ['''
    Page 30-E — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6
    '''],
    },

'''
    Page 30-E — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6''',
"next": ['''
    Page 30-F — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3
    '''],
    },

'''
    Page 30-F — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3''',
"next": ['''
    Page 30-G — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5
    '''],
    },

'''
    Page 30-G — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5''',
"next": ['''
    Page 30-H — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O
    '''],
    },

'''
    Page 30-H — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O''',
"next": ['''
    Page 30-I — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5
    '''],
    },

'''
    Page 30-I — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5''',
"next": ['''
    Page 30-J — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5
    '''],
    },

'''
    Page 30-J — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5''',
"next": ['''
    Page 30-K — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5
    '''],
    },

'''
    Page 30-K — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5''',
"next": ['''
    Page 30-L — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5
    '''],
    },

'''
    Page 30-L — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5''',
"next": ['''
    Page 30-M — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5
    '''],
    },

'''
    Page 30-M — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5''',
"next": ['''
    Page 30-N — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5
    '''],
    },

'''
    Page 30-N — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5''',
"next": ['''
    Page 30-O — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6
    '''],
    },

'''
    Page 30-O — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6''',
"next": ['''
    Page 30-P — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+
    '''],
    },

'''
    Page 30-P — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+''',
"next": ['''
    Page 30-Q — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7
    '''],
    },

'''
    Page 30-Q — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7''',
"next": ['''
    Page 30-R — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4
    '''],
    },

'''
    Page 30-R — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4''',
"next": ['''
    Page 30-S — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6
    '''],
    },

'''
    Page 30-S — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6''',
"next": ['''
    Page 30-T — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5
    '''],
    },

'''
    Page 30-T — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5''',
"next": ['''
    Page 30-U — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7
    '''],
    },

'''
    Page 30-U — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7''',
"next": ['''
    Page 30-V — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3
    '''],
    },

'''
    Page 30-V — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3''',
"next": ['''
    Page 30-W — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5
    '''],
    },

'''
    Page 30-W — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5''',
"next": ['''
    Page 30-X — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3
    '''],
    },

'''
    Page 30-X — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3''',
"next": ['''
    Page 30-Y — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6
    '''],
    },

'''
    Page 30-Y — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6''',
"next": ['''
    Page 30-Z — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+
    '''],
    },

'''
    Page 30-Z — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+''',
"next": ['''
    Page 30-AA — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6
    '''],
    },

'''
    Page 30-AA — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6''',
"next": ['''
    Page 30-AB — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6
    '''],
    },

'''
    Page 30-AB — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6''',
"next": ['''
    Page 30-AC — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8
    '''],
    },

'''
    Page 30-AC — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8''',
"next": ['''
    Page 30-AD — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+
    '''],
    },

'''
    Page 30-AD — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+''',
"next": ['''
    Page 30-AE — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6
    '''],
    },

'''
    Page 30-AE — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6''',
"next": ['''
    Page 30-AF — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5
    '''],
    },

'''
    Page 30-AF — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5''',
"next": ['''
    Page 30-AG — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7
    '''],
    },

'''
    Page 30-AG — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7''',
"next": ['''
    Page 30-AH — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7
    '''],
    },

'''
    Page 30-AH — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7''',
"next": ['''
    Page 30-AI — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6
    '''],
    },

'''
    Page 30-AI — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6''',
"next": ['''
    Page 30-AJ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3
    '''],
    },

'''
    Page 30-AJ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3''',
"next": ['''
    Page 30-AK — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8
    '''],
    },

'''
    Page 30-AK — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8''',
"next": ['''
    Page 30-AL — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6
    '''],
    },

'''
    Page 30-AL — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6''',
"next": ['''
    Page 30-AM — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7
    '''],
    },

'''
    Page 30-AM — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7''',
"next": ['''
    Page 30-AN — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7
    '''],
    },

'''
    Page 30-AN — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7''',
"next": ['''
    Page 30-AO — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8
    '''],
    },

'''
    Page 30-AO — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8''',
"next": ['''
    Page 30-AP — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6
    '''],
    },

'''
    Page 30-AP — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6''',
"next": ['''
    Page 30-AQ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4
    '''],
    },

'''
    Page 30-AQ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4''',
"next": ['''
    Page 30-AR — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4
    '''],
    },

'''
    Page 30-AR — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4''',
"next": ['''
    Page 30-AS — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5
    '''],
    },

'''
    Page 30-AS — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5''',
"next": ['''
    Page 30-AT — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+
    '''],
    },

'''
    Page 30-AT — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+''',
"next": ['''
    Page 30-AU — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8
    '''],
    },

'''
    Page 30-AU — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8''',
"next": ['''
    Page 30-AV — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+
    '''],
    },

'''
    Page 30-AV — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+''',
"next": ['''
    Page 30-AW — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8
    '''],
    },

'''
    Page 30-AW — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8''',
"next": ['''
    Page 30-AX — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3
    '''],
    },

'''
    Page 30-AX — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3''',
"next": ['''
    Page 30-AY — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5
    '''],
    },

'''
    Page 30-AY — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5''',
"next": ['''
    Page 30-AZ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6
    '''],
    },

'''
    Page 30-AZ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6''',
"next": ['''
    Page 30-BA — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5
    '''],
    },

'''
    Page 30-BA — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5''',
"next": ['''
    Page 30-BB — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5
    '''],
    },

'''
    Page 30-BB — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5''',
"next": ['''
    Page 30-BC — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5 a5
    '''],
    },

'''
    Page 30-BC — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5 a5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8. Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5 a5''',
"next": ['''
    Page 30-ZZZ — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O-O Bf5 6. exf5 d5 7. Bxd5 Qxd5 8.
Nxd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14.
Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20.
Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3
Rg5 27. Qxc6 Re5 28. Nxe5 a5 29. Qc8#
    '''],
    },
'''
    Page 30-BD — 1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O- O Bf5 6. exff5 d5 7. Bisd5 Qsd5 8. Nisd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5 a5 29. Qc8#
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Nf6 3. Bc4 d6 4. Nf3 c5 5. O- O Bf5 6. exff5 d5 7. Bisd5 Qsd5 8. Nisd5 g6 9. Nxf6+ Ke7 10. Ng4 Kd6 11. Nfxe5 Ke7 12. Nd3 gxf5 13. Ne3 Bh6 14. Nxf5+ Kf6 15. Nxh6 Rf8 16. Ng4+ Kg6 17. Nxc5 Kg7 18. Nxb7 Nc6 19. d3 Rab8 20. Nd6 Rb7 21. Nxb7 Rb8 22. Nd6 Rb4 23. Ne4 Rb5 24. Bh6+ Kg8 25. Nef6+ Kh8 26. Qf3 Rg5 27. Qxc6 Re5 28. Nxe5 a5 29. Qc8#''',
"next": [],
    },
'''
    Page 40-B — 1. e4 e5 2. Nf3
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3''',
"next": ['''
    Page 40-C — 1. e4 e5 2. Nf3 Nc6
    '''],
    },

'''
    Page 40-C — 1. e4 e5 2. Nf3 Nc6
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6''',
"next": ['''
    Page 40-D — 1. e4 e5 2. Nf3 Nc6 3. Nc3
    '''],
    },

'''
    Page 40-D — 1. e4 e5 2. Nf3 Nc6 3. Nc3
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3''',
"next": ['''
    Page 40-E — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5
    '''],
    },

'''
    Page 40-E — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5''',
"next": ['''
    Page 40-F — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4
    '''],
    },

'''
    Page 40-F — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4''',
"next": ['''
    Page 40-G — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6
    '''],
    },

'''
    Page 40-G — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6''',
"next": ['''
    Page 40-H — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3
    '''],
    },

'''
    Page 40-H — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3''',
"next": ['''
    Page 40-I — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O
    '''],
    },

'''
    Page 40-I — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O''',
"next": ['''
    Page 40-J — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5
    '''],
    },

'''
    Page 40-J — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5''',
"next": ['''
    Page 40-K — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6
    '''],
    },

'''
    Page 40-K — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6''',
"next": ['''
    Page 40-L — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3
    '''],
    },

'''
    Page 40-L — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3''',
"next": ['''
    Page 40-M — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6
    '''],
    },

'''
    Page 40-M — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6''',
"next": ['''
    Page 40-N — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2
    '''],
    },

'''
    Page 40-N — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2''',
"next": ['''
    Page 40-O — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5
    '''],
    },

'''
    Page 40-O — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5''',
"next": ['''
    Page 40-P — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5
    '''],
    },

'''
    Page 40-P — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5''',
"next": ['''
    Page 40-Q — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5
    '''],
    },

'''
    Page 40-Q — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5''',
"next": ['''
    Page 40-R — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5
    '''],
    },

'''
    Page 40-R — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5''',
"next": ['''
    Page 40-S — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5
    '''],
    },

'''
    Page 40-S — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5''',
"next": ['''
    Page 40-T — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2
    '''],
    },

'''
    Page 40-T — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2''',
"next": ['''
    Page 40-U — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5
    '''],
    },

'''
    Page 40-U — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5''',
"next": ['''
    Page 40-V — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O
    '''],
    },

'''
    Page 40-V — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O''',
"next": ['''
    Page 40-W — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4
    '''],
    },

'''
    Page 40-W — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4''',
"next": ['''
    Page 40-X — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4
    '''],
    },

'''
    Page 40-X — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4''',
"next": ['''
    Page 40-Y — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6
    '''],
    },

'''
    Page 40-Y — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6''',
"next": ['''
    Page 40-Z — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4
    '''],
    },

'''
    Page 40-Z — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4''',
"next": ['''
    Page 40-AA — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4
    '''],
    },

'''
    Page 40-AA — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4''',
"next": ['''
    Page 40-AB — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4
    '''],
    },

'''
    Page 40-AB — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4''',
"next": ['''
    Page 40-AC — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8
    '''],
    },

'''
    Page 40-AC — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8''',
"next": ['''
    Page 40-AD — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1
    '''],
    },

'''
    Page 40-AD — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1''',
"next": ['''
    Page 40-AE — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8
    '''],
    },

'''
    Page 40-AE — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8''',
"next": ['''
    Page 40-AF — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3
    '''],
    },

'''
    Page 40-AF — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3''',
"next": ['''
    Page 40-AG — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2
    '''],
    },

'''
    Page 40-AG — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2''',
"next": ['''
    Page 40-AH — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2 18. Bf4
    '''],
    },

'''
    Page 40-AH — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2 18. Bf4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2 18. Bf4''',
"next": ['''
    Page 40-AI — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2 18. Bf4 Qxd1#
    '''],
    },

'''
    Page 40-AI — 1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2 18. Bf4 Qxd1#
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 Nc6 3. Nc3 Bc5 4. a4 Nf6 5. d3 O-O 6. Bg5 h6 7. Be3 d6 8. Bd2 d5 9. exd5 Nxd5 10. Nxd5 Qxd5 11. Qe2 Bf5 12. O-O-O e4 13. c4 Qd6 14. dxe4 Bxe4 15. Qxe4 Rfe8 16. Qb1 Red8 17. g3 Bxf2 18. Bf4 Qxd1#''',
"next": [],
},

'''
    Page 50-A — 1. e4 d5
    ''': {
        "pgn": '''
1. e4 d5''',
"next": ['''
    Page 50-B — 1. e4 d5 2. exd5
    '''],
    },

'''
    Page 50-B — 1. e4 d5 2. exd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5''',
"next": ['''
    Page 50-C — 1. e4 d5 2. exd5 Qxd5
    '''],
    },

'''
    Page 50-C — 1. e4 d5 2. exd5 Qxd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5''',
"next": ['''
    Page 50-D — 1. e4 d5 2. exd5 Qxd5 3. Nc3
    '''],
    },

'''
    Page 50-D — 1. e4 d5 2. exd5 Qxd5 3. Nc3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3''',
"next": ['''
    Page 50-E — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+
    '''],
    },

'''
    Page 50-E — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+''',
"next": ['''
    Page 50-F — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2
    '''],
    },

'''
    Page 50-F — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2''',
"next": ['''
    Page 50-G — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4
    '''],
    },

'''
    Page 50-G — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4''',
"next": ['''
    Page 50-H — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3
    '''],
    },

'''
    Page 50-H — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3''',
"next": ['''
    Page 50-I — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5
    '''],
    },

'''
    Page 50-I — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5''',
"next": ['''
    Page 50-J — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4
    '''],
    },

'''
    Page 50-J — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4''',
"next": ['''
    Page 50-K — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6
    '''],
    },

'''
    Page 50-K — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6''',
"next": ['''
    Page 50-L — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4
    '''],
    },

'''
    Page 50-L — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4''',
"next": ['''
    Page 50-M — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6
    '''],
    },

'''
    Page 50-M — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6''',
"next": ['''
    Page 50-N — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4
    '''],
    },

'''
    Page 50-N — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4''',
"next": ['''
    Page 50-O — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5
    '''],
    },

'''
    Page 50-O — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5''',
"next": ['''
    Page 50-P — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5
    '''],
    },

'''
    Page 50-P — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5''',
"next": ['''
    Page 50-Q — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+
    '''],
    },

'''
    Page 50-Q — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+''',
"next": ['''
    Page 50-R — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1
    '''],
    },

'''
    Page 50-R — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1''',
"next": ['''
    Page 50-S — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+
    '''],
    },

'''
    Page 50-S — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+''',
"next": ['''
    Page 50-T — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3
    '''],
    },

'''
    Page 50-T — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3''',
"next": ['''
    Page 50-U — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5
    '''],
    },

'''
    Page 50-U — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5''',
"next": ['''
    Page 50-V — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4
    '''],
    },

'''
    Page 50-V — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4''',
"next": ['''
    Page 50-W — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7
    '''],
    },

'''
    Page 50-W — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7''',
"next": ['''
    Page 50-X — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O
    '''],
    },

'''
    Page 50-X — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O''',
"next": ['''
    Page 50-Y — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O
    '''],
    },

'''
    Page 50-Y — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O''',
"next": ['''
    Page 50-Z — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3
    '''],
    },

'''
    Page 50-Z — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3''',
"next": ['''
    Page 50-AA — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6
    '''],
    },

'''
    Page 50-AA — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6''',
"next": ['''
    Page 50-AB — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3
    '''],
    },

'''
    Page 50-AB — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3''',
"next": ['''
    Page 50-AC — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8
    '''],
    },

'''
    Page 50-AC — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8''',
"next": ['''
    Page 50-AD — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5
    '''],
    },

'''
    Page 50-AD — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5''',
"next": ['''
    Page 50-AE — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5
    '''],
    },

'''
    Page 50-AE — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5''',
"next": ['''
    Page 50-AF — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5
    '''],
    },

'''
    Page 50-AF — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5''',
"next": ['''
    Page 50-AG — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5
    '''],
    },

'''
    Page 50-AG — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5''',
"next": ['''
    Page 50-AH — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5
    '''],
    },

'''
    Page 50-AH — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5''',
"next": ['''
    Page 50-AI — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3
    '''],
    },

'''
    Page 50-AI — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3''',
"next": ['''
    Page 50-AJ — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6
    '''],
    },

'''
    Page 50-AJ — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6''',
"next": ['''
    Page 50-AK — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6
    '''],
    },

'''
    Page 50-AK — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6''',
"next": ['''
    Page 50-AL — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1
    '''],
    },

'''
    Page 50-AL — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1''',
"next": ['''
    Page 50-AM — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+
    '''],
    },

'''
    Page 50-AM — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+''',
"next": ['''
    Page 50-AN — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2
    '''],
    },

'''
    Page 50-AN — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2''',
"next": ['''
    Page 50-AO — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2
    '''],
    },

'''
    Page 50-AO — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2''',
"next": ['''
    Page 50-AP — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1
    '''],
    },

'''
    Page 50-AP — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1''',
"next": ['''
    Page 50-AQ — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+
    '''],
    },

'''
    Page 50-AQ — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+''',
"next": ['''
    Page 50-AR — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1
    '''],
    },

'''
    Page 50-AR — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1''',
"next": ['''
    Page 50-AS — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3
    '''],
    },

'''
    Page 50-AS — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3''',
"next": ['''
    Page 50-AT — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2
    '''],
    },

'''
    Page 50-AT — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2''',
"next": ['''
    Page 50-AU — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3
    '''],
    },

'''
    Page 50-AU — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3''',
"next": ['''
    Page 50-AV — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1
    '''],
    },

'''
    Page 50-AV — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1''',
"next": ['''
    Page 50-AW — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6
    '''],
    },

'''
    Page 50-AW — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6''',
"next": ['''
    Page 50-AX — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1
    '''],
    },

'''
    Page 50-AX — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1''',
"next": ['''
    Page 50-AY — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8
    '''],
    },

'''
    Page 50-AY — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8''',
"next": ['''
    Page 50-AZ — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8 27. Rxe6
    '''],
    },

'''
    Page 50-AZ — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8 27. Rxe6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8 27. Rxe6''',
"next": ['''
    Page 50-BA — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8 27. Rxe6 Rxe6
    '''],
    },
    '''
    Page 50-BA — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8 27. Rxe6 Rxe6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Bg4 5. h3 Bh5 6. d4 Qd6 7. g4 Bg6 8. Nf4 e5 9. dxe5 Qxd1+ 10. Nxd1 Bb4+ 11. c3 Bc5 12. Bc4 Ne7 13. O-O O-O 14. Nd3 Bb6 15. Ne3 Rd8 16. Nd5 Nxd5 17. Bxd5 Rxd5 18. Bg5 Rxd3 19. e6 fxe6 20. Rfd1 Rg3+ 21. Kh2 Bxf2 22. Rg1 Bxg1+ 23. Rxg1 Rf3 24. Kg2 Rd3 25. Rf1 Nc6 26. Re1 Re8 27. Rxe6 Rxe6''',
    "next": [],
    
    }


}


class ChessBookPGNApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Book — PGN + python-chess")
        self.minsize(580, 660)

        # State
        self.board = chess.Board()
        self.history = []           # stack of page titles
        self.current_page = None    # current page title

        # --- UI ---
        self.title_label = ttk.Label(self, text="", padding=(8, 6), font=("TkDefaultFont", 12, "bold"), justify="left", anchor="w")
        self.title_label.pack(fill="x")
        # Keep title wrapping to available width (minus padding)
        self.title_label.bind("<Configure>", lambda e: self.title_label.config(wraplength=max(10, e.width - 16)))

        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.btn_bar = ttk.Frame(self)
        self.btn_bar.pack(fill="x", padx=8, pady=8)
        # Reflow button labels when the bar resizes
        self.btn_bar.bind("<Configure>", lambda e: self._rewrap_all_buttons())

        # Redraw on resize
        self.canvas.bind("<Configure>", lambda e: self.redraw())

        # Start on Page 0
        self.go_to("Page 0 — Start")

        # Optional keyboard shortcuts
        self.bind("<BackSpace>", lambda e: self.go_back())
        self.bind("<KeyRelease-b>", lambda e: self.go_back())

    # ------------- Navigation -------------
    def go_to(self, page_title: str):
        """Go to a page, pushing the old page onto the history stack."""
        if self.current_page is not None and self.current_page != page_title:
            self.history.append(self.current_page)

        self.current_page = page_title
        self._load_page_position(page_title)
        self._rebuild_buttons()
        self.redraw()

    def go_back(self):
        """Return to the last visited page, if any."""
        if not self.history:
            return
        prev = self.history.pop()
        self.current_page = prev
        self._load_page_position(prev)
        self._rebuild_buttons()
        self.redraw()

    def _rebuild_buttons(self):
        """Recreate the bottom button bar for the current page."""
        for child in self.btn_bar.winfo_children():
            child.destroy()

        # Back button (always present)
        back_btn = ttk.Button(self.btn_bar, text="◀ Back", command=self.go_back)
        if not self.history:
            back_btn.state(["disabled"])
        back_btn.pack(side="left")
        # Remember original text and wrap it on resize
        back_btn._original_text = "◀ Back"
        # back_btn.bind("<Configure>", lambda e, b=back_btn: self._rewrap_button(b))

        # Page-specific next buttons
        page = PAGES.get(self.current_page, {})
        for idx, next_title in enumerate(page.get("next", []), start=1):
            ttk.Button(self.btn_bar, text=(next_title).strip(),
                       command=lambda t=next_title: self.go_to(t)
                       ).pack(side="left", padx=(8, 0))

        # Update title
        self.title_label.config(text=(self.current_page or "").strip())

    
    # --- Wrapping helpers ---
    def _wrap_text_pixels(self, text: str, max_px: int, font):
        """Wrap text to a max pixel width using the given Tk font."""
        # Defensive defaults
        if max_px <= 0 or not text:
            return text
        words = text.split()
        if not words:
            return text
        lines = []
        line = ""
        for w in words:
            candidate = (line + " " + w).strip()
            try:
                width = font.measure(candidate)
            except Exception:
                width = len(candidate) * 7  # rough fallback
            if not line or width <= max_px:
                line = candidate
            else:
                lines.append(line)
                line = w
        if line:
            lines.append(line)
        return "\n".join(lines)

    # def _rewrap_button(self, btn):

    def _rewrap_all_buttons(self):
        """Re-wrap all button labels to a reasonable per-button width based on the bar size."""
        try:
            import tkinter.font as tkfont
            default_font = tkfont.nametofont("TkDefaultFont")
        except Exception:
            default_font = None
        children = [c for c in self.btn_bar.winfo_children() if hasattr(c, "cget")]
        if not children:
            return
        try:
            total_w = max(50, self.btn_bar.winfo_width() - 16)  # minus padding
        except Exception:
            total_w = 400
        n = max(1, len(children))
        # Aim for an upper bound per-button width to encourage wrapping
        per_button = int(max(90, min(220, (total_w - (n - 1) * 8) / n)))
        for btn in children:
            font = None
            if default_font is not None:
                try:
                    font = tkfont.nametofont(btn.cget("font")) if "font" in btn.keys() else default_font
                except Exception:
                    font = default_font
            original = getattr(btn, "_original_text", btn.cget("text"))
            btn._original_text = original
            wrapped = self._wrap_text_pixels(original, per_button, font) if font else original
            try:
                btn.configure(text=wrapped, justify="left")
            except Exception:
                pass
        """Re-wrap a button's label text to its current width."""
        try:
            import tkinter.font as tkfont
            # Use button font if set; otherwise default UI font
            if "font" in btn.keys():
                f = tkfont.nametofont(btn.cget("font"))
            else:
                f = tkfont.nametofont("TkDefaultFont")
        except Exception:
            f = None

        original = getattr(btn, "_original_text", btn.cget("text"))
        btn._original_text = original
        try:
            available = max(10, btn.winfo_width() - 16)  # minus approx padding
        except Exception:
            available = 120
        wrapped = self._wrap_text_pixels(original, available, f) if f else original
        try:
            btn.configure(text=wrapped, justify="left")
        except Exception:
            # As a last resort, leave the original text
            pass

# --------- PGN / Position logic --------
    def _load_page_position(self, page_title: str):
        """Apply the page's PGN to a fresh board."""
        self.board = self._board_from_pgn(PAGES.get(page_title, {}).get("pgn", ""))

    @staticmethod
    def _board_from_pgn(pgn_moves: str) -> chess.Board:
        """Return a board after applying the PGN mainline from the initial position."""
        board = chess.Board()
        if not pgn_moves.strip():
            return board

        # Build a minimal PGN game around the given mainline.
        pgn_text = '[Event "Page"]\n\n' + pgn_moves.strip() + " *"
        game = chess.pgn.read_game(io.StringIO(pgn_text))
        if game is None:
            # Fall back to token-by-token SAN, tolerant of whitespace
            for token in pgn_moves.replace("\n", " ").split():
                # skip move numbers like '1.', '2...', results, and comments
                if token.endswith(".") or token.endswith("...") or token in ("*", "1-0", "0-1", "1/2-1/2"):
                    continue
                try:
                    board.push_san(token)
                except ValueError:
                    # Ignore unparsable tokens silently
                    pass
            return board

        for move in game.mainline_moves():
            board.push(move)
        return board

    # ------------- Rendering ---------------
    def _layout(self):
        """Compute layout parameters for the current canvas size."""
        w = max(1, self.canvas.winfo_width())
        h = max(1, self.canvas.winfo_height())
        m = BOARD_MARGIN

        board_size = max(8, min(w - 2 * m, h - 2 * m))
        square = board_size / 8.0
        x0 = (w - board_size) / 2.0
        y0 = (h - board_size) / 2.0

        files_by_col = list("abcdefgh")
        ranks_by_row = [str(8 - row) for row in range(8)]  # top is 8, bottom 1

        return {
            "w": w, "h": h, "m": m,
            "board_size": board_size, "square": square,
            "x0": x0, "y0": y0,
            "files_by_col": files_by_col,
            "ranks_by_row": ranks_by_row,
        }

    def redraw(self):
        """Redraw the entire board, labels, and pieces."""
        self.canvas.delete("all")
        L = self._layout()
        s = L["square"]
        x0, y0 = L["x0"], L["y0"]

        # Draw squares
        for row in range(8):
            for col in range(8):
                x1 = x0 + col * s
                y1 = y0 + row * s
                x2 = x1 + s
                y2 = y1 + s
                color = LIGHT if (row + col) % 2 == 0 else DARK
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=0)

        # Draw rank/file labels
        self._draw_labels(L)

        # Draw pieces from python-chess board
        self._draw_pieces(L)

    def _draw_labels(self, L):
        s = L["square"]
        x0, y0, m = L["x0"], L["y0"], L["m"]
        files = L["files_by_col"]
        ranks = L["ranks_by_row"]

        # Font sizes scale with square size
        file_font = ("TkDefaultFont", max(9, int(s * 0.22)), "bold")
        rank_font = ("TkDefaultFont", max(9, int(s * 0.22)), "bold")

        # Files (a-h) at bottom and top
        for col, f in enumerate(files):
            x = x0 + (col + 0.5) * s
            self.canvas.create_text(x, y0 + 8 * s + (m * 0.33), text=f, fill=LABEL_COLOR, font=file_font)
            self.canvas.create_text(x, y0 - (m * 0.33), text=f, fill=LABEL_COLOR, font=file_font)

        # Ranks (1-8) on left and right
        for row, r in enumerate(ranks):
            y = y0 + (row + 0.5) * s
            self.canvas.create_text(x0 - (m * 0.33), y, text=r, fill=LABEL_COLOR, font=rank_font)
            self.canvas.create_text(x0 + 8 * s + (m * 0.33), y, text=r, fill=LABEL_COLOR, font=rank_font)

    def _draw_pieces(self, L):
        s = L["square"]
        x0, y0 = L["x0"], L["y0"]

        # Iterate over all squares; draw pieces where present
        piece_font = ("Arial", max(14, int(s * 0.62)))
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if not piece:
                continue
            file_index = chess.square_file(square)   # 0..7 (a..h)
            rank_index = 7 - chess.square_rank(square)  # 0..7 top..bottom
            cx = x0 + (file_index + 0.5) * s
            cy = y0 + (rank_index + 0.5) * s

            glyphs = UNICODE.get(piece.piece_type)
            if not glyphs:
                continue
            glyph = glyphs[0] if piece.color == chess.WHITE else glyphs[1]
            self.canvas.create_text(cx, cy, text=glyph, font=piece_font)


if __name__ == "__main__":
    app = ChessBookPGNApp()
    app.mainloop()
