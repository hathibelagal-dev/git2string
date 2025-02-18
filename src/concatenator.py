from ignore_handler import IgnoreHandler
from file_handler import FileHandler
from tqdm import tqdm
import os


class FileConcatenator:
    def __init__(self, repo_path, output_file, include_binary=False, encoding="utf-8"):
        """Initialize with paths and binary inclusion flag."""
        self.repo_path = repo_path
        self.output_file = output_file
        self.ignore_handler = IgnoreHandler(repo_path)
        self.file_handler = FileHandler(include_binary)

    def concatenate(self):
        """Concatenate files from the repo path to the output file."""

        total_files = sum(len(files) for _, _, files in os.walk(self.repo_path))
        with tqdm(total=total_files, desc="Concatenating") as pbar:
            with open(self.output_file, "w", encoding="utf-8") as outfile:
                for root, _, files in os.walk(self.repo_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if not self.ignore_handler.should_ignore(file_path):
                            content = self.file_handler.read_file(file_path)
                            if content is not None:
                                relative_path = os.path.relpath(
                                    file_path, self.repo_path
                                )
                                outfile.write(f"--- START OF {relative_path} ---\n")
                                outfile.write(content)
                                outfile.write(f"\n--- END OF {relative_path} ---\n")
                                outfile.write("\n\n")
                            pbar.update(1)

        return total_files, self.ignore_handler.n_ignored
