from huggingface_hub import snapshot_download

model_id = "TommyDIL/BroBot"  # Replace with the ID of the model you want to download
snapshot_download(repo_id=model_id, local_dir="brodel")
