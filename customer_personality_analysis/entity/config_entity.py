from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str
    ingested_data_path: str
