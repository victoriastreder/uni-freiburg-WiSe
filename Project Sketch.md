```mermaid
graph TD
    subgraph "Project Planning"
        A1[Hypothesis Generation]
        A2[Hypothesis Revision]
    end

    subgraph "Literature Review"
        B1[Literature Search]
    end

    subgraph "Data Collection"
        C1[Data Compilation]
    end

    subgraph "Data Analysis"
        D1[Statistical Tests]
        D2[Graphical Representation]
    end

    subgraph "Project Writing"
        E1[First Draft]
        E2[Peer Review]
        E3[Revision]
        E4[Submission]
    end

    %% Styling to make it look like a board
    style A1 fill:#f9f,stroke:#333,stroke-width:2px
    style B1 fill:#bbf,stroke:#333,stroke-width:2px
    style C1 fill:#bfb,stroke:#333,stroke-width:2px
    style D1 fill:#fbf,stroke:#333,stroke-width:2px
    style E1 fill:#fff,stroke:#333,stroke-width:2px
```

```mermaid
gantt
    title WiSe Project Plan
    dateFormat YYYY-MM-DD
    axisFormat %m/%d
    section Project Planning
    hypothesis generation :t1, 2026-10-19, 1w
    hypothesis revision :t2, 2026-10-26, 1w
    section Literature Review
    literature search :t3, 2026-10-26, 2w
    section Data Collection
    data compilation :t4, 2026-11-02, 4w
    section Data Analysis
    statistical tests :t5, 2026-11-23, 3w
    graphical representation :t6, 2026-11-23, 3w
    section Project Writing
    first draft :t7, 2027-01-11, 1d
    peer review :t8, 2027-01-11, 2w
    revision :t9, 2027-01-25, 9w
    submisison :10, 2027-03-31, 1d
```

# Literature
October
## Literature Collection
##

# Data
November
## Notes
- all data are natural tidal waters
- grouping by river basin? then correlate latitude, soil depth, sequestration, organic carbon
- standardize size and tonnes of carbon
- create a prediction model based on correlations?
## Methodology
1. Linear Regression
2. Mixed-Effects Model

# Writing
December

# Review
January

# Finalization 
February

# Submission
March

Risk Management
```mermaid
mindmap
  root((Risk Management))
    Data Availability
      Risk: Insufficient Open Source Data
      Impact: Project Stall / Lack of Significance
      Mitigation: Use Proxy Data / Expand Database Search
    Data Quality
      Risk: Inconsistent Units or Missing Values
      Impact: Inaccurate Conclusions
      Mitigation: Data Normalization / Rigorous Cleaning
    Technical Execution
      Risk: Coding Errors in Analysis
      Impact: Invalid Statistical Results
      Mitigation: Cross-validation / Peer-review of Code
    Timeline
      Risk: Processing Delays
      Impact: Missed Submission Deadline
      Mitigation: Bi-weekly Milestones / MVP Approach
    Scientific Outcome
      Risk: No Significant Correlation Found
      Impact: Weak Research Conclusion
      Mitigation: Analyze Reasons for Absence of Correlation
```

Kanban
```mermaid
kanban
  Project Planning
    Hypothesis Generation
    Hypothesis Revision
  Literature Review
    Literature Search
  Data Collection
    Data Compilation
  Data Analysis
    Statistical Tests
    Graphical Representation
  Project Writing
    First Draft
    Peer Review
    Revision
    Submission
```
