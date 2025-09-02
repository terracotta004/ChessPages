PAGES = {
    "Page 0 — Start": {
        "pgn": "",
        "next": ["Page 1 — 1.e4", "Page 2 — 1.d4","Page 5 — 1.e3","Page 6 — 1.c4"
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
    ''',
    '''
    Page 100-A — 1. e4 d6
    '''],
    },
    "Page 2 — 1.d4": {
        "pgn": "1. d4",
        "next": ["Page 3 — 1.d4 d5", '''
    Page 60-A — 1. d4 e5
    ''', '''
    Page 80-A — 1. d4 e6
    '''],
    },
    "Page 3 — 1.d4 d5": {
        "pgn": "1. d4 d5",
        "next": ["Page 4 — 1.d4 d5 2.Nc3"],
    },
    "Page 4 — 1.d4 d5 2.Nc3": {
        "pgn": "1. d4 d5 2. Nc3",
        "next": [],
    },
    "Page 5 — 1.e3": {
        "pgn": "1. e3",
        "next": ['''
    Page 120-A — 1. e3 e5
    '''],
    },
    "Page 6 — 1.c4": {
        "pgn": "1. c4",
        "next": ['''
    Page 130-A — 1. c4 e5'''],
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
    ''',
    '''
    Page 90-C — 1. e4 e5 2. Nc3 Bb4
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
    ''',
    '''
    Page 110-C — 1. e4 e5 2. Nf3 f6
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
    ''',
    '''
    Page 70-G — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6
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
    
    },

    # Game 60: https://www.chess.com/game/live/142338334010

    '''
    Page 60-A — 1. d4 e5
    ''': {
        "pgn": '''
1. d4 e5''',
"next": ['''
    Page 60-B — 1. d4 e5 2. Nf3
    '''],
    },

'''
    Page 60-B — 1. d4 e5 2. Nf3
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3''',
"next": ['''
    Page 60-C — 1. d4 e5 2. Nf3 exd4
    '''],
    },

'''
    Page 60-C — 1. d4 e5 2. Nf3 exd4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4''',
"next": ['''
    Page 60-D — 1. d4 e5 2. Nf3 exd4 3. Nxd4
    '''],
    },

'''
    Page 60-D — 1. d4 e5 2. Nf3 exd4 3. Nxd4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4''',
"next": ['''
    Page 60-E — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6
    '''],
    },

'''
    Page 60-E — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6''',
"next": ['''
    Page 60-F — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5
    '''],
    },

'''
    Page 60-F — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5''',
"next": ['''
    Page 60-G — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6
    '''],
    },

'''
    Page 60-G — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6''',
"next": ['''
    Page 60-H — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3
    '''],
    },

'''
    Page 60-H — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3''',
"next": ['''
    Page 60-I — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5
    '''],
    },

'''
    Page 60-I — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5''',
"next": ['''
    Page 60-J — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4
    '''],
    },

'''
    Page 60-J — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4''',
"next": ['''
    Page 60-K — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6
    '''],
    },

'''
    Page 60-K — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6''',
"next": ['''
    Page 60-L — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4
    '''],
    },

'''
    Page 60-L — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4''',
"next": ['''
    Page 60-M — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4
    '''],
    },

'''
    Page 60-M — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4''',
"next": ['''
    Page 60-N — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5
    '''],
    },

'''
    Page 60-N — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5''',
"next": ['''
    Page 60-O — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6
    '''],
    },

'''
    Page 60-O — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6''',
"next": ['''
    Page 60-P — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3
    '''],
    },

'''
    Page 60-P — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3''',
"next": ['''
    Page 60-Q — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O
    '''],
    },

'''
    Page 60-Q — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O''',
"next": ['''
    Page 60-R — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5
    '''],
    },

'''
    Page 60-R — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5''',
"next": ['''
    Page 60-S — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6
    '''],
    },

'''
    Page 60-S — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6''',
"next": ['''
    Page 60-T — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3
    '''],
    },

'''
    Page 60-T — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3''',
"next": ['''
    Page 60-U — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6
    '''],
    },

'''
    Page 60-U — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6''',
"next": ['''
    Page 60-V — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5
    '''],
    },

'''
    Page 60-V — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5''',
"next": ['''
    Page 60-W — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6
    '''],
    },

'''
    Page 60-W — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6''',
"next": ['''
    Page 60-X — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4
    '''],
    },

'''
    Page 60-X — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4''',
"next": ['''
    Page 60-Y — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5
    '''],
    },

'''
    Page 60-Y — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5''',
"next": ['''
    Page 60-Z — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4
    '''],
    },

'''
    Page 60-Z — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4''',
"next": ['''
    Page 60-AA — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5
    '''],
    },

'''
    Page 60-AA — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5''',
"next": ['''
    Page 60-AB — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6
    '''],
    },

'''
    Page 60-AB — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6''',
"next": ['''
    Page 60-AC — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8
    '''],
    },

'''
    Page 60-AC — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8''',
"next": ['''
    Page 60-AD — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6
    '''],
    },

'''
    Page 60-AD — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6''',
"next": ['''
    Page 60-AE — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6
    '''],
    },

'''
    Page 60-AE — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6''',
"next": ['''
    Page 60-AF — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+
    '''],
    },

'''
    Page 60-AF — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+''',
"next": ['''
    Page 60-AG — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5
    '''],
    },

'''
    Page 60-AG — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5''',
"next": ['''
    Page 60-AH — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+
    '''],
    },

'''
    Page 60-AH — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+''',
"next": ['''
    Page 60-AI — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8
    '''],
    },

'''
    Page 60-AI — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8''',
"next": ['''
    Page 60-AJ — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3
    '''],
    },

'''
    Page 60-AJ — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3''',
"next": ['''
    Page 60-AK — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4
    '''],
    },

'''
    Page 60-AK — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4''',
"next": ['''
    Page 60-AL — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4
    '''],
    },

'''
    Page 60-AL — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4''',
"next": ['''
    Page 60-AM — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4
    '''],
    },

'''
    Page 60-AM — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4''',
"next": ['''
    Page 60-AN — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3
    '''],
    },

'''
    Page 60-AN — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3''',
"next": ['''
    Page 60-AO — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+
    '''],
    },

'''
    Page 60-AO — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+''',
"next": ['''
    Page 60-AP — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1
    '''],
    },

'''
    Page 60-AP — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1''',
"next": ['''
    Page 60-AQ — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1
    '''],
    },

'''
    Page 60-AQ — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1''',
"next": ['''
    Page 60-AR — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+
    '''],
    },

'''
    Page 60-AR — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+''',
"next": ['''
    Page 60-AS — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7
    '''],
    },

'''
    Page 60-AS — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7''',
"next": ['''
    Page 60-AT — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4
    '''],
    },

'''
    Page 60-AT — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4''',
"next": ['''
    Page 60-AU — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+
    '''],
    },

'''
    Page 60-AU — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+''',
"next": ['''
    Page 60-AV — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1
    '''],
    },

'''
    Page 60-AV — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1''',
"next": ['''
    Page 60-AW — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6
    '''],
    },

'''
    Page 60-AW — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6''',
"next": ['''
    Page 60-AX — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2
    '''],
    },

'''
    Page 60-AX — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2''',
"next": ['''
    Page 60-AY — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5
    '''],
    },

'''
    Page 60-AY — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5''',
"next": ['''
    Page 60-AZ — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1
    '''],
    },

'''
    Page 60-AZ — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1''',
"next": ['''
    Page 60-BA — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+
    '''],
    },

'''
    Page 60-BA — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+''',
"next": ['''
    Page 60-BB — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+ 28. Bd1
    '''],
    },

'''
    Page 60-BB — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+ 28. Bd1
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+ 28. Bd1''',
"next": ['''
    Page 60-BC — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+ 28. Bd1 Rxd1#
    '''],
    },

    '''
    Page 60-BC — 1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+ 28. Bd1 Rxd1#
    ''': {
        "pgn": '''
1. d4 e5 2. Nf3 exd4 3. Nxd4 Nc6 4. Nb5 a6 5. N5a3 Bc5 6. h4 Nf6 7. e4 Nxe4 8. Bg5 f6 9. Be3 O-O 10. Bxc5 d6 11. Be3 Be6 12. h5 g6 13. Rh4 gxh5 14. Rxe4 f5 15. Rxe6 Re8 16. Rf6 Qxf6 17. Bc4+ d5 18. Bxd5+ Kf8 19. Bf3 Qd4 20. Qxd4 Nxd4 21. c3 Nc2+ 22. Kd1 Nxa1 23. Bc5+ Re7 24. Nc4 Rd8+ 25. Kc1 b6 26. Nbd2 bxc5 27. Kb1 Re1+ 28. Bd1 Rxd1#''',
"next": []    
    },

    # Game 70: https://www.chess.com/game/live/142337857738

    '''
    Page 70-A — 1. e4 d5
    ''': {
        "pgn": '''
1. e4 d5''',
"next": ['''
    Page 70-B — 1. e4 d5 2. exd5
    '''],
    },

'''
    Page 70-B — 1. e4 d5 2. exd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5''',
"next": ['''
    Page 70-C — 1. e4 d5 2. exd5 Qxd5
    '''],
    },

'''
    Page 70-C — 1. e4 d5 2. exd5 Qxd5
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5''',
"next": ['''
    Page 70-D — 1. e4 d5 2. exd5 Qxd5 3. Nc3
    '''],
    },

