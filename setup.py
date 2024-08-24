import os

def create_project_structure():
    base_dir = "llm-data-analyzer"
    directories = [
        "app",
        "tests"
    ]
    files = [
        "app/__init__.py",
        "app/main.py",
        "app/prompts.py",
        "app/utils.py",
        "tests/__init__.py",
        "Dockerfile",
        "docker-compose.yml",
        "requirements.txt",
        "README.md"
    ]

    os.makedirs(base_dir, exist_ok=True)
    for directory in directories:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)
    
    for file in files:
        open(os.path.join(base_dir, file), 'a').close()

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()