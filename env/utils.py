import os

def set_env_variable(key, value, env_file='.env'):
    """Add or update a key-value pair in the .env file."""
    # Read the existing .env file
    env_vars = {}
    if os.path.exists(env_file):
        with open(env_file, 'r') as file:
            for line in file:
                # Skip comments and empty lines
                if line.strip() and not line.startswith("#"):
                    k, v = line.split('=', 1)
                    env_vars[k.strip()] = v.strip()
    
    # Update or add the new key-value pair
    env_vars[key] = value

    # Write back to the .env file
    with open(env_file, 'w') as file:
        for k, v in env_vars.items():
            file.write(f"{k}={v}\n")
