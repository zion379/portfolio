#!/usr/bin/env python3
"""
Sync a local folder (e.g. NAS mount) to the portfolio-general R2 bucket.

Usage:
    python sync_to_r2.py /path/to/local/assets
    python sync_to_r2.py /path/to/local/assets --dry-run
"""

import os
import sys
import argparse
import mimetypes
import boto3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = "09036693922922918ba202e3cfee1be0"
BUCKET_NAME = "portfolio-general"
ENDPOINT_URL = f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com"


def get_client():
    return boto3.client(
        "s3",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
    )


def sync(source_dir: Path, dry_run: bool = False):
    client = get_client()
    source_dir = source_dir.resolve()

    uploaded = 0
    skipped = 0

    for file_path in source_dir.rglob("*"):
        if not file_path.is_file():
            continue

        key = str(file_path.relative_to(source_dir))
        content_type, _ = mimetypes.guess_type(str(file_path))
        content_type = content_type or "application/octet-stream"

        # Check if identical file already exists in R2
        try:
            head = client.head_object(Bucket=BUCKET_NAME, Key=key)
            remote_size = head["ContentLength"]
            local_size = file_path.stat().st_size
            if remote_size == local_size:
                print(f"  skip  {key}")
                skipped += 1
                continue
        except client.exceptions.ClientError:
            pass  # file doesn't exist yet

        print(f"  {'(dry-run) ' if dry_run else ''}upload  {key}  [{content_type}]")
        if not dry_run:
            client.upload_file(
                str(file_path),
                BUCKET_NAME,
                key,
                ExtraArgs={"ContentType": content_type},
            )
        uploaded += 1

    print(f"\nDone — {uploaded} uploaded, {skipped} skipped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync local assets to R2 ham-media bucket")
    parser.add_argument("source", help="Local folder to sync (e.g. NAS mount path)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without uploading")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.exists():
        print(f"Error: {source} does not exist.")
        sys.exit(1)

    sync(source, dry_run=args.dry_run)

