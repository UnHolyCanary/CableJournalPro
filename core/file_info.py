from pathlib import Path


def get_file_info(filename: str) -> dict:
    """
    Возвращает информацию о выбранном файле.
    """

    file = Path(filename)

    return {
        "name": file.name,
        "folder": str(file.parent),
        "size_mb": round(file.stat().st_size / (1024 * 1024), 2),
    }