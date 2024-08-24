SUMMARY_PROMPT = """
You are an advanced language model tasked with generating a concise summary. Given the data from, please follow these steps:

1. **Analyze Content**: Analyze the data and identify what it is about.
2. **Extract Key Points**: Note down the most significant points or elements from the analysis.
3. **Condense Information**: Synthesize the key points into a coherent summary.
4. **Limit**: Ensure the summary is concise, mentions the most important points and does not exceed 50 words.

Note: The response should be the summary only. Also, do not include any markdown formatting in the response.
"""

KEY_OBJECTS_PROMPT = """
You are an advanced language model tasked with identifying key objects or terms. Given the data, please follow these steps:

1. **Scan for Key Elements**: Scan the data and identify the most significant objects or terms.
2. **Compile a List**: Create a list of the most significant objects or terms identified from the analysis.
3. **Limit**: Ensure the response contains no more than 50 words in total. (So, only get the most important ones)

Note: The response should be the list only. Also, it should be markdown formatted.
"""