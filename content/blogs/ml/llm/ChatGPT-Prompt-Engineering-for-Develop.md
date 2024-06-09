Title: Blog: ChatGPT Prompt Engineering for Developers
Date: 2024-05-07 19:31
Modified: 2024-05-09 21:31
Category: blogs
Tags: ml
slug: ml-llm-promt-engineering

## Two Types of LLM

1. Base LLM:

    * Predicts next word, based on text training data.

2. Instruction Tuned LLM

    * Fine-tune on instructions.
    * RLHF: Reinforcement Learning with Human Feedback.

## Guidelines

* Principle 1: Write clear and specific instructions.

  * Tactic 1: Use Delimiters.
  * Tactic 2: Ask for structured outputs.
  * Tactic 3: Ask model to check if conditions are satisfied.
  * Tactic 4: Few-shot prompting. Give successful examples then ask to perform task.

* Principle 2: Give the model time to think.

  * Tactic 1: Specify the steps required to complete a task.
  * Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion.

* Limitations
  * Hallucinations: These are fabricated ideas which is made up response with no relevance to real life scenarios.

## Iterative Prompt Development

* Idea -> Implement -> Experimental Result -> Error Analysis.
* Limit the number of words/sentences/characters.

```text
Your task is to help a marketing team create a description for 
sale season of a retail stores of the products based on 
technical fact sheet.

Write a product description based on information provided
in the technical specifications delimited by two backtics.

Use at most 50 words.

Technical specifications: ``{{text}}``
```

* Ask to focus on specific details.
* Ask to organize in table.

## Summarizing

* You can summarize the product for specific relevant area.
* Limit the number of character/words/sentences.
* You can also extract the information rather than summarize.

## Inferring

* Infer sentiments from text.
* Example

```text
What is the sentiment of the following tweet, which is delimited with double backticks?

Tweet: ``<tweet>``
```

* You can also get answer in one word like positive or negative using text like,

```text
...
Give your answer as a single word, either "psoitive" or "negative".
```

* Identiy the types of emotions,

```text
...
Give me a list of emotions that writer of the following tweet is expressing. Include no more than
six items in the list. Format your answer as lower-case separated by commas. 
```

* Extract information,

```text
Identity the following item from tweet:
- User the tweet is refering to.
- Product the user if tweeting about.

Format your response as JSON object with 
referred_user & product as keys. If information is not
present then use "unknown".
```

* You can also merge the above under one task.
* Infer topic from text.

```text
Determine five topics that are being discussed in the following text,
which is delimited by two backticks.

Make each item two or three words long.

```

##  Transforming

* It can perform following task but not limited to these:
  * Translation

  ```text
  Translate the following English text to German:
  ```

  ```text
  Tell me what language is this:
  ```

  ```text
  Translate the following text to French in both formal and informal forms:
  ```

  * Spelling/Grammer Checking

  ```text
  Proofread and correct the following text and rewrite the corrected version.
  If you don't find the error then just say "Everything is Alright".
  ```

  * Format conversion

  ```text
  Translate the following JSON into HTML format:
  ```

  * Tone adjustment

  ```text
  Translate the following slang to business letter:
  ```

## Expanding

* You can ask you model to ask as assistant and reply to the customer with required setiments.
* Make sure you use it responsibly and it generates relevant response.

##  Chatbot

* We can set various role based on requirements. Allowed values are:
  * system: You can set the behaviour of the model.
  * assistant: This is what model outputs.
  * user: This is what useer inputs to the model.
* Each conversation is seperate context.
