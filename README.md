
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Paper](https://img.shields.io/badge/Paper-COLM%202026-blue.svg)]()

This repository contains the official experimental payload, scripts, and evaluation results for the paper **"Beyond Preset Identities: How Agents Form Stances and Boundaries in Generative Societies"**.

> **Important Note:** This repository serves as the **Data & Configuration Payload**. The simulation environment is powered by the **CMASE framework**. To reproduce our experiments, you need to apply these files to the CMASE core engine.

## Repository Structure

Our files are organized as follows (Note: `e2` denotes Study 1, and `e3` denotes Study 2 in our codebase):

* **Directories:**
  * `env file/`: Contains the environment records, logs, and state snapshots for the simulations.
  * `maps/`: Contains the spatial configurations for the virtual environments (e.g., the virtual cafe).

* **Execution Scripts:**
  * `start_e2.py`: Main entry script to run the simulation for Study 1 (Controlled Intervention).
  * `start_e3.py`: Main entry script to run the simulation for Study 2 (Virtual Ethnography & Reconstruction).

* **Analysis & Evaluation Scripts:**
  * `interview_e2.py` & `interview_e2_compare.py`: Scripts used to conduct and compare post-simulation interviews with agents in Study 1.
  * `statistics_e2.py` & `statistics_e2_multi.py`: Scripts to calculate the quantitative metrics proposed in the paper (e.g., Innate Value Bias, Persuasion Sensitivity, TAD Rate).

* **Results Data:**
  * `All_Models_Comparison_Result.csv`: The final aggregated table comparing the performance of GPT-4o, Gemini, Llama, and Qwen.
  * `Strict_3Dim_Analysis.csv`: Detailed multi-dimensional evaluation metrics.

## Quick Start: How to Reproduce

To run these experiments, please follow the integration steps below:

### Step 1: Clone the Core Engine (CMASE)
First, clone the CMASE framework repository.

```bash
git clone https://github.com/armihia/CMASE.git
cd CMASE

Step 2: Apply the Experimental Payload
Clone this repository and copy all its contents directly into the root directory of the CMASE engine。

Step 3: Run the Simulations
Navigate back to the CMASE directory and execute the specific study scripts:

Bash
cd CMASE

# To run Study 1:
python start_e2.py

# To calculate metrics for Study 1:
python statistics_e2.py

# To run Study 2:
python start_e3.py

License
The data and configurations in this repository are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
