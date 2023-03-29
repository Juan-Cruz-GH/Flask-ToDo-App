from src.web import create_app
from pathlib import Path

app = create_app(static_folder=Path(__file__).parent.joinpath("static"))

if __name__ == "__main__":
    app.run(debug=True)
