# ML Models Setup Instructions

This directory should contain the trained machine learning models required for spam detection.

## Required Model Files

The following model files are required for the spam detection system to work:

- `layer1_logreg_model.pkl` - First layer logistic regression model (Binary classification: Ham vs Others)
- `layer2_logreg_model.pkl` - Second layer logistic regression model (Spam type classification)
- `vectorizer_layer1.pkl` - TF-IDF vectorizer for first layer
- `vectorizer_layer2.pkl` - TF-IDF vectorizer for second layer

## How to Obtain Models

Since these are large files (>50MB combined), they are excluded from git. You have several options:

### Option 1: Train Your Own Models

1. **Prepare your dataset** - Collect labeled email data (ham/spam)
2. **Run training script** - Train the models using your dataset
3. **Place models here** - Save trained models in this directory

### Option 2: Download Pre-trained Models

Contact the project maintainers to obtain the pre-trained models:

```bash
# Models will be provided as a separate download
# Extract them to this directory
```

### Option 3: Using Google Drive/Dropbox Links

The models might be available via cloud storage links:

```bash
# Download links will be provided in the main README.md
# Place downloaded models in this directory
```

## Model Usage

Once the models are placed in this directory, the FastAPI backend will automatically load them on startup.

## Storage Requirements

- Total size: ~50-80MB for all model files
- Memory usage: ~100-200MB when loaded in memory
- Minimum Python packages: scikit-learn, joblib, numpy

## Troubleshooting

If you get errors like "Model files not found":

1. Ensure all 4 model files are in this directory
2. Check file permissions
3. Verify Python can import joblib and scikit-learn
4. Check console logs for detailed error messages

## Backup Recommendation

Keep a backup of these model files as they take time to retrain if lost.
