# src/data/loader.py
import pandas as pd
from typing import Optional, Union

class DataLoader:
    def __init__(self, file_path: str):
        """
        Initialize the DataLoader with a file path.
        
        Args:
            file_path: Path to the data file
        """
        self.file_path = file_path
        self.data = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Load data from the specified file path.
        
        Returns:
            Loaded DataFrame
        """
        # Try different file formats
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path, parse_dates=True, index_col=0)
        elif self.file_path.endswith(('.xls', '.xlsx')):
            self.data = pd.read_excel(self.file_path, parse_dates=True, index_col=0)
        elif self.file_path.endswith('.json'):
            self.data = pd.read_json(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use .csv, .xls, .xlsx, or .json")
            
        return self.data
    
    def clean_data(self, method: str = 'ffill') -> pd.DataFrame:
        """
        Clean the loaded data.
        
        Args:
            method: Method for filling missing values (default: 'ffill')
            
        Returns:
            Cleaned DataFrame
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")
            
        # Forward fill missing values
        self.data = self.data.fillna(method=method).dropna()
        return self.data