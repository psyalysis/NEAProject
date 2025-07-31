# Gyro-skate Project Structure

## Overview
Gyro-skate is a skateboarding game that uses iPhone gyroscope data via OSC to detect and score skateboarding tricks in real-time.

## File Structure

```
Gyroskate/
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── main.py                            # Main game entry point
├── config.py                          # Configuration settings
├── 
├── core/                              # Core game modules
│   ├── __init__.py
│   ├── osc_handler.py                 # OSC communication (existing)
│   ├── game_state.py                  # Game state management
│   ├── trick_detector.py              # Trick detection algorithms
│   ├── scoring_system.py              # Points and scoring logic
│   └── board_controller.py            # 3D board physics and movement
│   
├── game/                              # Game logic modules
│   ├── __init__.py
│   ├── player_manager.py              # Player state and progression
│   ├── game_modes.py                  # Different game modes (Copycat, Speed run)
│   ├── session_manager.py             # Session tracking and statistics
│   └── leaderboard.py                 # Leaderboard system
│   
├── ui/                                # User interface
│   ├── __init__.py
│   ├── game_display.py                # Main game screen
│   ├── menu_system.py                 # Menu and navigation
│   ├── feedback_system.py             # Visual and audio feedback
│   ├── trick_animations.py            # Trick demonstration animations
│   └── assets/                        # UI assets
│       ├── images/
│       ├── sounds/
│       └── fonts/
│   
├── data/                              # Data management
│   ├── __init__.py
│   ├── trick_profiles.py              # Predefined trick rotation patterns
│   ├── data_logger.py                 # Session data logging
│   ├── statistics.py                  # Player statistics tracking
│   └── saved_data/                    # Saved game data
│       ├── sessions/
│       ├── leaderboards/
│       └── player_profiles/
│   
├── utils/                             # Utility functions
│   ├── __init__.py
│   ├── math_utils.py                  # Mathematical calculations
│   ├── validation.py                  # Input validation
│   ├── constants.py                   # Game constants
│   └── helpers.py                     # Helper functions
│   
├── tests/                             # Testing modules
│   ├── __init__.py
│   ├── test_trick_detection.py        # Trick detection tests
│   ├── test_osc_communication.py      # OSC communication tests
│   ├── test_scoring.py                # Scoring system tests
│   └── test_integration.py            # Integration tests
│   
├── web/                               # Web interface (if needed)
│   ├── index.html                     # Main web page
│   ├── styles.css                     # Web styling
│   ├── script.js                      # Web functionality
│   └── assets/                        # Web assets
│   
├── docs/                              # Documentation
│   ├── design_document.md             # Detailed design documentation
│   ├── testing_plan.md                # Testing strategy
│   ├── user_manual.md                 # User instructions
│   └── technical_specs.md             # Technical specifications
│   
└── resources/                         # Additional resources
    ├── trick_database.json            # Database of skateboarding tricks
    ├── sound_effects/                 # Audio files
    ├── graphics/                      # Graphics and images
    └── tutorials/                     # Tutorial materials
```

## Key Components

### Core Modules
- **OSC Handler**: Receives gyroscope data from iPhone
- **Game State**: Manages connection, ready, airborne, landing states
- **Trick Detector**: Analyzes rotation patterns to identify tricks
- **Scoring System**: Calculates points based on trick execution
- **Board Controller**: Handles 3D board physics and movement

### Game Logic
- **Player Manager**: Tracks player state and progression
- **Game Modes**: Different gameplay modes (Copycat, Speed run)
- **Session Manager**: Handles game sessions and statistics
- **Leaderboard**: Competitive scoring system

### User Interface
- **Game Display**: Main game screen with 3D board visualization
- **Menu System**: Navigation and settings
- **Feedback System**: Visual and audio feedback for tricks
- **Trick Animations**: Demonstrations of correct trick movements

### Data Management
- **Trick Profiles**: Predefined rotation patterns for each trick
- **Data Logger**: Records session data for analysis
- **Statistics**: Player performance tracking

## Development Phases

### Phase 1: Foundation
- OSC communication setup ✅
- Basic game state management
- Simple trick detection

### Phase 2: Core Gameplay
- 3D board visualization
- Trick detection algorithms
- Basic scoring system

### Phase 3: Polish
- User interface
- Audio/visual feedback
- Game modes

### Phase 4: Testing & Refinement
- Comprehensive testing
- Performance optimization
- User feedback integration 