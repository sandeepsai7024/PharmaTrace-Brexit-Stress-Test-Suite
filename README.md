# PharmaTrace-Brexit-Stress-Test-Suite

**Predictive Supply Chain Digital Twin for UK Pharmaceutical Resilience**

## 📌 Project Overview
PharmaTrace is a tech-forward "Digital Twin" designed to model and mitigate supply chain friction across the UK-EU trade corridor. In the UK pharmaceutical sector, logistics delays aren't just a business cost—they represent a significant risk to patient safety for life-saving medications.

This project simulates 2,000+ shipments of critical SKUs (Insulin, Oncology, Antibiotics) to identify vulnerabilities in the "Last Mile" of the UK border.

## 🛠️ The Tech Stack
* **Data Engineering:** Python (Pandas/NumPy) modeling lead times and customs delays using **Poisson** and **Normal distributions**.
* **Machine Learning:** **Random Forest Classifier** trained to predict "Stock-Out" events (1=Failure, 0=Success).
* **BI Architecture:** **Power BI Command Center** featuring real-time risk probability gauges and automated "Red Alert" exception reporting.
* **DAX Logic:** Custom measures for "Patient Days Remaining" and "Supply Gap Analysis."

## 🧠 Data Science & Predictive Logic
To move beyond static reporting, I modeled "Border Friction" as a random variable to account for the chaos of real-world logistics:

1. **Border Congestion:** Modeled using a **Poisson Distribution** ($\lambda=3$), representing discrete random customs events.
2. **Lead Times:** Modeled using a **Normal Distribution** ($\mu=7, \sigma=2$), capturing standard transit variability.

### Model Performance
The Random Forest model prioritizes **Recall** to ensure no critical stock-out event is missed.
* **Accuracy:** 94%
* **Recall (Sensitivity):** 91% (Critical for patient safety)
* **Top Risk Driver:** Storage Type (Cold Chain vs. Ambient).



## 📊 Dashboard Features
* **Sentinel Gauge:** Real-time monitoring of "Risk Probability."
* **Critical System Alert:** Automated status labeling that triggers a "RED ALERT" when the probability exceeds 15%.
* **Route Friction Heatmap:** Visualizes the bottleneck at Dover-Calais vs. Heathrow Air Freight.



## 📂 Repository Structure
* `generator.py`: The Python data engine and ML logic.
* `PharmaTrace_ML_Data.csv`: The generated dataset.
* `PharmaTrace_Suite.pbix`: The Power BI dashboard source file.
* `dashboard_preview.png`: High-resolution dashboard screenshot.
* `README.md`: Technical documentation.

## 🚀 How to Use
1. Clone the repository.
2. Run `generator.py` to see the data creation process.
3. Open `PharmaTrace_Suite.pbix` in Power BI Desktop to interact with the Stress-Test sliders.

## 📊 Model Performance & Data Science Logic

To transition from descriptive analytics to predictive insights, **PharmaTrace** utilizes a **Random Forest Classifier**. This model was trained on 2,000 simulated pharmaceutical shipments to predict the binary outcome of a **Stock-Out event** ($1$ = Failure, $0$ = Success).

### 1. The Probability Distributions
Unlike static models, this suite accounts for the "chaos" of real-world logistics by using stochastic modeling:

* **Border Congestion:** Modeled using a **Poisson Distribution** ($\lambda=3$), representing the discrete number of random customs events occurring in a fixed interval.
* **Lead Times:** Modeled using a **Normal Distribution** ($\mu=7, \sigma=2$), capturing the standard variability in transit across the UK-EU corridor.



### 2. Evaluation Metrics
In the context of pharmaceutical supply chains, **Recall** is prioritized over **Precision**. From a clinical safety perspective, it is preferable to have a "False Alarm" (triggering over-preparation) than to miss a "True Positive" (a life-saving drug actually reaching a stock-out state).

| Metric | Score | Significance |
| :--- | :--- | :--- |
| **Accuracy** | 94% | Overall correctness of the model predictions. |
| **Recall (Sensitivity)** | 91% | Ability to identify all actual Stock-Out events (Critical for patient safety). |
| **Precision** | 88% | Reliability of the "Red Alert" when triggered. |



### 3. Feature Importance
The Random Forest model identified the following primary drivers of supply chain friction:
1. **Storage Requirements (Cold Chain):** Highest weight due to low tolerance for transit delays.
2. **Route Selection:** Dover-Calais exhibits significantly higher variance than Air Freight.
3. **Customs Density:** Impact of random inspections on total lead time.

*Created by sai sandeep chintala - Data Science Portfolio Project*
