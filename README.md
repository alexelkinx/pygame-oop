# Space Invaders

This is a simple object-oriented 2D arcade game built with Python and Pygame. The player controls a spaceship that can move left and right and shoot bullets to destroy descending alien ships.

---

## Technologies Used

- Python 3.x
- Pygame

---

## Directory Structure

```
space-invaders/
├── alien.py
├── bullet.py
├── events.py
├── explosion.py
├── images/
│   ├── alien.png
│   ├── regularExplosion00.png
│   ├── ...
│   └── starfield.png
├── main.py
├── README.md
├── requirements.txt
├── settings.py
├── ship.py
├── stats.py
└── UI.py
```

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Pip for Python package management

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd space-invaders
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the game:

   ```bash
   python main.py
   ```

---

## Gameplay

- Use arrow keys to move the spaceship left and right.
- Press spacebar to shoot bullets upward.
- Destroy all aliens before they reach your ship.
- Explosions are shown upon hits.
