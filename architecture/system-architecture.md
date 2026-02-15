# System Architecture Overview

This document outlines the high-level architecture of the MLOps Production Governance framework.

## Core Components

- Airflow Orchestrator (15-day retraining schedule)
- ETL pipeline (rolling 90-day extraction)
- Model training (3M / 1M / 15D windows)
- Accuracy gating layer
- Environment-based deployment (Dev → PreProd → Prod)
- S3 versioned model artifacts
- Batch inference container
- Rollback control mechanism

Architecture diagram will be added here.