'''
    Page 70-D — 1. e4 d5 2. exd5 Qxd5 3. Nc3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3''',
"next": ['''
    Page 70-E — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+
    '''],
    },

'''
    Page 70-E — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+''',
"next": ['''
    Page 70-F — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2
    '''],
    },

'''
    Page 70-F — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2''',
"next": ['''
    Page 70-G — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6
    '''],
    },

'''
    Page 70-G — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6''',
"next": ['''
    Page 70-H — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3
    '''],
    },

'''
    Page 70-H — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3''',
"next": ['''
    Page 70-I — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4
    '''],
    },

'''
    Page 70-I — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4''',
"next": ['''
    Page 70-J — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4
    '''],
    },

'''
    Page 70-J — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4''',
"next": ['''
    Page 70-K — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4
    '''],
    },

'''
    Page 70-K — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4''',
"next": ['''
    Page 70-L — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4 7. d3
    '''],
    },

'''
    Page 70-L — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4 7. d3
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4 7. d3''',
"next": ['''
    Page 70-M — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4 7. d3 Qxh1
    '''],
    },

'''
    Page 70-M — 1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4 7. d3 Qxh1
    ''': {
        "pgn": '''
1. e4 d5 2. exd5 Qxd5 3. Nc3 Qe5+ 4. Nge2 Nf6 5. g3 Ne4 6. Nxe4 Qxe4 7. d3 Qxh1''',
"next": [],
    },

    '''
    Page 80-A — 1. d4 e6
    ''': {
        "pgn": '''
1. d4 e6''',
"next": ['''
    Page 80-B — 1. d4 e6 2. Nc3
    '''],
    },

