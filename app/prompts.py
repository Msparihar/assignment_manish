SUMMARY_SYSTEM_PROMPT = """
You are an advanced language model tasked with generating concise and comprehensive summaries of various types of data, including text documents, images, and structured data.
"""

SUMMARY_USER_PROMPT = """
Please analyze the following data and generate a concise summary:

<parsed_data>
{parsed_data}
</parsed_data>

Guidelines for summary generation:
1. Analyze the content to understand its context, purpose, and main ideas.
2. Identify and extract the most significant points, themes, or elements.
3. Synthesize these key points into a coherent and comprehensive summary.
4. Ensure the summary is concise, mentioning only the most important points.
5. Limit the summary to approximately 100 words.
6. Adapt your approach based on the type of data (text, image, or structured data).
7. For text and structured data, focus on main themes, trends, or insights.
8. For images, describe the main visual elements, their arrangement, and overall impression.

Please provide the summary as plain text without any formatting.
"""

KEY_OBJECTS_SYSTEM_PROMPT = """
You are an advanced language model tasked with identifying and listing key objects, terms, or concepts from various types of data, including text documents, images, and structured data.
"""

KEY_OBJECTS_USER_PROMPT = """
Please analyze the following data and identify the key objects, terms, or concepts:

<parsed_data>
{parsed_data}
</parsed_data>

Guidelines for identifying key elements:
1. Thoroughly scan the data to identify the most significant objects, terms, or concepts.
2. For text data, focus on important nouns, technical terms, or recurring themes.
3. For structured data, identify key variables, categories, or data points.
4. For images:
   - List the main objects or people visible
   - Note any text present in the image
   - Describe key visual elements (e.g., colors, shapes, patterns)
   - Identify any symbols or icons
5. Prioritize elements that are central to the main topic or purpose of the data.
6. Create a concise list of these key elements.
7. Limit the total response to approximately 100 words, focusing on the most crucial items.
8. Present the list as plain text, with each item on a new line, without numbering or bullet points.

Please provide the list of key objects, terms, or concepts as plain text without any formatting.
"""