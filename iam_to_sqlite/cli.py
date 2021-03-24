import click
import subprocess
import sqlite_utils
import json


@click.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.version_option()
def cli(db_path):
    "Load Amazon IAM data into a SQLite database"
    process = subprocess.run(
        ["aws", "iam", "get-account-authorization-details"], capture_output=True
    )
    data = json.loads(process.stdout)
    db = sqlite_utils.Database(str(db_path))
    db["Users"].upsert_all(data["UserDetailList"], pk="UserId")
    db["Groups"].upsert_all(data["GroupDetailList"], pk="GroupId")
    db["Roles"].upsert_all(data["RoleDetailList"], pk="RoleId")
    db["Policies"].upsert_all(data["Policies"], pk="PolicyId")
