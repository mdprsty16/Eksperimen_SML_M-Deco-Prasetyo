"""
Automation script for Insurance Dataset Preprocessing
Author: M-Deco-Prasetyo
Purpose: Convert raw insurance data into preprocessed, model-ready dataset
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings

warnings.filterwarnings('ignore')


class InsuranceDataPreprocessor:
    """
    A class to handle all preprocessing steps for the insurance dataset.
    """
    
    def __init__(self, raw_data_path):
        """
        Initialize the preprocessor with raw data path.
        
        Parameters:
        -----------
        raw_data_path : str
            Path to the raw insurance CSV file
        """
        self.raw_data_path = raw_data_path
        self.df = None
        self.df_preprocessed = None
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.X_scaled = None
        self.y = None
        
    def load_data(self):
        """
        Load the raw dataset from CSV file.
        
        Returns:
        --------
        pd.DataFrame
            The loaded dataset
        """
        print("Loading raw data...")
        self.df = pd.read_csv(self.raw_data_path)
        print(f"[OK] Dataset loaded successfully. Shape: {self.df.shape}")
        print(f"  Columns: {list(self.df.columns)}")
        return self.df
    
    def check_data_quality(self):
        """
        Check and report data quality issues.
        
        Returns:
        --------
        dict
            Dictionary containing data quality metrics
        """
        print("\n" + "="*60)
        print("Data Quality Check")
        print("="*60)
        
        quality_metrics = {
            'total_rows': len(self.df),
            'total_columns': len(self.df.columns),
            'missing_values': self.df.isnull().sum().sum(),
            'duplicate_rows': self.df.duplicated().sum(),
            'memory_usage_mb': self.df.memory_usage(deep=True).sum() / 1024**2
        }
        
        print(f"Total Rows: {quality_metrics['total_rows']}")
        print(f"Total Columns: {quality_metrics['total_columns']}")
        print(f"Missing Values: {quality_metrics['missing_values']}")
        print(f"Duplicate Rows: {quality_metrics['duplicate_rows']}")
        print(f"Memory Usage: {quality_metrics['memory_usage_mb']:.2f} MB")
        
        return quality_metrics
    
    def remove_duplicates(self):
        """
        Remove duplicate rows from the dataset.
        
        Returns:
        --------
        int
            Number of duplicates removed
        """
        print("\n" + "="*60)
        print("Removing Duplicates")
        print("="*60)
        
        self.df_preprocessed = self.df.copy()
        initial_rows = len(self.df_preprocessed)
        self.df_preprocessed = self.df_preprocessed.drop_duplicates()
        duplicates_removed = initial_rows - len(self.df_preprocessed)
        
        print(f"Duplicates removed: {duplicates_removed}")
        print(f"Shape after removing duplicates: {self.df_preprocessed.shape}")
        
        return duplicates_removed
    
    def encode_categorical_variables(self):
        """
        Encode categorical variables using Label Encoding.
        
        Returns:
        --------
        dict
            Dictionary mapping column names to their label encoders
        """
        print("\n" + "="*60)
        print("Encoding Categorical Variables")
        print("="*60)
        
        categorical_cols = self.df_preprocessed.select_dtypes(include=['object']).columns
        
        for col in categorical_cols:
            le = LabelEncoder()
            self.df_preprocessed[col] = le.fit_transform(self.df_preprocessed[col])
            self.label_encoders[col] = le
            
            # Print encoding mapping
            mapping = dict(zip(le.classes_, le.transform(le.classes_)))
            print(f"\n{col}:")
            for original, encoded in mapping.items():
                print(f"  {original} -> {encoded}")
        
        return self.label_encoders
    
    def separate_features_and_target(self):
        """
        Separate features (X) and target variable (y).
        
        Returns:
        --------
        tuple
            (X, y) - Features and target variable
        """
        print("\n" + "="*60)
        print("Separating Features and Target")
        print("="*60)
        
        X = self.df_preprocessed.drop('charges', axis=1)
        self.y = self.df_preprocessed['charges']
        
        print(f"Features shape: {X.shape}")
        print(f"Target shape: {self.y.shape}")
        print(f"Feature columns: {list(X.columns)}")
        
        return X, self.y
    
    def standardize_features(self, X):
        """
        Standardize numerical features using StandardScaler.
        
        Parameters:
        -----------
        X : pd.DataFrame
            The feature dataframe
            
        Returns:
        --------
        pd.DataFrame
            Scaled features
        """
        print("\n" + "="*60)
        print("Standardizing Features")
        print("="*60)
        
        X_scaled = self.scaler.fit_transform(X)
        self.X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
        
        print(f"Scaling completed successfully")
        print(f"\nFeature statistics after scaling:")
        print(self.X_scaled.describe())
        
        return self.X_scaled
    
    def create_final_dataset(self):
        """
        Create the final preprocessed dataset with features and target.
        
        Returns:
        --------
        pd.DataFrame
            Final preprocessed dataset
        """
        print("\n" + "="*60)
        print("Creating Final Dataset")
        print("="*60)
        
        preprocessed_data = self.X_scaled.copy()
        preprocessed_data['charges'] = self.y.values
        
        print(f"Final dataset shape: {preprocessed_data.shape}")
        print(f"\nFirst 5 rows of preprocessed data:")
        print(preprocessed_data.head())
        
        return preprocessed_data
    
    def save_preprocessed_data(self, output_path):
        """
        Save the preprocessed data to CSV file.
        
        Parameters:
        -----------
        output_path : str
            Path where the preprocessed data will be saved
        """
        print("\n" + "="*60)
        print("Saving Preprocessed Data")
        print("="*60)
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
            print(f"Created output directory: {output_dir}")
        
        # Save preprocessed data
        preprocessed_data = self.create_final_dataset()
        preprocessed_data.to_csv(output_path, index=False)
        
        print(f"[OK] Preprocessed data saved to: {output_path}")
        print(f"  File size: {os.path.getsize(output_path) / 1024:.2f} KB")
        
        return preprocessed_data
    
    def generate_preprocessing_report(self, report_path):
        """
        Generate a detailed preprocessing report.
        
        Parameters:
        -----------
        report_path : str
            Path where the report will be saved
        """
        print("\n" + "="*60)
        print("Generating Preprocessing Report")
        print("="*60)
        
        report = []
        report.append("="*60)
        report.append("INSURANCE DATASET PREPROCESSING REPORT")
        report.append("="*60)
        report.append("")
        
        report.append("1. DATASET OVERVIEW")
        report.append("-" * 60)
        report.append(f"Original dataset shape: {self.df.shape}")
        report.append(f"Preprocessed dataset shape: {self.X_scaled.shape}")
        report.append("")
        
        report.append("2. PREPROCESSING STEPS APPLIED")
        report.append("-" * 60)
        report.append(f"[OK] Removed duplicates")
        report.append(f"[OK] Encoded categorical variables: {list(self.label_encoders.keys())}")
        report.append(f"[OK] Standardized numerical features")
        report.append("")
        
        report.append("3. FEATURE STATISTICS AFTER SCALING")
        report.append("-" * 60)
        report.append(self.X_scaled.describe().to_string())
        report.append("")
        
        report.append("4. TARGET VARIABLE STATISTICS")
        report.append("-" * 60)
        report.append(self.y.describe().to_string())
        report.append("")
        
        report.append("5. FINAL DATASET INFORMATION")
        report.append("-" * 60)
        report.append(f"Rows: {len(self.X_scaled)}")
        report.append(f"Columns: {len(self.X_scaled.columns) + 1}")  # +1 for target
        report.append(f"Column names: {list(self.X_scaled.columns) + ['charges']}")
        report.append("")
        
        report_text = "\n".join(report)
        
        # Save report
        report_dir = os.path.dirname(report_path)
        if report_dir and not os.path.exists(report_dir):
            os.makedirs(report_dir, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        print(f"[OK] Report saved to: {report_path}")
        print(report_text)
    
    def run_full_pipeline(self, output_csv_path, report_path=None):
        """
        Execute the complete preprocessing pipeline.
        
        Parameters:
        -----------
        output_csv_path : str
            Path where the preprocessed CSV will be saved
        report_path : str, optional
            Path where the preprocessing report will be saved
            
        Returns:
        --------
        pd.DataFrame
            The final preprocessed dataset
        """
        print("\n" + "="*80)
        print("STARTING INSURANCE DATA PREPROCESSING PIPELINE")
        print("="*80)
        
        # Step 1: Load data
        self.load_data()
        
        # Step 2: Check data quality
        self.check_data_quality()
        
        # Step 3: Remove duplicates
        self.remove_duplicates()
        
        # Step 4: Encode categorical variables
        self.encode_categorical_variables()
        
        # Step 5: Separate features and target
        X, y = self.separate_features_and_target()
        
        # Step 6: Standardize features
        self.standardize_features(X)
        
        # Step 7: Save preprocessed data
        preprocessed_data = self.save_preprocessed_data(output_csv_path)
        
        # Step 8: Generate report (optional)
        if report_path:
            self.generate_preprocessing_report(report_path)
        
        print("\n" + "="*80)
        print("PREPROCESSING PIPELINE COMPLETED SUCCESSFULLY!")
        print("="*80 + "\n")
        
        return preprocessed_data


def main():
    """
    Main function to run the preprocessing pipeline.
    """
    # Define paths using script location for reliable relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    raw_data_path = os.path.join(project_root, 'insurance_raw', 'insurance.csv')
    output_dir = os.path.join(script_dir, 'insurance_preprocessing')
    output_csv_path = os.path.join(output_dir, 'insurance_preprocessed.csv')
    report_path = os.path.join(output_dir, 'preprocessing_report.txt')
    
    # Create preprocessor instance
    preprocessor = InsuranceDataPreprocessor(raw_data_path)
    
    # Run the full pipeline
    preprocessed_data = preprocessor.run_full_pipeline(output_csv_path, report_path)
    
    return preprocessed_data


if __name__ == "__main__":
    preprocessed_data = main()
