# Exercise Reminder App

An application designed to encourage physical activity by reminding users to take breaks and perform exercises. It provides exercise details, displays images, and counts down the time for each exercise.

## Description

This program is built in Python using the Tkinter library. It offers the following features:

- **Start Screen**: A welcoming screen that lets users begin their exercise session.
- **Exercise Management**: Displays exercises, their descriptions, duration, and repetitions.
- **Image Support**: Shows a thumbnail image of the current exercise.
- **Timer**: A countdown timer for each exercise.
- **Pause and Resume**: Allows pausing and resuming the exercise session.
- **Reminder**: Users can set a custom interval to remind them to continue the exercises later.

## Features

1. **Dynamic Exercise Cycle**:
   - Automatically cycles through a list of exercises (`exercises` module).
   - Displays exercise name, duration, and repetitions.

2. **Interactive Buttons**:
   - **Pause**: Pauses the current exercise session.
   - **Resume**: Resumes the paused session.
   - **Remind Me Later**: Allows the user to set a custom reminder interval.

3. **Image Support**:
   - Displays images for exercises (requires valid image paths in the `exercises` module).

## Installation

1. Clone the repository or download the source files.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt

## Run the application:
    python app.py