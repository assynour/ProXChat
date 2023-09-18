# Evaluation Results

This repository contains the evaluation results based on the `questions.xlsx` file. These questions are extracted from the dataset shared in the research paper ["Towards a Natural Language Conversational Interface for Process Mining (2022)"](https://link.springer.com/chapter/10.1007/978-3-030-98581-3_20), categorized under `Event Log`.

## Files Included

### `raw_results_processed.xlsx`

This file contains raw results related to LLM reasoning, the generated query, the database result, LLM's interpretation of the result, and details of the error-fixing trials by the LLM in cases of erroneous SQL queries.

### `raw_results_processed_labeled.xlsx`

This file includes the results of our manual inspection, which is stored in an additional column named **correct?**. Please note that this manual inspection is a labor-intensive exercise and is still ongoing.

### `global_statistics.xlsx`

This file provides global statistics about the number of questions for which the LLM failed to generate syntactically correct queries.