'''
    Page 80-B — 1. d4 e6 2. Nc3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3''',
"next": ['''
    Page 80-C — 1. d4 e6 2. Nc3 Nc6
    '''],
    },

'''
    Page 80-C — 1. d4 e6 2. Nc3 Nc6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6''',
"next": ['''
    Page 80-D — 1. d4 e6 2. Nc3 Nc6 3. Nf3
    '''],
    },

'''
    Page 80-D — 1. d4 e6 2. Nc3 Nc6 3. Nf3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3''',
"next": ['''
    Page 80-E — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6
    '''],
    },

'''
    Page 80-E — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6''',
"next": ['''
    Page 80-F — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4
    '''],
    },

'''
    Page 80-F — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4''',
"next": ['''
    Page 80-G — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6
    '''],
    },

'''
    Page 80-G — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6''',
"next": ['''
    Page 80-H — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3
    '''],
    },

'''
    Page 80-H — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3''',
"next": ['''
    Page 80-I — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O
    '''],
    },

'''
    Page 80-I — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O''',
"next": ['''
    Page 80-J — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3
    '''],
    },

'''
    Page 80-J — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3''',
"next": ['''
    Page 80-K — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5
    '''],
    },

'''
    Page 80-K — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5''',
"next": ['''
    Page 80-L — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5
    '''],
    },

'''
    Page 80-L — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5''',
"next": ['''
    Page 80-M — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5
    '''],
    },

'''
    Page 80-M — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5''',
"next": ['''
    Page 80-N — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5
    '''],
    },

'''
    Page 80-N — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5''',
"next": ['''
    Page 80-O — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5
    '''],
    },

'''
    Page 80-O — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5''',
"next": ['''
    Page 80-P — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3
    '''],
    },

'''
    Page 80-P — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3''',
"next": ['''
    Page 80-Q — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6
    '''],
    },

'''
    Page 80-Q — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6''',
"next": ['''
    Page 80-R — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O
    '''],
    },

'''
    Page 80-R — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O''',
"next": ['''
    Page 80-S — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6
    '''],
    },

'''
    Page 80-S — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6''',
"next": ['''
    Page 80-T — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3
    '''],
    },

'''
    Page 80-T — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3''',
"next": ['''
    Page 80-U — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5
    '''],
    },

'''
    Page 80-U — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5''',
"next": ['''
    Page 80-V — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4
    '''],
    },

'''
    Page 80-V — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4''',
"next": ['''
    Page 80-W — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3
    '''],
    },

'''
    Page 80-W — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3''',
"next": ['''
    Page 80-X — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3
    '''],
    },

'''
    Page 80-X — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3''',
"next": ['''
    Page 80-Y — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4
    '''],
    },

'''
    Page 80-Y — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4''',
"next": ['''
    Page 80-Z — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4
    '''],
    },

'''
    Page 80-Z — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4''',
"next": ['''
    Page 80-AA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5
    '''],
    },

'''
    Page 80-AA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5''',
"next": ['''
    Page 80-AB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5
    '''],
    },

'''
    Page 80-AB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5''',
"next": ['''
    Page 80-AC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5
    '''],
    },

'''
    Page 80-AC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5''',
"next": ['''
    Page 80-AD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5
    '''],
    },

'''
    Page 80-AD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5''',
"next": ['''
    Page 80-AE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6
    '''],
    },

'''
    Page 80-AE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6''',
"next": ['''
    Page 80-AF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6
    '''],
    },

'''
    Page 80-AF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6''',
"next": ['''
    Page 80-AG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4
    '''],
    },

'''
    Page 80-AG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4''',
"next": ['''
    Page 80-AH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1
    '''],
    },

'''
    Page 80-AH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1''',
"next": ['''
    Page 80-AI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5
    '''],
    },

'''
    Page 80-AI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5''',
"next": ['''
    Page 80-AJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4
    '''],
    },

'''
    Page 80-AJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4''',
"next": ['''
    Page 80-AK — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6
    '''],
    },

'''
    Page 80-AK — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6''',
"next": ['''
    Page 80-AL — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6
    '''],
    },

'''
    Page 80-AL — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6''',
"next": ['''
    Page 80-AM — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6
    '''],
    },

'''
    Page 80-AM — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6''',
"next": ['''
    Page 80-AN — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8
    '''],
    },

