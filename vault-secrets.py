import os
import hvac


def get_vault_secret(secret_path):
    client = hvac.Client(
        url=os.getenv('VAULT_ADDR'),
        token=os.getenv('VAULT_TOKEN')
    )

    try:
        secret = client.secrets.kv.v2.read_secret_version(
            path=secret_path
        )
        return secret['data']['data']
    except Exception as e:
        logging.error(f"Error reading secret: {e}")
        return None
