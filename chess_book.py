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

from pages_data import PAGES

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