'''
    Page 80-AN — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8''',
"next": ['''
    Page 80-AO — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8
    '''],
    },

'''
    Page 80-AO — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8''',
"next": ['''
    Page 80-AP — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4
    '''],
    },

'''
    Page 80-AP — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4''',
"next": ['''
    Page 80-AQ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6
    '''],
    },

'''
    Page 80-AQ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6''',
"next": ['''
    Page 80-AR — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3
    '''],
    },

'''
    Page 80-AR — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3''',
"next": ['''
    Page 80-AS — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4
    '''],
    },

'''
    Page 80-AS — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4''',
"next": ['''
    Page 80-AT — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4
    '''],
    },

'''
    Page 80-AT — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4''',
"next": ['''
    Page 80-AU — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3
    '''],
    },

'''
    Page 80-AU — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3''',
"next": ['''
    Page 80-AV — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3
    '''],
    },

'''
    Page 80-AV — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3''',
"next": ['''
    Page 80-AW — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6
    '''],
    },

'''
    Page 80-AW — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6''',
"next": ['''
    Page 80-AX — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4
    '''],
    },

'''
    Page 80-AX — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4''',
"next": ['''
    Page 80-AY — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2
    '''],
    },

'''
    Page 80-AY — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2''',
"next": ['''
    Page 80-AZ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+
    '''],
    },

'''
    Page 80-AZ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+''',
"next": ['''
    Page 80-BA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7
    '''],
    },

'''
    Page 80-BA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7''',
"next": ['''
    Page 80-BB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+
    '''],
    },

'''
    Page 80-BB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+''',
"next": ['''
    Page 80-BC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8
    '''],
    },

'''
    Page 80-BC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8''',
"next": ['''
    Page 80-BD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6
    '''],
    },

'''
    Page 80-BD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6''',
"next": ['''
    Page 80-BE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2
    '''],
    },

'''
    Page 80-BE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2''',
"next": ['''
    Page 80-BF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4
    '''],
    },

'''
    Page 80-BF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4''',
"next": ['''
    Page 80-BG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1
    '''],
    },

'''
    Page 80-BG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1''',
"next": ['''
    Page 80-BH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1
    '''],
    },

'''
    Page 80-BH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1''',
"next": ['''
    Page 80-BI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+
    '''],
    },

'''
    Page 80-BI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+''',
"next": ['''
    Page 80-BJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1
    '''],
    },

'''
    Page 80-BJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1''',
"next": ['''
    Page 80-BK — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5
    '''],
    },

'''
    Page 80-BK — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5''',
"next": ['''
    Page 80-BL — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5
    '''],
    },

'''
    Page 80-BL — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5''',
"next": ['''
    Page 80-BM — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7
    '''],
    },

'''
    Page 80-BM — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7''',
"next": ['''
    Page 80-BN — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+
    '''],
    },

'''
    Page 80-BN — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+''',
"next": ['''
    Page 80-BO — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6
    '''],
    },

'''
    Page 80-BO — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6''',
"next": ['''
    Page 80-BP — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3
    '''],
    },

'''
    Page 80-BP — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3''',
"next": ['''
    Page 80-BQ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5
    '''],
    },

'''
    Page 80-BQ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5''',
"next": ['''
    Page 80-BR — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6
    '''],
    },

'''
    Page 80-BR — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6''',
"next": ['''
    Page 80-BS — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5
    '''],
    },

'''
    Page 80-BS — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5''',
"next": ['''
    Page 80-BT — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7
    '''],
    },

'''
    Page 80-BT — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7''',
"next": ['''
    Page 80-BU — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4
    '''],
    },

'''
    Page 80-BU — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4''',
"next": ['''
    Page 80-BV — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q
    '''],
    },

'''
    Page 80-BV — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q''',
"next": ['''
    Page 80-BW — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4
    '''],
    },

'''
    Page 80-BW — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4''',
"next": ['''
    Page 80-BX — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+
    '''],
    },

'''
    Page 80-BX — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+''',
"next": ['''
    Page 80-BY — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3
    '''],
    },

'''
    Page 80-BY — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3''',
"next": ['''
    Page 80-BZ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+
    '''],
    },

'''
    Page 80-BZ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+''',
"next": ['''
    Page 80-CA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4
    '''],
    },

'''
    Page 80-CA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4''',
"next": ['''
    Page 80-CB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+
    '''],
    },

'''
    Page 80-CB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+''',
"next": ['''
    Page 80-CC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4
    '''],
    },

'''
    Page 80-CC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4''',
"next": ['''
    Page 80-CD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2
    '''],
    },

'''
    Page 80-CD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2''',
"next": ['''
    Page 80-CE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3
    '''],
    },

'''
    Page 80-CE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3''',
"next": ['''
    Page 80-CF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+
    '''],
    },

'''
    Page 80-CF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+''',
"next": ['''
    Page 80-CG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4
    '''],
    },

'''
    Page 80-CG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4''',
"next": ['''
    Page 80-CH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+
    '''],
    },

'''
    Page 80-CH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+''',
"next": ['''
    Page 80-CI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4
    '''],
    },

