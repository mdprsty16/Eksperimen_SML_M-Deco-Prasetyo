# 🚀 GitHub Actions Quick Start Guide

## Project Structure ✓
```
Eksperimen_SML_M-Deco-Prasetyo/
├── .github/workflows/
│   ├── preprocessing.yml              ← Basic workflow
│   └── advanced-preprocessing.yml     ← Advanced workflow
├── insurance_raw/
│   └── insurance.csv                  ← Raw data (1,338 rows)
├── preprocessing/
│   ├── Template_Eksperimen_MSML.ipynb ← Notebook (experimentation)
│   ├── automate_M-Deco-Prasetyo.py    ← Automation script
│   └── insurance_preprocessing/       ← Output folder
│       ├── insurance_preprocessed.csv ✓ (1,337 rows - ready for ML)
│       ├── preprocessing_report.txt   ✓ (detailed report)
│       └── backups/                   ✓ (versioned backups)
├── requirements.txt                   ✓ (dependencies)
├── README.md                          ✓ (main documentation)
└── .github/WORKFLOWS_README.md        ✓ (workflows guide)
```

## Two Workflows Configured

### 1️⃣ Basic Pipeline (`preprocessing.yml`)
**Auto-triggers on:**
- Push to main (changes in `insurance_raw/` or `preprocessing/`)
- Manual trigger from GitHub UI

**Output:**
- Preprocessed CSV ✓
- Report ✓
- Downloadable artifact (30 days)

### 2️⃣ Advanced Pipeline (`advanced-preprocessing.yml`)
**Features:**
- Everything from basic +
- Data quality validation
- Timestamped backups
- Can create GitHub Release
- Extended retention (90 days)
- Detailed execution summary

**Manual option:**
- Create Release with `create_release=true`

## How to Trigger

### Method 1: Automatic (Recommended)
```bash
git add .
git commit -m "Update data or script"
git push origin main
```
✓ Workflow starts automatically in ~10 seconds

### Method 2: Manual Trigger
1. Go to GitHub repo → **Actions** tab
2. Select **Insurance Data Preprocessing Pipeline** (or Advanced)
3. Click **Run workflow**
4. Click **Run workflow** again
✓ Starts in ~10 seconds

## What Happens When Workflow Runs

1. ✓ Setup Python 3.11
2. ✓ Install dependencies (`requirements.txt`)
3. ✓ Run `automate_M-Deco-Prasetyo.py`
4. ✓ Verify output files created
5. ✓ Run quality checks (advanced only)
6. ✓ Commit preprocessed data to repo
7. ✓ Upload artifacts
8. ✓ Generate summary

**Time**: ~1-2 minutes

## Download Preprocessed Data

### From GitHub
1. Navigate to `preprocessing/insurance_preprocessing/`
2. Click on files
3. Click Download button

### From GitHub Actions (Latest Artifact)
1. Go to **Actions** tab
2. Click latest completed run
3. Scroll down to **Artifacts**
4. Click download button next to `preprocessed-data-*`
5. Contains: CSV + Report + Backups

## Monitoring Workflow Status

### Check Status
- **Actions** tab → Green ✓ = Success
- **Actions** tab → Red ✗ = Failed
- View logs: Click run → Expand steps

### View Summary
- Click completed run
- Scroll to **Job Summary** section
- Shows execution details, timestamps, row counts

## Workflow Outputs

| File | Size | Purpose |
|------|------|---------|
| `insurance_preprocessed.csv` | 167 KB | Model-ready dataset |
| `preprocessing_report.txt` | 2 KB | Processing details |
| Backups (advanced) | 167 KB | Timestamped copies |

## Features

### ✅ Automated
- No manual intervention needed
- Runs automatically on data/script changes

### ✅ Versioned
- Timestamped backups
- Optional GitHub Releases
- Full history in commits

### ✅ Monitored
- Quality validation
- Step-by-step logs
- Execution summaries

### ✅ Accessible
- Download anytime from Actions
- Download from repository
- Download from Releases (if created)

## Customization

### Change Auto-Trigger Paths
Edit `.github/workflows/preprocessing.yml`, line with:
```yaml
paths:
  - 'insurance_raw/**'
  - 'preprocessing/automate_*.py'
```

### Add Schedule (Weekly)
Add to workflow `on:` section:
```yaml
schedule:
  - cron: '0 0 * * 0'  # Sunday midnight
```

### Change Artifact Days
Edit `retention-days:` in workflows (default 30 or 90)

## Troubleshooting

| Problem | Check |
|---------|-------|
| Workflow not showing | Push to `main` branch with `.github/workflows/` |
| Not auto-triggering | Verify paths in `on.push.paths` match your changes |
| Failed run | Click run → Expand steps → Read error messages |
| Can't find outputs | Check workflow completed successfully (green ✓) |
| Large artifact | Data is expected size (~167 KB for this dataset) |

## GitHub Actions Status Badge

Add to your README to show workflow status:

### Markdown
```markdown
![Preprocessing](https://github.com/USERNAME/REPO/actions/workflows/preprocessing.yml/badge.svg)
```

Replace:
- `USERNAME` with your GitHub username
- `REPO` with repository name

## Cost (Free Tier)

- ✓ 2,000 minutes/month (free)
- ✓ This workflow uses ~1-2 min per run
- ✓ Can run ~1,000 times/month on free tier

## Next Steps

1. ✓ Push files to GitHub
2. ✓ Go to Actions tab
3. ✓ Watch workflow run
4. ✓ Download artifacts or preprocessed data
5. ✓ Use preprocessed CSV for ML models

---

**All set!** Your GitHub Actions automation is ready. 🎉
