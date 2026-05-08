import json
from typing import Callable, Any
from huggingface_hub import HfApi, create_repo


def upload_files(
    api: HfApi, repo: str, display_func: Callable[..., Any] | None = None
) -> dict[str, str]:
    """
    Uploads the following files to the specified repo (and creates the repo if it doesn't exist).
    
    :param api: The HfApi object created after the caller has logged in using the huggingface_hub `login()` method.
    :param repo: The full repository name to upload to on Huggingface (eg. `your_user/my-repo`).
    :param display_func: The function used to display the result of uploading files (this should always be the display function for Jupyter notebooks)

    :return: A dictionary of the form { repo_id: <> } denoting where the files were uploaded to.

    :post: Creates a `repo.json` file containing the necessary information to submit to Gradescope (ie. contents of the returned dictionary as a `json`).
    """

    # Create repo & get ID
    repo_url = create_repo(repo_id=repo, private=False, exist_ok=True)
    repo = repo_url.repo_id

    # Attempt to upload files from local directory
    filepaths = ["model.pkl", "pyproject.toml", ".python-version"]

    for p in filepaths:
        if not display_func:
            api.upload_file(
                path_or_fileobj=f"./{p}",
                path_in_repo=p,
                repo_id=repo,
                repo_type="model",
            )
            continue

        display_func(
            api.upload_file(
                path_or_fileobj=f"./{p}",
                path_in_repo=p,
                repo_id=repo,
                repo_type="model",
            )
        )

    submit_json = {"repo_id": repo}

    with open("./repo.json", "w") as f:
        json.dump(submit_json, f, indent=2)

    return submit_json