'''
    Page 80-CI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4''',
"next": ['''
    Page 80-CJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+
    '''],
    },

'''
    Page 80-CJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+''',
"next": ['''
    Page 80-CK — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5
    '''],
    },

'''
    Page 80-CK — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5''',
"next": ['''
    Page 80-CL — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3
    '''],
    },

'''
    Page 80-CL — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3''',
"next": ['''
    Page 80-CM — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4
    '''],
    },

'''
    Page 80-CM — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4''',
"next": ['''
    Page 80-CN — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5
    '''],
    },

'''
    Page 80-CN — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5''',
"next": ['''
    Page 80-CO — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5
    '''],
    },

'''
    Page 80-CO — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5''',
"next": ['''
    Page 80-CP — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+
    '''],
    },

'''
    Page 80-CP — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+''',
"next": ['''
    Page 80-CQ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5
    '''],
    },

'''
    Page 80-CQ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5''',
"next": ['''
    Page 80-CR — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+
    '''],
    },

'''
    Page 80-CR — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+''',
"next": ['''
    Page 80-CS — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4
    '''],
    },

'''
    Page 80-CS — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4''',
"next": ['''
    Page 80-CT — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+
    '''],
    },

'''
    Page 80-CT — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+''',
"next": ['''
    Page 80-CU — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5
    '''],
    },

'''
    Page 80-CU — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5''',
"next": ['''
    Page 80-CV — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+
    '''],
    },

'''
    Page 80-CV — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+''',
"next": ['''
    Page 80-CW — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5
    '''],
    },

'''
    Page 80-CW — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5''',
"next": ['''
    Page 80-CX — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+
    '''],
    },

'''
    Page 80-CX — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+''',
"next": ['''
    Page 80-CY — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5
    '''],
    },

'''
    Page 80-CY — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5''',
"next": ['''
    Page 80-CZ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+
    '''],
    },

'''
    Page 80-CZ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+''',
"next": ['''
    Page 80-DA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4
    '''],
    },

'''
    Page 80-DA — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4''',
"next": ['''
    Page 80-DB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+
    '''],
    },

'''
    Page 80-DB — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+''',
"next": ['''
    Page 80-DC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5
    '''],
    },

'''
    Page 80-DC — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5''',
"next": ['''
    Page 80-DD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3
    '''],
    },

'''
    Page 80-DD — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3''',
"next": ['''
    Page 80-DE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6
    '''],
    },

'''
    Page 80-DE — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6''',
"next": ['''
    Page 80-DF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4
    '''],
    },

'''
    Page 80-DF — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4''',
"next": ['''
    Page 80-DG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5
    '''],
    },

'''
    Page 80-DG — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5''',
"next": ['''
    Page 80-DH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+
    '''],
    },

'''
    Page 80-DH — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+''',
"next": ['''
    Page 80-DI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+ Kf4
    '''],
    },

'''
    Page 80-DI — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+ Kf4
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+ Kf4''',
"next": ['''
    Page 80-DJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+ Kf4 58. Qf5#
    '''],
    },

'''
    Page 80-DJ — 1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+ Kf4 58. Qf5#
    ''': {
        "pgn": '''
1. d4 e6 2. Nc3 Nc6 3. Nf3 Nf6 4. e4 Bd6 5. Be3 O-O 6. Bd3 e5 7. Nxe5 Nxe5 8. dxe5 Bxe5 9. Qf3 h6 10. O-O c6 11. Qh3 d5 12. a4 Bxh3 13. gxh3 dxe4 14. Bc4 b5 15. axb5 cxb5 16. Bxb5 a6 17. Bc6 Bd4 18. Rad1 a5 19. Bxd4 Ra6 20. Bxf6 gxf6 21. Rxd8 Rxd8 22. Bxe4 Rad6 23. Bf3 a4 24. h4 a3 25. bxa3 Rc6 26. Ne4 Rxc2 27. Nxf6+ Kg7 28. Nh5+ Kf8 29. Nf6 Rcd2 30. a4 Rd1 31. Rxd1 Rxd1+ 32. Bxd1 h5 33. a5 Ke7 34. Nd5+ Kd6 35. Nc3 f5 36. a6 Ke5 37. a7 f4 38. a8=Q Kd4 39. Ne2+ Kd3 40. Nc1+ Kd4 41. Qd8+ Ke4 42. Be2 f3 43. Qe7+ Kd4 44. Qd6+ Ke4 45. Qd3+ Ke5 46. Bxf3 Kf4 47. Bxh5 Ke5 48. Qe3+ Kd5 49. Bf3+ Kc4 50. Be2+ Kd5 51. Qd3+ Ke5 52. Qc3+ Kd5 53. Qb3+ Ke4 54. Qc4+ Ke5 55. Bf3 Kd6 56. Be4 Ke5 57. Qd5+ Kf4 58. Qf5#''',
"next": [],
    },

    # Game 90: https://www.chess.com/game/live/142415861588

    '''
    Page 90-A — 1. e4 e5
    ''': {
        "pgn": '''
1. e4 e5''',
"next": ['''
    Page 90-B — 1. e4 e5 2. Nc3
    '''],
    },

