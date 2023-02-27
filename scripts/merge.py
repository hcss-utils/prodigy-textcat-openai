from pathlib import Path

import srsly
import typer


def main(input_folder: Path, output_file: Path) -> int:
    data = []
    for f in input_folder.rglob("predictions_*.jsonl"):
        lines = srsly.read_jsonl(f)
        for line in lines:
            data.append(line)
        typer.echo(f)
    srsly.write_jsonl(output_file, data)
    return 0


if __name__ == "__main__":
    typer.run(main)
