# src/analysis/performance.py
import numpy as np

def calculate_sharpe_ratio(returns: np.ndarray, risk_free_rate: float = 0.0, 
                          periods_per_year: int = 252) -> float:
    """
    Calculate the annualized Sharpe ratio.
    
    Args:
        returns: Array of asset returns
        risk_free_rate: Annual risk-free rate (default 0.0)
        periods_per_year: Number of periods per year (default 252)
        
    Returns:
        Annualized Sharpe ratio
    """
    excess_returns = returns - risk_free_rate/periods_per_year
    return np.sqrt(periods_per_year) * np.mean(excess_returns) / np.std(excess_returns)

def calculate_sortino_ratio(returns: np.ndarray, risk_free_rate: float = 0.0,
                           periods_per_year: int = 252) -> float:
    """
    Calculate the annualized Sortino ratio.
    
    Args:
        returns: Array of asset returns
        risk_free_rate: Annual risk-free rate (default 0.0)
        periods_per_year: Number of periods per year (default 252)
        
    Returns:
        Annualized Sortino ratio
    """
    excess_returns = returns - risk_free_rate/periods_per_year
    downside_returns = returns[returns < 0]
    if len(downside_returns) == 0:
        return np.inf
    downside_std = np.std(downside_returns)
    return np.sqrt(periods_per_year) * np.mean(excess_returns) / downside_std