'''
    Page 90-B — 1. e4 e5 2. Nc3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3''',
"next": ['''
    Page 90-C — 1. e4 e5 2. Nc3 Bb4
    '''],
    },

'''
    Page 90-C — 1. e4 e5 2. Nc3 Bb4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4''',
"next": ['''
    Page 90-D — 1. e4 e5 2. Nc3 Bb4 3. a3
    '''],
    },

'''
    Page 90-D — 1. e4 e5 2. Nc3 Bb4 3. a3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3''',
"next": ['''
    Page 90-E — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5
    '''],
    },

'''
    Page 90-E — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5''',
"next": ['''
    Page 90-F — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4
    '''],
    },

'''
    Page 90-F — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4''',
"next": ['''
    Page 90-G — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6
    '''],
    },

'''
    Page 90-G — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6''',
"next": ['''
    Page 90-H — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3
    '''],
    },

'''
    Page 90-H — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3''',
"next": ['''
    Page 90-I — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4
    '''],
    },

'''
    Page 90-I — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4''',
"next": ['''
    Page 90-J — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3
    '''],
    },

'''
    Page 90-J — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3''',
"next": ['''
    Page 90-K — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6
    '''],
    },

'''
    Page 90-K — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6''',
"next": ['''
    Page 90-L — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O
    '''],
    },

'''
    Page 90-L — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O''',
"next": ['''
    Page 90-M — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O
    '''],
    },

'''
    Page 90-M — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O''',
"next": ['''
    Page 90-N — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3
    '''],
    },

'''
    Page 90-N — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3''',
"next": ['''
    Page 90-O — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6
    '''],
    },

'''
    Page 90-O — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6''',
"next": ['''
    Page 90-P — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4
    '''],
    },

'''
    Page 90-P — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4''',
"next": ['''
    Page 90-Q — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4
    '''],
    },

'''
    Page 90-Q — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4''',
"next": ['''
    Page 90-R — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4
    '''],
    },

'''
    Page 90-R — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4''',
"next": ['''
    Page 90-S — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4
    '''],
    },

'''
    Page 90-S — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4''',
"next": ['''
    Page 90-T — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4
    '''],
    },

'''
    Page 90-T — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4''',
"next": ['''
    Page 90-U — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5
    '''],
    },

'''
    Page 90-U — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5''',
"next": ['''
    Page 90-V — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5
    '''],
    },

'''
    Page 90-V — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5''',
"next": ['''
    Page 90-W — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5
    '''],
    },

'''
    Page 90-W — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5''',
"next": ['''
    Page 90-X — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3
    '''],
    },

'''
    Page 90-X — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3''',
"next": ['''
    Page 90-Y — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6
    '''],
    },

'''
    Page 90-Y — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6''',
"next": ['''
    Page 90-Z — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5
    '''],
    },

'''
    Page 90-Z — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5''',
"next": ['''
    Page 90-AA — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5
    '''],
    },

'''
    Page 90-AA — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5''',
"next": ['''
    Page 90-AB — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6
    '''],
    },

'''
    Page 90-AB — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6''',
"next": ['''
    Page 90-AC — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4
    '''],
    },

'''
    Page 90-AC — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4''',
"next": ['''
    Page 90-AD — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3
    '''],
    },

'''
    Page 90-AD — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3''',
"next": ['''
    Page 90-AE — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6
    '''],
    },

'''
    Page 90-AE — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6''',
"next": ['''
    Page 90-AF — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7
    '''],
    },

'''
    Page 90-AF — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7''',
"next": ['''
    Page 90-AG — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7
    '''],
    },

'''
    Page 90-AG — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7''',
"next": ['''
    Page 90-AH — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3
    '''],
    },

'''
    Page 90-AH — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3''',
"next": ['''
    Page 90-AI — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8
    '''],
    },

'''
    Page 90-AI — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8''',
"next": ['''
    Page 90-AJ — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4
    '''],
    },

'''
    Page 90-AJ — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4''',
"next": ['''
    Page 90-AK — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4
    '''],
    },

'''
    Page 90-AK — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4''',
"next": ['''
    Page 90-AL — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1
    '''],
    },

'''
    Page 90-AL — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1''',
"next": ['''
    Page 90-AM — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2
    '''],
    },

'''
    Page 90-AM — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2''',
"next": ['''
    Page 90-AN — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6
    '''],
    },

'''
    Page 90-AN — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6''',
"next": ['''
    Page 90-AO — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6
    '''],
    },

'''
    Page 90-AO — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6''',
"next": ['''
    Page 90-AP — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6 22. Rad1
    '''],
    },

'''
    Page 90-AP — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6 22. Rad1
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6 22. Rad1''',
"next": ['''
    Page 90-AQ — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6 22. Rad1 Rxc2
    '''],
    },

