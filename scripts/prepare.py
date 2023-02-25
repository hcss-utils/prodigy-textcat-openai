import typing
from pathlib import Path

import srsly
import typer

JSON = typing.Dict[str, typing.Any]
EXCLUDE = ["resolved_text_lemmatized", "text"]


def main(input_path: Path, output_path: Path) -> None:
    seen_tasks = set()
    annotation_task = []
    for line in srsly.read_jsonl(input_path):
        text = line["meta"]["text"]
        if text in seen_tasks:
            continue

        annotation_task.append(
            {
                "text": text,
                "meta": {k: v for k, v in line["meta"].items() if k not in EXCLUDE},
            }
        )
        seen_tasks.add(text)

    srsly.write_jsonl(output_path, annotation_task)


if __name__ == "__main__":
    typer.run(main)
