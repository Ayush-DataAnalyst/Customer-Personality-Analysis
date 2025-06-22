from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# ✅ 👇 This reads all dependencies from requirements.txt
with open("requirements.txt") as f:
    LIST_OF_REQUIREMENTS = f.read().splitlines()

# 🛠 Metadata and install config
setup(
    name="customer_personality_analysis",
    version="0.0.1",
    author="Ayush-DataAnalyst",
    description="A modular ML pipeline to perform customer personality analysis using clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ayush-DataAnalyst/Customer-Personality-Analysis",
    author_email="ayushshimpi02@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.10",
    install_requires=LIST_OF_REQUIREMENTS
)
