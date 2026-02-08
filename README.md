# NTD Public Transit Service Data Preparation

## Overview

This repository contains a Python-based workflow for cleaning and preparing
public transit service data from the National Transit Database (NTD) for 
transportation planning analysis.

The focus of this example is on data organization, validation, and
documentation rather than advanced modeling. The cleaned output is intended
to support reporting, summary analysis, and joins with spatial boundary
layers in GIS environments.

---

## Data Source

**National Transit Database (NTD)**  
U.S. Department of Transportation

**Dataset:**  
NTD Annual Data View - Service (by Agency)

**Report Year:**  
2022

**Source Portal:**  
https://data.transportation.gov

The dataset provides agency-level totals for public transit service metrics
reported to the National Transit Database. It is publicly available and
can be used for planning, reporting, and performance monitoring.

**Access Method:**  
Direct CSV download from the USDOT Open Data Portal (Socrata platform).

*Note:*  
The dataset is also accessible via the Socrata API. CSV export was used here
to avoid row limits and to align with common ArcGIS and planning workflows.

---

## Data Preparation Workflow

The script performs the following steps:

1. Load raw NTD service data from CSV.
2. Standardize column names for consistency and compatibility across tools.
3. Convert service, mileage, population, and hour fields to numeric values.
4. Validate key identifiers such as agency, state, and report year.
5. Log potential data quality issues (e.g., negative values) without
   removing records.
6. Export a cleaned dataset suitable for reporting and GIS workflows.

All cleaning rules and assumptions are documented directly in the source
code to support transparency and reproducibility.

---

## Output Files

### data/processed/ntd_2022_public_transit_clean.csv

A cleaned and validated agency-level dataset intended for
Tabular analysis in Excel or statistical software

---

## Notes on Spatial Use

This dataset is reported at the agency level and does not include geographic
coordinates. The cleaned output is intended for use by joining to 
agency-level or regional boundary layers (e.g., transit agency service
areas, MPO boundaries, or state boundaries) as needed for spatial analysis.

---

## Tools Used

- Python  
- pandas  

The script is intentionally lightweight and does not rely on proprietary GIS
libraries.
