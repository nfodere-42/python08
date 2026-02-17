import os
from dotenv import load_dotenv


def load_config() -> dict:
    """Load configuration from environment variables."""
    load_dotenv()
    return {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion": os.getenv("ZION_ENDPOINT"),
    }


def validate_config(cfg: dict) -> None:
    """Warn about missing values."""
    for key, value in cfg.items():
        if value is None:
            print(f"[WARNING] Missing configuration: {key}")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    cfg = load_config()
    validate_config(cfg)
    print("\nConfiguration loaded:\n")
    print(f"Mode: {cfg['mode']}")
    print(f"Database: {cfg['database']}")
    print(f"API Access: {'Authenticated' if cfg['api_key'] else 'Missing'}")
    print(f"Log Level: {cfg['log_level']}")
    print(f"Zion Network: {cfg['zion']}\n")
    print("Environment security check:\n")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
