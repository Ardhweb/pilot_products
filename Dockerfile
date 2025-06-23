# # # Use a slim Python image based on Debian Bookworm
# # FROM python:3.10-slim-bookworm

# # # Force update for apt-get before installing basic tools to prevent issues
# # # with an extremely stale cache, though this might still show warnings.
# # # It's here to ensure we have *some* package list for the next install.
# # RUN apt-get update || true # Allow failure here, as keys might be missing initially


# # # Install core dependencies needed for key management and basic operations.
# # # dirmngr is vital for gpg --recv-keys, ca-certificates for HTTPS, gnupg for gpg.
# # RUN apt-get install -y --no-install-recommends \
# #     gnupg \
# #     dirmngr \
# #     curl \
# #     ca-certificates

# # # Clean up apt lists immediately after install to prevent further issues with stale data
# # RUN rm -rf /var/lib/apt/lists/*

# # # --- START GPG KEY FIX ---

# # # Strategy 1: Directly add the specific missing keys from keyserver.
# # # This directly addresses the specific NO_PUBKEY errors you are seeing.
# # # Using 'keyserver.ubuntu.com' which is generally reliable.
# # # `set -eux;` provides debugging output and exits on error.
# # RUN set -eux; \
# #     export DEBIAN_FRONTEND=noninteractive; \
# #     for key in \
# #         0E98404D386FA1D9 \
# #         6ED0E7B82643E131 \
# #         F8D2585B8783D481 \
# #         54404762BBB6E853 \
# #         BDE6D2B9216EC7A8 \
# #     ; do \
# #         echo "Attempting to fetch key: $key"; \
# #         gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys "$key" || \
# #         gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$key"; \
# #     done; \
# #     echo "Exporting fetched keys to /etc/apt/trusted.gpg.d/debian-specific-keys.gpg"; \
# #     gpg --export 0E98404D386FA1D9 6ED0E7B82643E131 F8D2585B8783D481 54404762BBB6E853 BDE6D2B9216EC7A8 > /etc/apt/trusted.gpg.d/debian-specific-keys.gpg; \
# #     echo "Keys added. Running apt-get update."; \
# #     apt-get update

# # # --- END GPG KEY FIX ---

    
# # # Install all system dependencies required by WeasyPrint and other build tools.
# # # This list is comprehensive based on your provided information.
# # RUN apt-get install -y --no-install-recommends \
# #     build-essential \
# #     libcairo2 \
# #     libcairo2-dev \
# #     libpango-1.0-0 \
# #     libpangocairo-1.0-0 \
# #     # pango1.0-tools (from your list) is typically not needed in a runtime image,
# #     # it provides command-line tools, not libraries.
# #     # libpango1.0-dev (from your list) is covered by libpango-1.0-0 and libpangocairo-1.0-0
# #     libgdk-pixbuf2.0-0 \
# #     libgdk-pixbuf2.0-dev \
# #     libffi-dev \
# #     shared-mime-info \
# #     libjpeg-dev \
# #     libpng-dev \
# #     libharfbuzz-dev \
# #     libfribidi-dev && \
# #     rm -rf /var/lib/apt/lists/*

# # # Set working directory inside the container
# # WORKDIR /app

# # # Copy requirements and install Python dependencies.
# # COPY requirements.txt .
# # RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# # # Copy the rest of the project files.
# # COPY . .

# # # Expose the port your Django application will run on
# # EXPOSE 8000

# # # Run the Django server.
# # CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# # Use a slim Python image based on Debian Bookworm
# FROM python:3.10-slim-bookworm

# # Avoid interactive prompts
# ENV DEBIAN_FRONTEND=noninteractive

# # Update APT and install required packages in one clean layer
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gnupg2 \
#     dirmngr \
#     curl \
#     ca-certificates \
#     build-essential \
#     libcairo2 \
#     libcairo2-dev \
#     libpango-1.0-0 \
#     libpangocairo-1.0-0 \
#     libgdk-pixbuf2.0-0 \
#     libgdk-pixbuf2.0-dev \
#     libffi-dev \
#     shared-mime-info \
#     libjpeg-dev \
#     libpng-dev \
#     libharfbuzz-dev \
#     libfribidi-dev && \
#     rm -rf /var/lib/apt/lists/*

# # Optional: GPG key fix (only needed if you had NO_PUBKEY errors)
# # If not needed, you can remove this block entirely
# RUN set -eux; \
#     for key in \
#         0E98404D386FA1D9 \
#         6ED0E7B82643E131 \
#         F8D2585B8783D481 \
#         54404762BBB6E853 \
#         BDE6D2B9216EC7A8 \
#     ; do \
#         echo "Attempting to fetch key: $key"; \
#         gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys "$key" || \
#         gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$key"; \
#     done; \
#     gpg --export 0E98404D386FA1D9 6ED0E7B82643E131 F8D2585B8783D481 54404762BBB6E853 BDE6D2B9216EC7A8 > /etc/apt/trusted.gpg.d/debian-specific-keys.gpg

# # Set working directory
# WORKDIR /app

# # Copy Python dependencies and install
# COPY requirements.txt .
# RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# # Copy source code
# COPY . .

# # Expose Django port
# EXPOSE 8000

# # Run Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Use a slim Python image based on Debian Bookworm

FROM python:3.10-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    curl \
    ca-certificates \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libpq-dev \
    libcairo2 \
    libcairo2-dev \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libgdk-pixbuf2.0-dev \
    libffi-dev \
    shared-mime-info \
    libjpeg-dev \
    libpng-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
