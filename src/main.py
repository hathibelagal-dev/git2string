import argparse
from concatenator import FileConcatenator
import emoji


def main():
    parser = argparse.ArgumentParser(
        description="Concatenate all files of a Git repo into a single prompt."
    )
    parser.add_argument("repo_path", help="Path to the root of the repository")
    parser.add_argument(
        "--include-binary",
        action="store_true",
        help="Include binary files in concatenation",
    )
    parser.add_argument(
        "--output-file", default="llm_prompt.txt", help="Name of the output file"
    )
    parser.add_argument(
        "--output-encoding", default="utf-8", help="Encoding for output file"
    )

    args = parser.parse_args()

    concatenator = FileConcatenator(
        args.repo_path, args.output_file, args.include_binary, args.output_encoding
    )
    _, n_ignored = concatenator.concatenate()
    print(
        emoji.emojize(
            f":thumbs_up: All valid files have been concatenated into {args.output_file}"
        )
    )
    if n_ignored > 0:
        print(
            emoji.emojize(
                f":thumbs_up: {n_ignored} files were ignored due to .gitignore or .r2pignore rules"
            )
        )


if __name__ == "__main__":
    main()
