# GitHub Actions Preprocessing Pipeline

## Overview
Automated preprocessing pipeline using GitHub Actions that runs every time code is pushed or on manual trigger.

## Workflows

### 1. Basic Preprocessing Workflow (`preprocessing.yml`)
**Triggers:**
- Push to `main` branch when `insurance_raw/` or automation script changes
- Manual trigger via GitHub UI (`workflow_dispatch`)
- Pull requests to `main`

**What it does:**
- Sets up Python 3.11 environment
- Installs dependencies from `requirements.txt`
- Runs the preprocessing automation script
- Verifies output files were created
- Commits preprocessed data back to repository
- Uploads artifacts (30-day retention)
- Generates execution summary

**Output:**
- ✅ `insurance_preprocessed.csv` - Ready for ML models
- ✅ `preprocessing_report.txt` - Detailed report
- 📦 GitHub Artifact for download

### 2. Advanced Preprocessing Workflow (`advanced-preprocessing.yml`)
**Additional Features:**
- Data quality validation
- Creates versioned backups with timestamps
- Extracts dataset metrics (row count, etc.)
- Can create GitHub Release with preprocessed data
- Extended artifact retention (90 days)
- Comprehensive job summary
- Optional release creation for versioning

**Additional Triggers:**
- Manual input: `create_release` - Creates a GitHub Release with the preprocessed data

## How to Use

### Automatic Triggers
The workflows run automatically when:
1. Changes are pushed to `main` branch in:
   - `insurance_raw/` folder
   - `preprocessing/automate_*.py` files
   - `.github/workflows/` folder

### Manual Trigger
Click on **Actions** tab in GitHub → Select workflow → **Run workflow**

### View Results
1. **GitHub Actions Tab:**
   - Click **Actions** tab
   - Select the completed run
   - View step logs and summary

2. **Download Artifacts:**
   - In the completed run, scroll down
   - Click **Download** next to artifact name

3. **Repository Changes:**
   - Preprocessed data auto-committed to `preprocessing/insurance_preprocessing/`

## Workflow Configuration

### Dependencies
All dependencies are listed in `requirements.txt`:
```
pandas>=1.3.0
numpy>=1.20.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

### Environment
- **OS**: Ubuntu Latest
- **Python**: 3.11
- **Runs on**: GitHub-hosted runners (free tier available)

## File Structure
```
Eksperimen_SML_M-Deco-Prasetyo/
├── .github/
│   └── workflows/
│       ├── preprocessing.yml          # Basic workflow
│       └── advanced-preprocessing.yml # Advanced workflow with releases
├── insurance_raw/
│   └── insurance.csv
├── preprocessing/
│   ├── automate_M-Deco-Prasetyo.py
│   ├── Template_Eksperimen_MSML.ipynb
│   └── insurance_preprocessing/
│       ├── insurance_preprocessed.csv
│       ├── preprocessing_report.txt
│       └── backups/
├── requirements.txt
└── README.md
```

## Processing Steps

Each workflow executes:
1. **Data Loading** - Reads raw CSV from `insurance_raw/`
2. **Quality Check** - Validates data integrity
3. **Duplicate Removal** - Removes duplicate rows
4. **Categorical Encoding** - Encodes categorical features
5. **Feature Standardization** - Scales features (mean=0, std=1)
6. **Report Generation** - Creates detailed report

## Monitoring & Troubleshooting

### View Logs
- GitHub Actions → Run → Click job → Expand steps

### Common Issues

| Issue | Solution |
|-------|----------|
| Workflow not triggering | Check branch is `main` and paths match triggers |
| Python package errors | Ensure `requirements.txt` is updated |
| File not found error | Verify relative paths in automation script |
| Permission denied | Ensure `GITHUB_TOKEN` has proper permissions |

## Security

- Uses GitHub-generated `GITHUB_TOKEN` (scoped to repository)
- Commits signed by `github-actions[bot]`
- No secrets or credentials in workflow files
- Data remains in repository

## Cost

- **GitHub Actions**: Free tier includes 2,000 minutes/month
- This workflow typically runs in < 2 minutes
- Suitable for unlimited runs within free tier

## Advanced Features

### Create GitHub Release
To create a versioned release with preprocessed data:
1. Go to **Actions** tab
2. Select **Advanced Preprocessing with Data Release**
3. Click **Run workflow**
4. Set **create_release** to `true`
5. Click **Run workflow**

This creates:
- Tagged release (e.g., `preprocessing-2024-01-15_10-30-45`)
- Download link for preprocessed data
- Release notes with processing details

## Customization

### Modify Trigger Events
Edit `.github/workflows/preprocessing.yml`:
```yaml
on:
  push:
    branches: [main]
    paths: ['insurance_raw/**', 'preprocessing/**']  # Add/remove as needed
  schedule:
    - cron: '0 0 * * 0'  # Weekly trigger (Sunday midnight)
```

### Change Artifact Retention
```yaml
retention-days: 30  # Change to desired number of days
```

### Add Notifications
Extend with email or Slack notifications:
```yaml
- name: Send notification
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

## Support

For issues or questions:
1. Check workflow logs in GitHub Actions
2. Review automation script: `preprocessing/automate_M-Deco-Prasetyo.py`
3. Verify `requirements.txt` dependencies