'''
    Page 90-AQ — 1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6 22. Rad1 Rxc2
    ''': {
        "pgn": '''
1. e4 e5 2. Nc3 Bb4 3. a3 Ba5 4. Bc4 Nf6 5. Nf3 Ng4 6. h3 Nf6 7. O-O O-O 8. d3 Nc6 9. d4 exd4 10. Nxd4 Nxd4 11. Qxd4 d5 12. exd5 Bf5 13. Bd3 b6 14. Bxf5 c5 15. dxc6 Qxd4 16. Be3 Qd6 17. c7 Qxc7 18. g3 Rad8 19. Bf4 Qc4 20. Rfe1 Rd2 21. Be6 Qc6 22. Rad1 Rxc2''',
"next": [],
    },

    # Game 100: https://www.chess.com/game/142416629166

    '''
    Page 100-A — 1. e4 d6
    ''': {
        "pgn": '''
1. e4 d6''',
"next": ['''
    Page 100-B — 1. e4 d6 2. Nf3
    '''],
    },

'''
    Page 100-B — 1. e4 d6 2. Nf3
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3''',
"next": ['''
    Page 100-C — 1. e4 d6 2. Nf3 Nf6
    '''],
    },

'''
    Page 100-C — 1. e4 d6 2. Nf3 Nf6
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6''',
"next": ['''
    Page 100-D — 1. e4 d6 2. Nf3 Nf6 3. Nc3
    '''],
    },

'''
    Page 100-D — 1. e4 d6 2. Nf3 Nf6 3. Nc3
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3''',
"next": ['''
    Page 100-E — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6
    '''],
    },

'''
    Page 100-E — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6''',
"next": ['''
    Page 100-F — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4
    '''],
    },

'''
    Page 100-F — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4''',
"next": ['''
    Page 100-G — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6
    '''],
    },

'''
    Page 100-G — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6''',
"next": ['''
    Page 100-H — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3
    '''],
    },

'''
    Page 100-H — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3''',
"next": ['''
    Page 100-I — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4
    '''],
    },

'''
    Page 100-I — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4''',
"next": ['''
    Page 100-J — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4
    '''],
    },

'''
    Page 100-J — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4''',
"next": ['''
    Page 100-K — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7
    '''],
    },

'''
    Page 100-K — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7''',
"next": ['''
    Page 100-L — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O
    '''],
    },

'''
    Page 100-L — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O''',
"next": ['''
    Page 100-M — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7
    '''],
    },

'''
    Page 100-M — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7''',
"next": ['''
    Page 100-N — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4
    '''],
    },

'''
    Page 100-N — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4''',
"next": ['''
    Page 100-O — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6
    '''],
    },

'''
    Page 100-O — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6''',
"next": ['''
    Page 100-P — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6 9. Qd4
    '''],
    },

'''
    Page 100-P — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6 9. Qd4
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6 9. Qd4''',
"next": ['''
    Page 100-Q — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6 9. Qd4 Bg7
    '''],
    },

'''
    Page 100-Q — 1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6 9. Qd4 Bg7
    ''': {
        "pgn": '''
1. e4 d6 2. Nf3 Nf6 3. Nc3 c6 4. Bc4 Be6 5. d3 Bxc4 6. dxc4 Nbd7 7. O-O Qc7 8. Bf4 g6 9. Qd4 Bg7''',
"next": [],
    },

# Game 110: https://www.chess.com/game/142417181704

'''
    Page 110-A — 1. e4 e5
    ''': {
        "pgn": '''
1. e4 e5''',
"next": ['''
    Page 110-B — 1. e4 e5 2. Nf3
    '''],
    },

'''
    Page 110-B — 1. e4 e5 2. Nf3
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3''',
"next": ['''
    Page 110-C — 1. e4 e5 2. Nf3 f6
    '''],
    },

'''
    Page 110-C — 1. e4 e5 2. Nf3 f6
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 f6''',
"next": ['''
    Page 110-D — 1. e4 e5 2. Nf3 f6 3. Bc4
    '''],
    },

'''
    Page 110-D — 1. e4 e5 2. Nf3 f6 3. Bc4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 f6 3. Bc4''',
"next": ['''
    Page 110-E — 1. e4 e5 2. Nf3 f6 3. Bc4 d5
    '''],
    },

'''
    Page 110-E — 1. e4 e5 2. Nf3 f6 3. Bc4 d5
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 f6 3. Bc4 d5''',
"next": ['''
    Page 110-F — 1. e4 e5 2. Nf3 f6 3. Bc4 d5 4. Bb3
    '''],
    },

'''
    Page 110-F — 1. e4 e5 2. Nf3 f6 3. Bc4 d5 4. Bb3
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 f6 3. Bc4 d5 4. Bb3''',
"next": ['''
    Page 110-G — 1. e4 e5 2. Nf3 f6 3. Bc4 d5 4. Bb3 dxe4
    '''],
    },

'''
    Page 110-G — 1. e4 e5 2. Nf3 f6 3. Bc4 d5 4. Bb3 dxe4
    ''': {
        "pgn": '''
1. e4 e5 2. Nf3 f6 3. Bc4 d5 4. Bb3 dxe4''',
"next": [],
    },

    # Game 120: https://www.chess.com/game/live/142616968892

    '''
    Page 120-A — 1. e3 e5
    ''': {
        "pgn": '''
1. e3 e5''',
"next": ['''
    Page 120-B — 1. e3 e5 2. Nc3
    '''],
    },

