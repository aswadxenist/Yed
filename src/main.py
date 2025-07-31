from typing import Optional

class YedApplication:
    def __init__(self):
        self.name = "Yed"
        self.version = "1.0.0"
    
    def start(self) -> None:
        """Start the Yed application"""
        print(f"Starting {self.name} version {self.version}")
    
    def process_data(self, data: Optional[str] = None) -> str:
        """Process input data
        
        Args:
            data: Input data to process
            
        Returns:
            Processed data result
        """
        if data is None:
            return "No data provided"
        return f"Processing: {data}"

def main():
    app = YedApplication()
    app.start()
    result = app.process_data("test data")
    print(result)

if __name__ == "__main__":
    main()