FROM python:3.13-slim

# Create app directory
WORKDIR /app

# Install system dependencies required by some Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential git curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the full repository into the image so pip can build the package
COPY . /app/

# Use pip to install the project dependencies (adk) from pyproject
# Generate a temporary requirements file from pyproject.toml in a portable way
RUN pip install --upgrade pip setuptools wheel \
    && python -c "import tomllib,sys; data=tomllib.loads(open('pyproject.toml','r',encoding='utf-8').read()); deps=data.get('project',{}).get('dependencies',[]); open('requirements-build.txt','w').write('\n'.join(deps))" \
    && if [ -s requirements-build.txt ]; then pip install -r requirements-build.txt; fi \
    && pip install . \
    && rm -f requirements-build.txt

# (repository already copied above)

# Expose a default port - ADK web may use 8080 or another port; leave as a hint
EXPOSE 8080

# Default command requested by the user
CMD ["sh", "-c", "adk web src/hd_google_hackathon/agents --host 0.0.0.0 --port 8080"]
