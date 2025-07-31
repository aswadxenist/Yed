from typing import Any, Dict, List, Optional

def validate_data(data: Any) -> bool:
    """Validate input data
    
    Args:
        data: Data to validate
        
    Returns:
        True if data is valid, False otherwise
    """
    return data is not None

def format_output(data: Dict[str, Any]) -> str:
    """Format dictionary data to string
    
    Args:
        data: Dictionary to format
        
    Returns:
        Formatted string representation
    """
    return '\n'.join(f'{k}: {v}' for k, v in data.items())

def process_list(items: List[str], prefix: Optional[str] = None) -> List[str]:
    """Process a list of items with optional prefix
    
    Args:
        items: List of items to process
        prefix: Optional prefix to add to each item
        
    Returns:
        Processed list of items
    """
    if prefix:
        return [f'{prefix}: {item}' for item in items]
    return items.copy()