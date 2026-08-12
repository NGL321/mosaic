# PROTOTYPE — the Mosaic base image recipe.
#
# TOOLING TRACK. PROTOCOL §1's test: if this changed silently, could a result already in
# the record become wrong? No — because a build produces a NEW digest, every env.lock
# pins the digest it froze against, and every manifest records the digest it ran on. A
# bump is invisible to everything already frozen. That is not a convenience; it is the
# whole reason this file is allowed to be tooling track.
#
# WHAT BELONGS HERE, AND NOTHING ELSE:
#   everything a Python lockfile cannot express.
#
# Not "the big things". Not "the slow things". The division is `what pip resolves` versus
# `what pip presupposes`. A lockfile that names torch presupposes an interpreter, a libc,
# and a CUDA userspace it cannot itself install. Those are baked. Research packages are
# never baked — they are the thing being searched over.

FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04@sha256:0f6bfcbf267e65123bcc2287e2153dedfc0f24772fb5ce84afe16ac4b2fada95

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3.11 python3.11-venv python3-pip \
        git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# uv resolves and installs the per-Inquiry lock. It is apparatus, not a research package,
# so it is pinned here rather than in any Inquiry's lock.
RUN python3.11 -m pip install --no-cache-dir uv==0.4.27

# The marker. Read by tools/run_inquiry.py, which refuses to start outside a Mosaic image.
# NOTE — this is a SELF-REPORT and the prototype's findings say so plainly: a container
# cannot verify its own digest from the inside. It catches the accident (someone running
# a script on the bare desktop), not the adversary. The load-bearing enforcement is the
# publish gate, which is outside the container entirely.
RUN echo "mosaic-base" > /etc/mosaic-env

WORKDIR /work
