# Mood-Based Music Generator

This demo project creates a simple application that generates three audio files based on a predefined audio file and descriptions. This project leverages NVIDIA GPU.

## Prerequisites

1. **NVIDIA GPU**: Ensure that you have an NVIDIA GPU installed on your machine.
2. **NVIDIA Docker**: Install NVIDIA Docker following the instructions [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/mexxik/audiocraft-demo
cd audiocraft-demo
```

### Step 2: Build the Docker Image

Run the following command to build the Docker image:

```bash
./build.sh
```

###Step 3: Run the Application

Use the following command to run the application:

```bash
./run.sh
```

## Output

The generated audio files will be saved in the assets folder.