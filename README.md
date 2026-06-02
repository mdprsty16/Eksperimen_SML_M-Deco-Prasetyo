# Eksperimen Machine Learning - Insurance Dataset Preprocessing

![Preprocessing Workflow](https://github.com/M-Deco-Prasetyo/Eksperimen_SML_M-Deco-Prasetyo/actions/workflows/preprocessing.yml/badge.svg)
![Advanced Preprocessing](https://github.com/M-Deco-Prasetyo/Eksperimen_SML_M-Deco-Prasetyo/actions/workflows/advanced-preprocessing.yml/badge.svg)

## 📋 Project Structure

```
Eksperimen_SML_M-Deco-Prasetyo/
├── .github/
│   └── workflows/
│       ├── preprocessing.yml              # Basic automated preprocessing
│       └── advanced-preprocessing.yml     # Advanced workflow with releases
├── insurance_raw/
│   └── insurance.csv                      # Raw dataset (1,338 records)
├── preprocessing/
│   ├── Template_Eksperimen_MSML.ipynb    # Experimentation notebook
│   ├── automate_M-Deco-Prasetyo.py       # Automation script
│   └── insurance_preprocessing/           # Output folder
│       ├── insurance_preprocessed.csv     # Preprocessed dataset
│       ├── preprocessing_report.txt       # Processing report
│       └── backups/                       # Versioned backups
├── requirements.txt                       # Python dependencies
└── README.md                              # This file
```

## ✅ Completion Status - ADVANCE (4 pts)

### ✓ Basic (2 pts) - Completed
- [x] Manual experimentation with notebook
- [x] Data loading from CSV
- [x] Exploratory Data Analysis (EDA)
- [x] Data preprocessing steps

### ✓ Skilled (3 pts) - Completed
- [x] Created `automate_M-Deco-Prasetyo.py` with full preprocessing functions
- [x] Generated `insurance_preprocessing/` output folder with:
  - `insurance_preprocessed.csv` (1,337 processed records)
  - `preprocessing_report.txt` (detailed report)

### ✓ Advance (4 pts) - Completed
- [x] GitHub Actions workflows for automated preprocessing
- [x] Dual workflow setup:
  - **Basic Pipeline**: Automatic triggers on code changes
  - **Advanced Pipeline**: With data versioning and releases
- [x] Automatic dataset updates on repository changes
- [x] Artifact preservation and downloads

## 🚀 GitHub Actions Setup

### Workflows Available

#### 1. **Preprocessing Pipeline** (Basic)
- **File**: `.github/workflows/preprocessing.yml`
- **Triggers**: 
  - Push to `main` (when `insurance_raw/` or script changes)
  - Manual trigger via GitHub UI
  - Pull requests to `main`
- **Output**: Preprocessed CSV + Report + Artifacts

#### 2. **Advanced Preprocessing** (Advanced)
- **File**: `.github/workflows/advanced-preprocessing.yml`
- **Features**:
  - Data quality validation
  - Versioned backups with timestamps
  - Optional GitHub Release creation
  - Extended artifact retention (90 days)
  - Comprehensive execution summary

### Running Workflows

#### Automatic (Recommended)
Push changes to trigger automatically:
```bash
git add .
git commit -m "Update raw data"
git push origin main
```

#### Manual Trigger
1. Go to **GitHub repository** → **Actions** tab
2. Select workflow: **Insurance Data Preprocessing Pipeline**
3. Click **Run workflow**
4. Choose **main** branch
5. Click **Run workflow**

#### Create Release
1. Go to **Actions** tab
2. Select **Advanced Preprocessing with Data Release**
3. Click **Run workflow**
4. Set **create_release** to `true`
5. Click **Run workflow**

## 📊 Data Processing

### Raw Dataset
- **Rows**: 1,338
- **Columns**: 7 (age, sex, bmi, children, smoker, region, charges)
- **Format**: CSV
- **Size**: ~55 KB

### Processing Steps
1. **Data Quality Check** → 1 duplicate found
2. **Remove Duplicates** → 1,337 records remain
3. **Encode Categorical Variables**:
   - `sex`: female (0), male (1)
   - `smoker`: no (0), yes (1)
   - `region`: northeast (0), northwest (1), southeast (2), southwest (3)
4. **Standardize Features** → Mean = 0, Std = 1
5. **Generate Report** → Comprehensive preprocessing report

### Output Dataset
- **Rows**: 1,337 (after duplicate removal)
- **Columns**: 7 (6 features + target)
- **Format**: CSV (standardized values)
- **Size**: ~167 KB
- **Ready for ML**: ✓ Yes

## 📝 Preprocessing Report Content

The `preprocessing_report.txt` includes:
- Original vs. preprocessed dataset shape
- Preprocessing steps applied
- Feature statistics after scaling
- Target variable statistics
- Final dataset information

## 🛠️ Dependencies

```txt
pandas>=1.3.0
numpy>=1.20.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

## 📦 Artifacts & Downloads

### From GitHub Actions
1. Go to completed workflow run
2. Scroll to "Artifacts" section
3. Download `preprocessed-data-*` (contains both CSV and report)

### From Repository
- Navigate to `preprocessing/insurance_preprocessing/`
- Download files directly or clone repository

## 🔄 Workflow Monitoring

### View Execution Logs
1. **Actions** tab → Select completed run
2. Click job to expand and see detailed logs
3. Each step shows execution time and output

### Check Status
- Green checkmark (✓) = Successful
- Red X = Failed
- Orange circle = Running
- Yellow circle = Queued

## 🎯 Use Cases

### For Data Scientists
- Automated data pipeline for reproducibility
- Version control for preprocessed datasets
- Scheduled preprocessing for incremental data

### For Model Development
- Always have latest preprocessed data in artifacts
- Automated quality checks before model training
- Historical versions available for comparison

### For Collaboration
- Team members can trigger processing manually
- All updates tracked in commit history
- Releases for milestone datasets

## 🔐 Security

- ✓ No hardcoded credentials
- ✓ Uses GitHub-provided `GITHUB_TOKEN`
- ✓ Commits signed by `github-actions[bot]`
- ✓ Data remains within repository
- ✓ No external API calls

## 📈 Cost

- **GitHub Actions**: Free tier = 2,000 minutes/month
- **Workflow runtime**: ~1-2 minutes per run
- **Free tier budget**: Sufficient for ~1,000 runs/month

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| Workflow not triggered | Verify branch is `main` and files changed match trigger paths |
| "File not found" error | Check relative paths in `automate_M-Deco-Prasetyo.py` |
| Package installation fails | Update `requirements.txt` with compatible versions |
| No artifacts available | Check workflow completed successfully in Actions tab |

## 📚 Documentation

- **Notebook**: See `preprocessing/Template_Eksperimen_MSML.ipynb` for manual steps
- **Automation**: See `preprocessing/automate_M-Deco-Prasetyo.py` for implementation
- **Workflows**: See `.github/WORKFLOWS_README.md` for detailed setup guide

## 👤 Author

**M-Deco-Prasetyo**

Machine Learning Experimentation & Automation  
Class: Supervised Machine Learning (MSML)

---

**Last Updated**: June 2, 2026  
**Status**: ✅ Complete (Advance Level)