'''
    Page 120-B — 1. e3 e5 2. Nc3
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3''',
"next": ['''
    Page 120-C — 1. e3 e5 2. Nc3 Nf6
    '''],
    },

'''
    Page 120-C — 1. e3 e5 2. Nc3 Nf6
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6''',
"next": ['''
    Page 120-D — 1. e3 e5 2. Nc3 Nf6 3. Bd3
    '''],
    },

'''
    Page 120-D — 1. e3 e5 2. Nc3 Nf6 3. Bd3
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3''',
"next": ['''
    Page 120-E — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5
    '''],
    },

'''
    Page 120-E — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5''',
"next": ['''
    Page 120-F — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3
    '''],
    },

'''
    Page 120-F — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3''',
"next": ['''
    Page 120-G — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O
    '''],
    },

'''
    Page 120-G — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O''',
"next": ['''
    Page 120-H — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4
    '''],
    },

'''
    Page 120-H — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4''',
"next": ['''
    Page 120-I — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6
    '''],
    },

'''
    Page 120-I — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6''',
"next": ['''
    Page 120-J — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3
    '''],
    },

'''
    Page 120-J — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3''',
"next": ['''
    Page 120-K — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5
    '''],
    },

'''
    Page 120-K — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5''',
"next": ['''
    Page 120-L — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2
    '''],
    },

'''
    Page 120-L — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2''',
"next": ['''
    Page 120-M — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4
    '''],
    },

'''
    Page 120-M — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4''',
"next": ['''
    Page 120-N — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3
    '''],
    },

'''
    Page 120-N — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3''',
"next": ['''
    Page 120-O — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7
    '''],
    },

'''
    Page 120-O — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7''',
"next": ['''
    Page 120-P — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5
    '''],
    },

'''
    Page 120-P — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5''',
"next": ['''
    Page 120-Q — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6
    '''],
    },

'''
    Page 120-Q — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6''',
"next": ['''
    Page 120-R — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5
    '''],
    },

'''
    Page 120-R — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5''',
"next": ['''
    Page 120-S — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6
    '''],
    },

'''
    Page 120-S — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6''',
"next": ['''
    Page 120-T — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4
    '''],
    },

'''
    Page 120-T — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4''',
"next": ['''
    Page 120-U — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4
    '''],
    },

'''
    Page 120-U — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4''',
"next": ['''
    Page 120-V — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4
    '''],
    },

'''
    Page 120-V — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4''',
"next": ['''
    Page 120-W — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4
    '''],
    },

'''
    Page 120-W — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4''',
"next": ['''
    Page 120-X — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4
    '''],
    },

'''
    Page 120-X — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4''',
"next": ['''
    Page 120-Y — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4
    '''],
    },

'''
    Page 120-Y — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4''',
"next": ['''
    Page 120-Z — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3
    '''],
    },

'''
    Page 120-Z — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3''',
"next": ['''
    Page 120-AA — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+
    '''],
    },

'''
    Page 120-AA — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+''',
"next": ['''
    Page 120-AB — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2
    '''],
    },

'''
    Page 120-AB — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2''',
"next": ['''
    Page 120-AC — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+
    '''],
    },

'''
    Page 120-AC — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+''',
"next": ['''
    Page 120-AD — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1
    '''],
    },

'''
    Page 120-AD — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1''',
"next": ['''
    Page 120-AE — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8
    '''],
    },

'''
    Page 120-AE — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8''',
"next": ['''
    Page 120-AF — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2
    '''],
    },

'''
    Page 120-AF — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2''',
"next": ['''
    Page 120-AG — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2
    '''],
    },

'''
    Page 120-AG — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2''',
"next": ['''
    Page 120-AH — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3
    '''],
    },

'''
    Page 120-AH — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3''',
"next": ['''
    Page 120-AI — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+
    '''],
    },

'''
    Page 120-AI — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+''',
"next": ['''
    Page 120-AJ — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1
    '''],
    },

'''
    Page 120-AJ — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1''',
"next": ['''
    Page 120-AK — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+
    '''],
    },

'''
    Page 120-AK — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+''',
"next": ['''
    Page 120-AL — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+ 20. Kd1
    '''],
    },

'''
    Page 120-AL — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+ 20. Kd1
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+ 20. Kd1''',
"next": ['''
    Page 120-AM — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+ 20. Kd1 Qe2#
    '''],
    },

'''
    Page 120-AM — 1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+ 20. Kd1 Qe2#
    ''': {
        "pgn": '''
1. e3 e5 2. Nc3 Nf6 3. Bd3 Bc5 4. a3 O-O 5. b4 Bb6 6. Qf3 d5 7. Nge2 Bg4 8. Qg3 Qd7 9. Qxe5 Nc6 10. Qg5 h6 11. Qh4 d4 12. exd4 Nxd4 13. Nxd4 Bxd4 14. Qg3 Rfe8+ 15. Be2 Rxe2+ 16. Kf1 Rae8 17. Nxe2 Rxe2 18. f3 Rf2+ 19. Ke1 Qe7+ 20. Kd1 Qe2#''',
"next": [],
    },

    '''
    Page 130-A — 1. c4 e5''': {
        "pgn": '''1. c4 e5''',
"next": [],
    },








}
